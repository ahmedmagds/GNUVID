#!/usr/bin/env python3
# PROGRAM: GNUVID (GNU-based Virus IDentification) is a Python3 program
# It ranks CDS nucleotide sequences in a genome fna file based on the number of
# observed exact CDS nucleotide matches in a public or private database.
# It is created also to type SARS-CoV-2 genome using a wgMLST approach
# The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing.
# It automatically assign allele numbers to each of the ORFs and a Sequence Type (ST) to the genome.
# It is based on the panallelome approach of WhatsGNU (https://github.com/ahmedmagds/WhatsGNU)


# Copyright (C) 2020 Ahmed M. Moustafa

#########################################################################################
# LICENSE
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#########################################################################################

# DATE CREATED: November 23, 2020

# AUTHOR: Ahmed M Moustafa

# CONTACT1: moustafaam@email.chop.edu
# CONTACT2: ahmedmagdy2009@hotmail.com

# AFFILIATION: Pediatric Infectious Disease Division, Children’s Hospital of Philadelphia,
# Abramson Pediatric Research Center, University of Pennsylvania, Philadelphia,
# Pennsylvania, 19104, USA

# CITATION1: Ahmed M Moustafa and Paul J Planet
# GNUVID: a tool for typing SARS-CoV-2
import os
import sys
import argparse
import joblib
import pandas as pd
import psutil
import time
import tempfile
from operator import itemgetter
from collections import defaultdict
from sklearn.datasets import make_classification
from sklearn import metrics
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix, make_scorer
from collections import defaultdict
from collections import Counter
START_TIME = time.time()
PARSER = argparse.ArgumentParser(
    prog="GNUVID_Post_Training.py",
    description="This script will predict CC for NA_genomes & summarize CCs",)
PARSER.add_argument("-p","--predict",help="run NA prediction [default OFF]",action="store_true",)
PARSER.add_argument("-s","--subsample",help="subsample fna as query_aln file used so extract right feature [default OFF]",action="store_true",)
PARSER.add_argument(
    "inactive_date",
    type=str,
    help="an inactive date cutoff, usually 1 month before release date, in this format (2021-05-22) to assign status"
)
PARSER.add_argument(
    "quiet_date", type=str, help="a quiet date cutoff, usually 2 weeks before release date, in this format (2021-06-07) to assign status"
)
PARSER.add_argument("metadata", type=str, help="GISAID metadata report")
PARSER.add_argument("ST_GNUVID_report", type=str, help="ST GNUVID txt report")
PARSER.add_argument("DB_RF", type=str, help="Random forest DB (.joblib)")
PARSER.add_argument("features", type=str, help="features (SNPs) positions")
PARSER.add_argument("query_aln", type=str, help="Query Whole Genome SNPs MSA file to analyze (.aln) or Query Whole Genome MSA file (.fna)")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
###########Parse feature positions###############
if ARGS.predict:
    VCF_OBJECT = open(ARGS.features,'r') # has the nucleotide(feature) positions
    features_list = []
    postitions_list = []
    for line in VCF_OBJECT:
        features_list.append(line.rstrip())
        postitions_list.append(int(line.rstrip())-1)
    VCF_OBJECT.close()
    ###########Parse the SNPs alignment file#########
    SNPs_aln = open(ARGS.query_aln,'r')#sequence_file
    SEQUENCES_LIST = []
    order_list = []
    SEQUENCE_STRING = ''
    counter = 0
    for line in SNPs_aln:
        line = line.rstrip()
        if line.startswith(">"):
            if (len(SEQUENCE_STRING) > 0):
                if SEQUENCE_INFO.split('_CC')[-1] == 'NA':
                    counter += 1
                    if counter in [1000,50000,100000,200000,300000,400000,500000,600000,700000]:
                        print('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter),flush=True)
                    lst = list(SEQUENCE_STRING)
                    if ARGS.subsample:
                        lst = [lst[ind] for ind in postitions_list]
                    SEQUENCES_LIST.append(lst)
                    order_list.append(SEQUENCE_INFO)
                SEQUENCE_STRING = ""
            SEQUENCE_INFO = line.lstrip(">")
        else:
            SEQUENCE_STRING += line
    if SEQUENCE_INFO.split('_CC')[-1] == 'NA':
        counter += 1
        if counter in [1000,50000,100000,200000,300000,400000,500000,600000,700000]:
            print('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter),flush=True)
        lst = list(SEQUENCE_STRING)
        if ARGS.subsample:
            lst = [lst[ind] for ind in postitions_list]
        SEQUENCES_LIST.append(lst)
        order_list.append(SEQUENCE_INFO)
    SNPs_aln.close()
    print('Genome included for prediction: ',len(SEQUENCES_LIST))
    print('RAM memory used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter),flush=True)
    ###########Prediction#############
    nucs = ['A', 'C', 'G', 'T', '-']
    DT_model = ARGS.DB_RF #ML model
    START_TIME = time.time()
    loaded_model = joblib.load(DT_model)
    print('RAM memory used after loading model: {}'.format(psutil.virtual_memory()[3]),flush=True)
    seq_array = pd.DataFrame(SEQUENCES_LIST, columns=features_list)
    print("Finished opening model in --- {:.3f} seconds ---".format(time.time() - START_TIME))
    print('RAM memory used after DF: {}'.format(psutil.virtual_memory()[3]),flush=True)
    START_TIME = time.time()
    for i in nucs:
        line = [i] * len(SEQUENCES_LIST[0])
        seq_array.loc[len(seq_array)] = line
    seq_array = pd.get_dummies(seq_array, columns=features_list)
    seq_array.drop(seq_array.tail(len(nucs)).index, inplace=True)
    print("Finished one-hot encoding DF in --- {:.3f} seconds ---".format(time.time() - START_TIME))
    print('RAM memory used after one-hot encoding: {}'.format(psutil.virtual_memory()[3]),flush=True)
    START_TIME = time.time()
    predictions = loaded_model.predict_proba(seq_array)
    prediction_results = []
    for index in range(0,len(predictions),1):
        maxScore = 0
        maxIndex = -1
        # get the max probability score and its assosciated index
        for i in range(len(predictions[index])):
            if predictions[index][i] > maxScore:
                maxScore = predictions[index][i]
                maxIndex = i
        score = maxScore
        prediction = loaded_model.classes_[maxIndex]
        prediction_results.append([prediction,score])
    print('Done Predictions',flush=True)
    ##########GNUVID DB Deidentified Report######
    strains_report_file = open(ARGS.ST_GNUVID_report,'r') #deidentified report
    report_dict = {}
    report_list = []
    header_line = '\t'.join(strains_report_file.readline().rstrip().split('\t')[:-1])
    for line in strains_report_file:
        line = line.rstrip()
        line_list = line.split('\t')
        report_dict[line_list[-1]] = line_list[:-1]
        report_list.append(line_list[-1])
    strains_report_file.close()
############update CCNA with new predictions########
op_name = ARGS.ST_GNUVID_report.split('_deidentified.txt')[0] + '_NAs.txt'
if ARGS.predict:
    fo = open(op_name,'w')
    fo.write(header_line+'\n')
    pred_dict = {}
    for y,isolate in zip(prediction_results,order_list):
        pred_dict[isolate] = y
    counter = 0
    for ST_CC in report_list:
        isolate_details = report_dict[ST_CC]
        if 'CCNA' in ST_CC:
            pred_lst = pred_dict[ST_CC]
            if pred_lst[-1] >= 0.7:
                isolate_details[-1] = pred_lst[0]
                counter += 1
            fo.write('\t'.join(isolate_details)+'\n')
        else:
            fo.write('\t'.join(isolate_details)+'\n')
    print('Total CCNA: ',len(prediction_results))
    print('Genomes reassigned CC: ',counter)
    fo.close()
##########deidentification########
output_obj = open(op_name, 'r')
Output_GNUVID = op_name.rsplit('_NAs.txt')[0] + '_deidentified_NAs.txt'
Output_GNUVID_obj = open(Output_GNUVID, 'w')
header_string = output_obj.readline()
Output_GNUVID_obj.write(header_string)
ST_dict = Counter()
CC_dict = {}
CC_list = []
included_acc_list = []
for line in output_obj:
    line = line.rstrip()
    line_list = line.split('\t')
    Strain_ST = line_list[-2]
    ST_dict[Strain_ST] += 1
    Strain_CC = line_list[-1]
    if Strain_CC != 'NA':
        CC_list.append(Strain_CC)
    Strain_acc = line_list[0].split('|')[-2]
    included_acc_list.append(Strain_acc)
    ST_name_rank = 'ST' + Strain_ST + '_' + str(ST_dict[Strain_ST])
    Strain_new_name = ST_name_rank + '_CC' + Strain_CC
    Output_GNUVID_obj.write(Strain_new_name+'\t'+'\t'.join(line_list[1:])+'\n')
    CC_dict[Strain_acc] = Strain_new_name
    CC_dict[ST_name_rank] = Strain_new_name
Output_GNUVID_obj.close()
print('done with deidentification',flush=True)
output_obj.close()
print('Number of CCs: ',len(Counter(CC_list)))
##########metadata############
meta_obj = open(ARGS.metadata,'r')
meta_obj.readline()
meta_dict = {}
included_acc_set = set(included_acc_list)
for line in meta_obj:
    line_list = line.rstrip().split('\t')
    acc = line_list[2]
    if acc in included_acc_set:
        gis_clade = line_list[10]
        pango_lin = line_list[11]
        aa_subs = line_list[14].rstrip(')').lstrip('(').split(',')#list
        if set(aa_subs) == {''}:
            meta_dict[acc] = [pango_lin,gis_clade,[]]
        else:
            meta_dict[acc] = [pango_lin,gis_clade,aa_subs]
print('Done with metadata parsing',flush=True)
############Parse the DB_isolates report for CCs summary############
input_report_object = open(op_name,'r')
header_line = (input_report_object.readline().rstrip()).split('\t')
ST_index = header_line.index('ST')
try:
  CC_index = header_line.index('CC')
except:
  PARSER.exit(
      status=0,
      message="The report does not have CC column, run goeBURST\n")
try:
  Region_index = header_line.index('Region')
except:
  PARSER.exit(
      status=0,
      message="The report does not have Region\n")
input_report_object.seek(0)
N_counter = 0
input_report_object.readline()
CC_country_dict = defaultdict(list)
CC_dates_dict = defaultdict(list)
CC_region_dict = defaultdict(list)
CC_isolates_dict = defaultdict(list)
CC_STs_dict = defaultdict(list)
CC_acc_dict = {}
aa_subs_dict = defaultdict(list)
gis_clade_dict = defaultdict(list)
pango_dict = defaultdict(list)
CC_list = []
for line in input_report_object:
  line = line.rstrip()
  line_list = line.split('\t')
  if line_list[CC_index] != "NA":
      ST_date = line_list[1]
      ST_country = line_list[2]
      GISAID_acc = line_list[0].split('|')[-2]
      ST_region = line_list[Region_index]
      ST_number = line_list[ST_index]
      CC_number = int(line_list[CC_index])
      if CC_number not in CC_list:
          CC_list.append(CC_number)
      if ST_date.count('-') == 2:
          if len(ST_date) == 10:
              CC_dates_dict[CC_number].append(ST_date)
          else:
              ST_date_list = ST_date.split('-')
              if len(ST_date_list[1]) == 1:
                  ST_date_list[1] = ('0'+ST_date_list[1])
              if len(ST_date_list[2]) == 1:
                  ST_date_list[2] = ('0'+ST_date_list[2])
              ST_date = '-'.join(ST_date_list)
              CC_dates_dict[CC_number].append(ST_date)
      CC_country_dict[CC_number].append(ST_country)
      CC_region_dict[CC_number].append(ST_region)
      CC_STs_dict[CC_number].append(ST_number)
      CC_isolates_dict[CC_number].append(GISAID_acc)
      try:
          pango_dict[CC_number].append(meta_dict[GISAID_acc][0])
          gis_clade_dict[CC_number].append(meta_dict[GISAID_acc][1])
          aa_subs_dict[CC_number].extend(meta_dict[GISAID_acc][2])
      except:
          N_counter += 1
print('isolates without metadata:', N_counter,flush=True)
input_report_object.close()
gzip1 = op_name.split('_ST_report_')[0] +'_report.txt.gz'
gzip2 = op_name.split('_ST_report_')[0] +'_report_deidentified.txt.gz'
os.system('gzip -c {} > {}'.format(op_name, gzip1))
os.system('gzip -c {} > {}'.format(Output_GNUVID, gzip2))
#######WHO Naming#########
VOC_VOI = {"B.1.1.7":'Alpha','Q':'Alpha','B.1.351':'Beta','P.1':'Gamma',
            'B.1.617.2':'Delta','AY':'Delta','C.37':'Lambda','B.1.621':'Mu',
            'B.1.525':'VUM','B.1.526':'VUM','B.1.630':'VUM',
            'B.1.617.1':'VUM','B.1.619':'VUM','B.1.620':'VUM','C.1.2':'VUM',
        'B.1.427':'VUM','B.1.429':'VUM', 'P.2':'VUM','P.3':'VUM',
        'R.1':'VUM','B.1.466.2':'VUM','B.1.1.523':'VUM',
        'AV.1':'VUM','B.1.1.318':'VUM','B.1.1.519':'VUM','AT.1':'VUM',
        'C.36.3':'VUM','B.1.214.2':'VUM','B.1.427/429':'VUM'}
variants_list = list(VOC_VOI.keys())
######Writing report######
inactive_date = ARGS.inactive_date
quiet_date = ARGS.quiet_date
release_date = [inactive_date, quiet_date]
output_report_file = (
          op_name.split("_DB_isolates_ST_report")[0]
          + "_CCs_report.txt")
output_report_object = open(output_report_file,'w')
output_report_file2 = (
          op_name.split("_DB_isolates_ST_report")[0]
          + "_CCs_report.md")
output_report_object2 = open(output_report_file2,'w')
output_report_header = 'Clonal Complex\tNumber of STs/isolates\tMost common 5 countries\tMost common Region\tDate range\tStatus\tPango Lineage (%)\tGISAID Clade (%)\tWHO Naming\tAA Substitutions\n'
output_report_object.write(output_report_header)
output_report_object2.write('| Clonal Complex | Number of STs/isolates | Most common 5 countries | Most common Region | Date range | Status | Pango Lineage (%isolates) | GISAID Clade | WHO Naming | AA Substitutions in >=60% of isolates |\n|----------------|-------------------------|-------------------------|--------------------|------------|--------|---------------------------|--------------|------------|---------------------------------------|\n')
for CC in sorted(CC_list):
    release_date = [inactive_date, quiet_date]
    STs_count = len(set(CC_STs_dict[CC]))
    isolates_count = len(CC_isolates_dict[CC])
    sorted_dates = sorted(CC_dates_dict[CC])
    dates_range = sorted_dates[0] + ' to ' + sorted_dates[-1]
    if sorted_dates[-1] in release_date:
        date_index = release_date.index(sorted_dates[-1])
        if date_index == 0:
            CC_state = "Quiet"
        else:
            CC_state = "Active"
    else:
        release_date.append(sorted_dates[-1])
        state_date = sorted(release_date).index(sorted_dates[-1])
        if state_date == 0:
            CC_state = "Inactive"
        elif state_date == 1:
            CC_state = "Quiet"
        else:
            CC_state = "Active"

    Top_5_countries = Counter(CC_country_dict[CC]).most_common(5)
    Countries_list = []
    for i in Top_5_countries:
        country_percent = i[0] + " ({:.0%})".format(i[1]/isolates_count)
        Countries_list.append(country_percent)
    Top_Region = Counter(CC_region_dict[CC]).most_common(1)[0] #tuple
    Top_Region_percent = Top_Region[0] + " ({:.0%})".format(Top_Region[1]/isolates_count)
    Top_Pango = Counter(pango_dict[CC]).most_common(1)[0] #tuple
    Top_Pango_percent = Top_Pango[0] + " ({:.0%})".format(Top_Pango[1]/isolates_count)
    Top_GIS = Counter(gis_clade_dict[CC]).most_common(1)[0] #tuple
    Top_GIS_percent = Top_GIS[0] + " ({:.0%})".format(Top_GIS[1]/isolates_count)
    aa_changes = Counter(aa_subs_dict[CC]).most_common()
    aa_lst = [x[0]+" ({:.0%})".format(x[1]/isolates_count) for x in aa_changes if (x[1]/isolates_count >= 0.6)]
    if len(aa_lst) == 0:
        aa_lst = ['No AA Substitutions present in >= 60% of the isolates']
    try:
        WHO = VOC_VOI[Top_Pango[0]]
    except:
        try:
            WHO = VOC_VOI[Top_Pango[0].rsplit('.',1)[0]]
        except:
            WHO = 'NA'
    output_report_object.write('{}\t{}/{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
            CC,STs_count,isolates_count,', '.join(Countries_list),
            Top_Region_percent, dates_range, CC_state, Top_Pango_percent,Top_GIS_percent,WHO,','.join(aa_lst)))
    if CC_state == "Active":
        CC_state = "**Active**"
        CC = "**" + str(CC) + "**"
    if CC_state == "**Active**":
        output_report_object2.write('| {} | {}/{} | {} | {} | {} | {} | {} | {} | {} | {} |\n'.format(
            CC,STs_count,isolates_count,', '.join(Countries_list),
            Top_Region_percent, dates_range, CC_state, Top_Pango_percent,Top_GIS_percent,WHO,','.join(aa_lst)))

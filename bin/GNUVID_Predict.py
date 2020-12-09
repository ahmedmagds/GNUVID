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
import time
import tempfile
import logging
import subprocess
from shutil import rmtree as rmt
from operator import itemgetter
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix, make_scorer
from sklearn.model_selection import cross_val_score
START_TIME = time.time()
########################################
PARSER = argparse.ArgumentParser(
    prog="GNUVID_Predict.py",
    description="GNUVID v2.0 uses the natural variation in public genomes of SARS-CoV-2 to \
    rank gene sequences based on the number of observed exact matches (the GNU score) \
    in all known genomes of SARS-CoV-2. It assigns a sequence type to each genome based on \
    its profile of unique gene allele sequences. It can type (using whole genome multilocus sequence typing; wgMLST) \
    your query genome in seconds. GNUVID_Predict is a speedy algorithm for assigning Clonal Complexes \
    to new genomes, which uses machine learning Random Forest Classifier, implemented as of GNUVID v2.0.",
)
PARSER.add_argument(
    "-o",
    "--output_folder",
    type=str,
    help="Output folder and prefix to be created for \
results (default: timestamped GNUVID_results in the current directory)",
)
PARSER.add_argument(
    "-i",
    "--individual",
    help="Individual Output file for each genome showing the allele sequence\
    and GNU score for each gene allele",
    action="store_true",
)
PARSER.add_argument(
    "-f",
    "--force",
    help="Force overwriting existing results folder assigned with -o (default: off)",
    action="store_true",
)
PARSER.add_argument(
    "-q",
    "--quiet",
    help="No screen output [default OFF]",
    action="store_true",
)
PARSER.add_argument(
    "-v",
    "--version",
    help="print version and exit",
    action="version",
    version="%(prog)s 2.0",
)
PARSER.add_argument(
    "query_fna", type=str, help="Query Whole Genome Nucleotide FASTA file to analyze (.fna)"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
Classifier_version = '10/20/2020'
#########blast check##############
try:
    GETVERSION = subprocess.Popen("blastn -version", shell=True, stdout=subprocess.PIPE).stdout
    VERSION = GETVERSION.read()
    print("Found blastn (version:{})".format(VERSION.decode().splitlines()[1]))
except:
    PARSER.exit(status=0, message="Error: blastn cannot be found\n")
#####create results folder######
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
if ARGS.output_folder:
    try:
        os.mkdir(ARGS.output_folder)
        RESULTS_FOLDER = ARGS.output_folder + OS_SEPARATOR
    except:
        if ARGS.force:
            rmt(ARGS.output_folder)
            os.mkdir(ARGS.output_folder)
            RESULTS_FOLDER = ARGS.output_folder + OS_SEPARATOR
        else:
            PARSER.exit(
                status=0,
                message="Folder exists, Please change --output_folder or use --force\n")
else:
    os.mkdir("GNUVID_results_{}".format(TIMESTR))
    RESULTS_FOLDER = "GNUVID_results_{}{}".format(TIMESTR,OS_SEPARATOR)
###############Logging##################
LOG_FILE = 'GNUVID_'+ TIMESTR
if ARGS.quiet:
    LOG_LIST = [
        logging.FileHandler("{0}{1}.log".format(RESULTS_FOLDER, LOG_FILE))
    ]
else:
    LOG_LIST = [
        logging.FileHandler("{0}{1}.log".format(RESULTS_FOLDER, LOG_FILE)),
        logging.StreamHandler()
    ]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
    handlers=LOG_LIST)
if ARGS.force:
    logging.info("overwrote results folder({})".format(RESULTS_FOLDER))
else:
    logging.info("created results folder({})".format(RESULTS_FOLDER))
#############################
if ARGS.output_folder:
    output_file = RESULTS_FOLDER + ARGS.output_folder + '.csv' #name of output
else:
    output_file = RESULTS_FOLDER + "GNUVID_results_{}.csv".format(TIMESTR)
seq_file = ARGS.query_fna#sequence_file
SEQ_OBJECT = open(seq_file,'r')
Script_Path = os.path.realpath(__file__)
DB_Folder_Path = os.path.join(Script_Path.rsplit(OS_SEPARATOR,2)[0], "db")
VCF_file = os.path.join(DB_Folder_Path,'SNPs_15136_OCT.txt') # has the nucleotide(feature) positions
VCF_OBJECT = open(VCF_file,'r')
DT_model = os.path.join(DB_Folder_Path,'GNUVID_10202020_RandomForest.joblib')#ML model
COMP_DB_file = os.path.join(DB_Folder_Path,'GNUVID_10202020_comp_db.joblib')#compressed DB
strains_report_file = os.path.join(DB_Folder_Path,'GNUVID_10202020_DB_isolates_report.txt')
Ref_CDS = os.path.join(DB_Folder_Path,'MN908947.3_cds.fna')
Ref_WG = os.path.join(DB_Folder_Path,'MN908947.3.fasta')
########################################
features_list = []
postitions_list = []
for line in VCF_OBJECT:
    SNP = line.rstrip()
    features_list.append(SNP)
    postitions_list.append(int(SNP)-1)
#############################
ref_obj = open(Ref_WG,'r')
ref_obj.readline()
seq_str = ''
for line in ref_obj:
    line = line.rstrip()
    seq_str += line
refseq_lst = list(seq_str)
ref_obj.close()
########parse DB report########
Genes = ['ORF1ab','Surface_glycoprotein','ORF3a','Envelope_protein',
'Membrane_glycoprotein','ORF6','ORF7a','ORF8','Nucleocapsid_phosphoprotein','ORF10']
ST_allele_Dict = {}
Alleles_dict = {}
ST_dates_country_CC_dict = defaultdict(list)
ST_all_dates = defaultdict(list)
report_object = open(strains_report_file,'r')
report_object.seek(0)
header_line = (report_object.readline().rstrip()).split('\t')
Gene_counter = (header_line.index('ORF1ab')) - 1
ST_index = header_line.index('ST')
Gene_counter = (header_line.index('ORF1ab')) - 1
ORF1ab_index = (header_line.index('ORF1ab'))

try:
    CC_index = header_line.index('CC')
except:
    CC_index = 'NA'
#capturing dates, countries, regions for STs and dates for alleles
report_object.seek(0)
report_object.readline()
if CC_index != 'NA':
    CC_ST_dict = {}
gene_all_alleles_dict = defaultdict(list)
alleles_all_dates = defaultdict(list)
for line in report_object:
    line = line.rstrip()
    line_list = line.split('\t')
    ST_date = line_list[1]
    ST_country = line_list[2]
    ST_CC = line_list[CC_index]
    ST_number = line_list[ST_index]
    Alleles_profile = '_'.join(line_list[ORF1ab_index:ST_index])
    ST_allele_Dict[Alleles_profile] = ST_number
    if (len(ST_date) > 7) and (ST_date.split('-')[0] in ['2020', '2019']):
        if len(ST_date) < 10:
            ST_date_lst = ST_date.split('-')
            if len(ST_date_lst[1]) < 2:
                new_date = '0' + ST_date_lst[1]
                ST_date_lst[1] = new_date
            if len(ST_date_lst[2]) < 2:
                new_date2 = '0' + ST_date_lst[2]
                ST_date_lst[2] = new_date2
            ST_date = '-'.join(ST_date_lst)
        ST_dates_country_CC_dict[ST_number].append((ST_date,ST_country,ST_CC))
    else:
        ST_dates_country_CC_dict[ST_number]
        ST_all_dates[ST_number].append((ST_date,ST_country,ST_CC))
    Gene_counter = (header_line.index('ORF1ab')) - 1
    for gene in Genes:
        Gene_counter += 1
        allele_number = line_list[Gene_counter]
        gene_allele = gene + '_' + allele_number
        if (len(ST_date) > 7):
            gene_all_alleles_dict[gene_allele].append(ST_date)
        else:
            gene_all_alleles_dict[gene_allele]
            alleles_all_dates[gene_allele].append(ST_date)

sorted_ST_data = {}
for ST in ST_dates_country_CC_dict:
    if len(ST_dates_country_CC_dict[ST]) == 0:
        sorted_ST_data[ST] = ST_all_dates[ST]
    else:
        sorted_ST_data[ST] = sorted(ST_dates_country_CC_dict[ST])
sorted_alleles_data = {}
for allele in gene_all_alleles_dict:
    if len(gene_all_alleles_dict[allele]) == 0:
        sorted_alleles_data[allele] = alleles_all_dates[allele]
    else:
        sorted_alleles_data[allele] = sorted(gene_all_alleles_dict[allele])
#########################
START_TIME = time.time()
COMP_DICT = joblib.load(COMP_DB_file)
alleles = []
alleles.append([])
REPORT_LIST = ["Query Gene","GNUVID DB Version","GNU score","length","sequence","Ns count","Allele number",
"First date seen", "Last date seen"]
NA_list = 10 *['NA']
SEQ_STR = ''
query_dict = {}
counter = 0
for line in SEQ_OBJECT:
    line = line.rstrip()
    if line.startswith(">"):
        if len(SEQ_STR) > 0:
            counter += 1
            if ARGS.individual:
                file_name = RESULTS_FOLDER + 'Genome' + str(counter) + '.csv'
                QUERYFILE_IND = open(file_name,'w')
                QUERYFILE_IND.write("{}\n".format(",".join(REPORT_LIST)))
            counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
            query_dict[counter_SEQ_INFO] = SEQ_STR
            QUERYFILE_tmp = tempfile.NamedTemporaryFile(mode='w+')
            QUERYFILE_tmp.write('>'+SEQ_INFO+'\n'+SEQ_STR)
            QUERYFILE_tmp.seek(0)
            blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
            blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sseq sstart send pident qcovs' -out {}".format(Ref_CDS,QUERYFILE_tmp.name, blast_report_tmp.name))
            if blast_results == 0:
                #####Blast results Parser#####
                allele_tmp_lst = []
                allele_tmp_lst.append(counter_SEQ_INFO)
                try:
                    blast_report_tmp.seek(0)
                    Isolate_WG_dict = defaultdict(list)
                    for line2 in blast_report_tmp:
                        line_list = line2.rstrip().split("\t")
                        hit_seq = line_list[1].replace('-','')
                        hit_seq = hit_seq.upper()
                        Isolate_WG_dict[line_list[0]].append(hit_seq)
                    for gene_name in Genes:
                        longest_seq = sorted(Isolate_WG_dict[gene_name], key=len, reverse=True)[0]
                        try:
                            ids_list = COMP_DICT[longest_seq]
                            function, allele_number = ids_list[0].rsplit('_',1)
                            allele_tmp_lst.append(allele_number)
                            if ARGS.individual:
                                SEQ_INFO_fn = SEQ_INFO + '_' + function
                                fst_date = sorted_alleles_data[ids_list[0]][0]
                                lst_date = sorted_alleles_data[ids_list[0]][-1]
                                query_sequence_details = [SEQ_INFO_fn, Classifier_version,
                                ids_list[-1],str(len(longest_seq)),longest_seq, '0',
                                allele_number,fst_date, lst_date]
                        except:
                            Ns_count = 0
                            for Nuc in longest_seq:
                                if Nuc not in ['A','C','G','T']:
                                    Ns_count += 1
                            if Ns_count > 0:
                                GNU_score = 'None'
                                allele_number = 'None'
                            else:
                                GNU_score = '0'
                                allele_number = 'Novel'
                            allele_tmp_lst.append(allele_number)
                            if ARGS.individual:
                                SEQ_INFO_fn = SEQ_INFO + '_' + gene_name
                                query_sequence_details = [SEQ_INFO_fn, Classifier_version,
                                GNU_score, str(len(longest_seq)), longest_seq,
                                str(Ns_count), allele_number, 'NA', 'NA']
                        if ARGS.individual:
                            QUERYFILE_IND.write("{}\n".format(
                                    ",".join(query_sequence_details)))
                    if ARGS.individual:
                        QUERYFILE_IND.close()
                    blast_report_tmp.close()
                    alleles.append(allele_tmp_lst)
                except:
                    tmp_NA_lst = [counter_SEQ_INFO] + NA_list
                    alleles.append(tmp_NA_lst)
                    logging.critical(
                        "Could not parse blastn results for {}".format(SEQ_INFO))
                    if ARGS.individual:
                        logging.critical(
                            "Could not create Individual Output file for {}".format(SEQ_INFO))
            else:
                tmp_NA_lst = [counter_SEQ_INFO] + NA_list
                alleles.append(tmp_NA_lst)
                logging.critical(
                    "Could not run blastn for {}".format(SEQ_INFO))
                if ARGS.individual:
                    logging.critical(
                        "Could not create Individual Output file for {}".format(SEQ_INFO))
            SEQ_STR = ""
        SEQ_INFO = line.lstrip('>')
        #order_list.append(SEQ_INFO)
    else:
        SEQ_STR += line
counter += 1
if ARGS.individual:
    file_name = RESULTS_FOLDER + 'Genome' + str(counter) + '.csv'
    QUERYFILE_IND = open(file_name,'w')
    QUERYFILE_IND.write("{}\n".format(",".join(REPORT_LIST)))
counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
query_dict[counter_SEQ_INFO] = SEQ_STR
QUERYFILE_tmp = tempfile.NamedTemporaryFile(mode='w+')
QUERYFILE_tmp.write('>'+SEQ_INFO+'\n'+SEQ_STR)
QUERYFILE_tmp.seek(0)
blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sseq sstart send pident qcovs' -out {}".format(Ref_CDS,QUERYFILE_tmp.name, blast_report_tmp.name))
if blast_results == 0:
    #####Blast results Parser#####
    allele_tmp_lst = []
    allele_tmp_lst.append(counter_SEQ_INFO)
    try:
        blast_report_tmp.seek(0)
        Isolate_WG_dict = defaultdict(list)
        for line2 in blast_report_tmp:
            line_list = line2.rstrip().split("\t")
            hit_seq = line_list[1].replace('-','')
            hit_seq = hit_seq.upper()
            Isolate_WG_dict[line_list[0]].append(hit_seq)
        for gene_name in Genes:
            longest_seq = sorted(Isolate_WG_dict[gene_name], key=len, reverse=True)[0]
            try:
                ids_list = COMP_DICT[longest_seq]
                function, allele_number = ids_list[0].rsplit('_',1)
                allele_tmp_lst.append(allele_number)
                if ARGS.individual:
                    SEQ_INFO_fn = SEQ_INFO + '_' + function
                    fst_date = sorted_alleles_data[ids_list[0]][0]
                    lst_date = sorted_alleles_data[ids_list[0]][-1]
                    query_sequence_details = [SEQ_INFO_fn, Classifier_version,
                    ids_list[-1],str(len(longest_seq)),longest_seq, '0',
                    allele_number,fst_date, lst_date]
            except:
                Ns_count = 0
                for Nuc in longest_seq:
                    if Nuc not in ['A','C','G','T']:
                        Ns_count += 1
                if Ns_count > 0:
                    GNU_score = 'None'
                    allele_number = 'None'
                else:
                    GNU_score = '0'
                    allele_number = 'Novel'
                allele_tmp_lst.append(allele_number)
                if ARGS.individual:
                    SEQ_INFO_fn = SEQ_INFO + '_' + gene_name
                    query_sequence_details = [SEQ_INFO_fn, Classifier_version,
                    GNU_score, str(len(longest_seq)), longest_seq,
                    str(Ns_count), allele_number, 'NA', 'NA']
            if ARGS.individual:
                QUERYFILE_IND.write("{}\n".format(
                        ",".join(query_sequence_details)))
        if ARGS.individual:
            QUERYFILE_IND.close()
        blast_report_tmp.close()
        alleles.append(allele_tmp_lst)
    except:
        tmp_NA_lst = [counter_SEQ_INFO] + NA_list
        alleles.append(tmp_NA_lst)
        logging.critical(
            "Could not parse blastn results for {}".format(SEQ_INFO))
        if ARGS.individual:
            logging.critical(
                "Could not create Individual Output file for {}".format(SEQ_INFO))
else:
    tmp_NA_lst = [counter_SEQ_INFO] + NA_list
    alleles.append(tmp_NA_lst)
    logging.critical(
        "Could not run blastn for {}".format(SEQ_INFO))
    if ARGS.individual:
        logging.critical(
            "Could not create Individual Output file for {}".format(SEQ_INFO))
SEQ_OBJECT.close()
logging.info("Finished Finding Alleles --- {:.3f} seconds ---".format(time.time() - START_TIME))
#########Divergence of exact matches and prediction##########
exact_match = []
prediction_list = []
prediction_list.append([])
for index in range(1,len(alleles),1):
    try:
        results_data = []
        predict_ST = ST_allele_Dict['_'.join(alleles[index][1:])]
        ST_data = sorted_ST_data[predict_ST]
        ST_1st_date = ST_data[0][0]
        country_1st = ST_data[0][1]
        exact_CC = ST_data[0][2]
        ST_last_date = ST_data[-1][0]
        country_last = ST_data[-1][1]
        p_value = 'Exact'
        results_data = [predict_ST,country_1st,ST_1st_date,ST_last_date,country_last,exact_CC, p_value]
        if exact_CC == 'NA':
            prediction_list.append(alleles[index])
        else:
            alleles[index].extend(results_data)
            exact_match.append(alleles[index])
    except:
        prediction_list.append(alleles[index])
########Failed Exact Matching########
if len(prediction_list) > 0:
    mafft_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
    seq_tmp = tempfile.NamedTemporaryFile(mode='w+')
    for index in range(1,len(prediction_list),1):
        seq_tmp.write('>'+prediction_list[index][0].split('__',1)[-1]+'\n'+query_dict[prediction_list[index][0]]+'\n')
    seq_tmp.seek(0)
    mafft_results = os.system('mafft --quiet --add {} --keeplength {} > {}'.format(seq_tmp.name, Ref_WG,mafft_report_tmp.name))
    if mafft_results == 0:
        try:
            mafft_report_tmp.seek(0)
            tmp_lst = []
            SEQUENCES_LIST = []
            order_list = []
            SEQUENCE_STRING = ''
            nucs = ['A','T','G','C','-']
            for line in mafft_report_tmp:
                line = line.rstrip()
                if line.startswith(">"):
                    if (len(SEQUENCE_STRING) > 0):
                        lst = list(SEQUENCE_STRING)
                        for j in postitions_list:
                            nuc = lst[j].upper()
                            if nuc in nucs:
                                tmp_lst.append(nuc)
                            else:
                                tmp_lst.append(refseq_lst[j])
                        SEQUENCES_LIST.append(tmp_lst)
                        SEQUENCE_STRING = ""
                        tmp_lst = []
                    SEQUENCE_INFO = line.lstrip(">")
                    order_list.append(SEQUENCE_INFO)
                else:
                    SEQUENCE_STRING += line
            lst = list(SEQUENCE_STRING)
            for j in postitions_list:
                nuc = lst[j].upper()
                if nuc in nucs:
                    tmp_lst.append(nuc)
                else:
                    tmp_lst.append(refseq_lst[j])
            SEQUENCES_LIST.append(tmp_lst)
            mafft_report_tmp.close()
            logging.info("Done with mafft")
        except:
            logging.critical("Could not parse mafft results")
    else:
        logging.critical("Could not run mafft")
###########Prediction#############
    START_TIME = time.time()
    loaded_model = joblib.load(DT_model)
    seq_array = pd.DataFrame(SEQUENCES_LIST, columns=features_list)
    logging.info("Finished opening model in --- {:.3f} seconds ---".format(time.time() - START_TIME))
    START_TIME = time.time()
    for i in nucs:
    	line = [i] * len(SEQUENCES_LIST[0])
    	seq_array.loc[len(seq_array)] = line
    seq_array = pd.get_dummies(seq_array, columns=features_list)
    seq_array.drop(seq_array.tail(len(nucs)).index, inplace=True)
    logging.info("Finished one-hot encoding DF in --- {:.3f} seconds ---".format(time.time() - START_TIME))
    START_TIME = time.time()
    predictions = loaded_model.predict_proba(seq_array)
    prediction_results = []
    for index in range(1,len(predictions),1):
        maxScore = 0
        maxIndex = -1
        # get the max probability score and its assosciated index
        for i in range(len(predictions[index])):
            if predictions[index][i] > maxScore:
                maxScore = predictions[index][i]
                maxIndex = i
        score = maxScore
        prediction = loaded_model.classes_[maxIndex]
        if 'None' in prediction_list[index] or 'NA' in prediction_list[index]:
            results_data2 = prediction_list[index] + ['None','NA','NA','NA','NA',prediction,str(score)] #exact_matching results
        else:
            results_data2 = prediction_list[index] + ['Novel','NA','NA','NA','NA',prediction,str(score)] #exact_matching results
        prediction_results.append(results_data2)
#########Convergence of exact matches and prediction##########
final_results = [(int(x[0].split('__',1)[0]),x) for x in exact_match]
final_results.extend([(int(x[0].split('__',1)[0]),x) for x in prediction_results])
sorted_final_results = sorted(final_results, key=itemgetter(0))
#####################OutPut###################
fo = open(output_file,'w')
new_details = ['Exact ST','First country seen','First date seen','Last country seen','Last date seen','CC','probability']
fo.write("Sequence ID,GNUVID DB Version,{},{}\n".format(','.join(Genes),','.join(new_details)))
for y in sorted_final_results:
    seqId = y[1][0].split('__',1)[-1]
    y_results = y[1][1:]
    fo.write('{},{},{}\n'.format(seqId,Classifier_version,','.join(y_results)))
logging.info("Finished prediction in --- {:.3f} seconds ---".format(time.time() - START_TIME))
logging.info("Typed the query isolate/s and wrote {}".format(output_file.rsplit(OS_SEPARATOR,1)[-1]))
logging.info("""Thanks for using GNUVID v2.0, I hope you found it useful.
References:
WhatsGNU 'Moustafa AM and Planet PJ 2020, Genome Biology;21:58'.
MAFFT version 7 'Katoh and Standley 2013, Molecular Biology and Evolution;30:772-780'.
pandas 'Reback et  al. 2020, DOI:10.5281/zenodo.3509134'.
Scikit-learn 'Pedregosa et al. 2011, JMLR; 12:2825-2830'.
BLAST+ 'Camacho et al. 2009, BMC Bioinformatics; 10:421'.
GISAID 'Shu Y. and McCauley J. 2017, EuroSurveillance; 22:13'
The reference genome MN908947 'Wu et al. 2020, Nature; 579:265–269'
eBURST 'Feil et al. 2004, Journal of Bacteriology; 186:1518'
goeBURST 'Francisco et al. 2009, BMC Bioinformatics; 10:152'
PHYLOViZ 2.0 'Nascimento et al. 2017, Bioinformatics; 33:128-129'
The manual is extensive and available to read at https://github.com/ahmedmagds/GNUVID
If you have problems, please file at https://github.com/ahmedmagds/GNUVID/issues""")

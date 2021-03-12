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
START_TIME = time.time()
########################################
PARSER = argparse.ArgumentParser(
    prog="GNUVID_Predict.py",
    description="GNUVID v2.2 uses the natural variation in public genomes of SARS-CoV-2 to \
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
    "-m",
    "--min_len",
    type=int,
    help="minimum sequence length [Default: 15000]",
)
PARSER.add_argument(
    "-n",
    "--n_max",
    type=float,
    help="maximum proportion of ambiguity (Ns) allowed [Default: 0.5]",
)
PARSER.add_argument(
    "-b",
    "--block_pred",
    type=int,
    help="prediction block size, good for limited memory [Default: 1000]",
)
PARSER.add_argument(
    "-e",
    "--exact_matching",
    help="turn off exact matching (no allele will be identified for each  ORF)\
    and only use machine learning prediction [default: False]",
    action="store_true",
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
    version="%(prog)s 2.1",
)
PARSER.add_argument(
    "query_fna", type=str, help="Query Whole Genome Nucleotide FASTA file to analyze (.fna)"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
if bool(vars(ARGS)["individual"]) and bool(vars(ARGS)["exact_matching"]):
    PARSER.exit(status=0, message="Error: You cannot use -i with -e\n")
OS_SEPARATOR = os.sep
Classifier_version = '01/06/2021'
START_TIME0 = time.time()
if ARGS.exact_matching:
    e_matching = 0
else:
    e_matching = 1
if ARGS.block_pred:
    pred_block = ARGS.block_pred
else:
    pred_block = 1000
if ARGS.min_len:
    min_len = ARGS.min_len
else:
    min_len = 15000
if ARGS.n_max:
    n_max = ARGS.n_max
else:
    n_max = 0.5
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
log_name = "{0}{1}.log".format(RESULTS_FOLDER, LOG_FILE)
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
VCF_file = os.path.join(DB_Folder_Path,'SNPs_20188_Jan2021.txt') # has the nucleotide(feature) positions
VCF_OBJECT = open(VCF_file,'r')
DT_model = os.path.join(DB_Folder_Path,'GNUVID_01062021_RandomForest.joblib')#ML model
COMP_DB_file = os.path.join(DB_Folder_Path,'GNUVID_01062021_comp_db.joblib')#compressed DB
strains_report_file = os.path.join(DB_Folder_Path,'GNUVID_01062021_DB_isolates_report.txt')
Ref_CDS = os.path.join(DB_Folder_Path,'MN908947.3_cds.fna')
Ref_WG = os.path.join(DB_Folder_Path,'MN908947.3.fasta')
########################################
VOC_dict = {81085:'P.1',70949:'P.2',72860:'B.1.429 (CAL.20C)',71014:'B.1.351', 46649:'B.1.1.7', 45062:'B.1.1.7',
49676:'B.1.1.7', 54949:'B.1.1.7', 54452:'B.1.1.7', 58534:'B.1.1.7',
57630:'B.1.1.7', 66559:'B.1.1.7', 62415:'B.1.1.7', 67441:'B.1.1.7'}
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
    if (len(ST_date) > 7) and (ST_date.split('-')[0] in ['2021','2020', '2019']):
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
logging.info("Finished Parsing metadata in --- {:.3f} seconds ---".format(time.time() - START_TIME))
##########Quality Check###############
START_TIME = time.time()
alleles = []
NA_list = 10 *['NA']
REPORT_LIST = ["Query Gene","GNUVID DB Version","GNU score","length","sequence","Ns count","Allele number",
"First date seen", "Last date seen"]
counter = 0
SEQ_STR = ''
query_dict = {}
order_list = []
order_dict = {}
failed_list  = []
for line in SEQ_OBJECT:
    line = line.rstrip()
    if line.startswith(">"):
        if len(SEQ_STR) > 0:
            counter += 1
            if ' ' in SEQ_INFO:#fix spaces in fasta id
                SEQ_INFO  =  SEQ_INFO.replace(' ','_')
            if ',' in SEQ_INFO:#fix , in fasta id
                SEQ_INFO  =  SEQ_INFO.replace(',','_')
            if len(SEQ_STR) < min_len:
                    SEQ_INFO = SEQ_INFO + f" failed (seq_len:{len(SEQ_STR)})"
                    counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
                    failed_list.append(counter_SEQ_INFO)
            else:
                N_count = SEQ_STR.upper().count("N")
                N_prop = round((N_count)/len(SEQ_STR), 2)
                if N_prop > n_max:
                    SEQ_INFO = SEQ_INFO + f" failed (N_prop:{N_prop})"
                    counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
                    failed_list.append(counter_SEQ_INFO)
                else:
                    counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
                    query_dict[counter_SEQ_INFO] = SEQ_STR
                    order_list.append(counter_SEQ_INFO)
            #order_dict[SEQ_INFO] = counter_SEQ_INFO
            SEQ_STR = ""
        SEQ_INFO = line.lstrip('>')
    else:
        SEQ_STR += line
counter += 1
if ' ' in SEQ_INFO:#fix spaces in fasta id
    SEQ_INFO  =  SEQ_INFO.replace(' ','_')
if ',' in SEQ_INFO:#fix , in fasta id
    SEQ_INFO  =  SEQ_INFO.replace(',','_')
if len(SEQ_STR) < min_len:
        SEQ_INFO = SEQ_INFO + f" failed (seq_len:{len(SEQ_STR)})"
        counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
        failed_list.append(counter_SEQ_INFO)
else:
    N_count = SEQ_STR.upper().count("N")
    N_prop = round((N_count)/len(SEQ_STR), 2)
    if N_prop > n_max:
        SEQ_INFO = SEQ_INFO + f" failed (N_prop:{N_prop})"
        counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
        failed_list.append(counter_SEQ_INFO)
    else:
        counter_SEQ_INFO = str(counter) + '__' + SEQ_INFO
        query_dict[counter_SEQ_INFO] = SEQ_STR
        order_list.append(counter_SEQ_INFO)
SEQ_OBJECT.close()
if len(order_list) == 0:
    logging.critical("All sequences failed quality check")
    fo = open(output_file,'w')
    fo.write("Sequence ID,GNUVID DB Version,CC,probability,Variant of Concern,Quality Check\n")
    for y in failed_list:
        seq_name_fail = y.split('__',1)[-1]
        seq_name,fail_reason = seq_name_fail.split(' ',1)
        y_results = ['None','None','None',fail_reason]
        fo.write('{},{},{}\n'.format(seq_name,Classifier_version,','.join(y_results)))
    sys.exit(0)
#############qc-passed seq file#################
seq_file_tmp = tempfile.NamedTemporaryFile(mode='w+')
for new_seq_id in order_list:
    seq_file_tmp.write('>'+new_seq_id+'\n'+query_dict[new_seq_id]+'\n')
seq_file_tmp.seek(0)
logging.info("Checked Quality of Sequences in --- {:.3f} seconds ---".format(time.time() - START_TIME))
#########################################################
if e_matching == 1: ##Allele numbers for each record (exact matching)
    if len(query_dict) < 5:
        max_seqs = 5
    else:
        max_seqs = len(query_dict)
    blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
    blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -max_target_seqs {} -outfmt '6 qseqid sseqid sseq sstart send pident qcovs' -out {}".format(Ref_CDS,seq_file_tmp.name,str(max_seqs),blast_report_tmp.name))
    if blast_results == 0:
        try:
            blast_report_tmp.seek(0)
            Isolate_blast_dict = defaultdict(list)
            for line2 in blast_report_tmp:
                line2_list = line2.rstrip().split("\t")
                hit_seq = line2_list[2].replace('-','')
                hit_seq = line2_list[0] + '__' + hit_seq.upper()
                Isolate_blast_dict[line2_list[1]].append(hit_seq)
            blast_report_tmp.close()
            blast_parse = 'success'
            logging.info("Finished Finding ORFs in --- {:.3f} seconds ---".format(time.time() - START_TIME))
        except:
            for counter_seq_record in order_list:
                tmp_NA_lst = [counter_SEQ_INFO] + NA_list
                alleles.append(tmp_NA_lst)
            logging.critical("Could not parse blastn and will run Random Forest prediction")
        if blast_parse == 'success':
            COMP_DICT = joblib.load(COMP_DB_file)
            logging.info("Loaded comp DB in --- {:.3f} seconds ---".format(time.time() - START_TIME))
            for acc in order_list:#make sure space will not cause issues for dict keys
                allele_tmp_lst = []
                allele_tmp_lst.append(acc)
                isolate_hits_dict = defaultdict(list)
                N_list = []
                hits_list = Isolate_blast_dict[acc]
                for hit in hits_list:
                    hit_id, hit_seq2 = hit.split('__')
                    isolate_hits_dict[hit_id].append(hit_seq2)
                if ARGS.individual:
                    file_name = RESULTS_FOLDER + 'Genome' + acc.split('__',1)[0] + '.csv'
                    QUERYFILE_IND = open(file_name,'w')
                    QUERYFILE_IND.write("{}\n".format(",".join(REPORT_LIST)))
                for gene_name in Genes:
                    try:
                        longest_seq = sorted(isolate_hits_dict[gene_name], key=len, reverse=True)[0]
                        len_seq = str(len(longest_seq))
                    except:
                        longest_seq = 'Missing'
                        len_seq = '0'
                    try:
                        ids_list = COMP_DICT[longest_seq]
                        function, allele_number = ids_list[0].rsplit('_',1)
                        allele_tmp_lst.append(allele_number)
                        if ARGS.individual:
                            SEQ_INFO_fn = acc.split('__',1)[-1] + '_' + function
                            fst_date = sorted_alleles_data[ids_list[0]][0]
                            lst_date = sorted_alleles_data[ids_list[0]][-1]
                            query_sequence_details = [SEQ_INFO_fn, Classifier_version,
                            ids_list[-1],len_seq,longest_seq, '0',
                            allele_number,fst_date, lst_date]
                    except:#I can use Counter for counting N which may be faster implementation
                        Ns_count = 0
                        for Nuc in longest_seq:
                            if Nuc not in ['A','C','G','T']:
                                Ns_count += 1
                        if longest_seq == 'Missing':
                            GNU_score = 'Missing'
                            allele_number = 'Missing'
                            Ns_count = 'NA'
                        elif Ns_count > 0:
                            GNU_score = 'None'
                            allele_number = 'None'
                        else:
                            GNU_score = '0'
                            allele_number = 'Novel'
                        allele_tmp_lst.append(allele_number)
                        if ARGS.individual:
                            SEQ_INFO_fn = SEQ_INFO + '_' + gene_name
                            query_sequence_details = [SEQ_INFO_fn, Classifier_version,
                            GNU_score, len_seq, longest_seq,
                            str(Ns_count), allele_number, 'NA', 'NA']
                    if ARGS.individual:
                        QUERYFILE_IND.write("{}\n".format(
                                ",".join(query_sequence_details)))
                if ARGS.individual:
                    QUERYFILE_IND.close()
                alleles.append(allele_tmp_lst)
        logging.info("Finished Finding Alleles in --- {:.3f} seconds ---".format(time.time() - START_TIME))
    else:#could not run blastn so everything will be predicted
        for counter_seq_record in order_list:
            tmp_NA_lst = [counter_SEQ_INFO] + NA_list
            alleles.append(tmp_NA_lst)
        logging.critical("Could not run blastn and running Random Forest prediction")
else:#exact matching turned off so everything will be predicted
    for counter_seq_record in order_list:
        tmp_NA_lst = [counter_seq_record] + NA_list
        alleles.append(tmp_NA_lst)
    logging.info("Skipping exact matching and running Random Forest prediction")
#########Divergence of exact matches and prediction##########
exact_match = []
prediction_list = []
prediction_dict = {}
for index in range(0,len(alleles),1):
    try:
        results_data = []
        predict_ST = ST_allele_Dict['_'.join(alleles[index][1:])]
        ST_data = sorted_ST_data[predict_ST]
        ST_1st_date = ST_data[0][0]
        country_1st = ST_data[0][1]
        exact_CC = ST_data[0][2]
        try:
            VOC = VOC_dict[int(exact_CC)]
        except:
            VOC = 'No'
        ST_last_date = ST_data[-1][0]
        country_last = ST_data[-1][1]
        p_value = 'Exact'
        results_data = [predict_ST,country_1st,ST_1st_date,ST_last_date,country_last,exact_CC, p_value, VOC,'passed']
        if exact_CC == 'NA':
            alleles[index].extend(results_data)
            prediction_list.append(alleles[index])
            prediction_dict[alleles[index][0]] = alleles[index]
        else:
            alleles[index].extend(results_data)
            exact_match.append(alleles[index])
    except:
        prediction_list.append(alleles[index])
        prediction_dict[alleles[index][0]] = alleles[index]
results_none = 18 * ['None'] #for failed
failed_list_results = []
for i in failed_list: #failed sequences results
    None_list = [i.split(' ',1)[0]] + results_none + [i.split(' ',1)[-1]]
    failed_list_results.append(None_list)
#########block function to avoid memory overload########
def FASTA_to_seq_list(seq_file,SNP_postitions,blk_size):
    tmp_lst = []
    SEQUENCES_LIST = []
    order_list = []
    SEQUENCE_STRING = ''
    nucs = ['A','T','G','C','-']
    for line in seq_file:
        line = line.rstrip()
        if line.startswith(">"):
            if (len(SEQUENCE_STRING) > 0):
                lst = list(SEQUENCE_STRING)
                for j in SNP_postitions:
                    nuc = lst[j].upper()
                    if nuc in nucs:
                        tmp_lst.append(nuc)
                    else:
                        tmp_lst.append(refseq_lst[j])
                SEQUENCES_LIST.append(tmp_lst)
                order_list.append(SEQUENCE_INFO)
                SEQUENCE_STRING = ""
                tmp_lst = []
            SEQUENCE_INFO = line.lstrip(">")
        else:
            SEQUENCE_STRING += line
        if len(SEQUENCES_LIST) == blk_size:
            yield order_list, SEQUENCES_LIST
            order_list = []
            SEQUENCES_LIST = []
    lst = list(SEQUENCE_STRING)
    for j in SNP_postitions:
        nuc = lst[j].upper()
        if nuc in nucs:
            tmp_lst.append(nuc)
        else:
            tmp_lst.append(refseq_lst[j])
    SEQUENCES_LIST.append(tmp_lst)
    order_list.append(SEQUENCE_INFO)
    seq_file.close()
    yield order_list, SEQUENCES_LIST
########Prediction for Failed Exact Matching########
if len(prediction_list) > 0:
    aln_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
    sam_log = tempfile.NamedTemporaryFile(mode='w+')
    logging.info("Aligning to the reference")
    if  len(prediction_list) == len(order_list):
        seq_file_tmp.seek(0)
        aln_results = os.system('minimap2 -a -x asm5 {} {} 2> {} | gofasta sam toMultiAlign --reference {} > {}'.format(Ref_WG,seq_file_tmp.name,sam_log.name,Ref_WG,aln_report_tmp.name))
    else:
        seq_tmp = tempfile.NamedTemporaryFile(mode='w+')
        for index in range(0,len(prediction_list),1):
            seq_tmp.write('>'+prediction_list[index][0]+'\n'+query_dict[prediction_list[index][0]]+'\n')
        seq_tmp.seek(0)
        aln_results = os.system('minimap2 -a -x asm5 {} {} 2> {} | gofasta sam toMultiAlign --reference {} > {}'.format(Ref_WG,seq_tmp.name,sam_log.name,Ref_WG,aln_report_tmp.name))
    if aln_results == 0:
        from sklearn.ensemble import RandomForestClassifier
        START_TIME = time.time()
        logging.info(sam_log.readlines())
        sam_log.close()
        loaded_model = joblib.load(DT_model)
        logging.info("Finished opening RF model in --- {:.3f} seconds ---".format(time.time() - START_TIME))
        #try:
        aln_report_tmp.seek(0)
        nucs = ['A','T','G','C','-']
        counter = 0
        prediction_results = []
        mapped = []
        for order_lst,seq_lst in FASTA_to_seq_list(aln_report_tmp,postitions_list,pred_block):
            counter += 1
            logging.info("processing group {} of {} sequences in --- {:.3f} seconds ---".format(
                            counter,len(seq_lst),time.time() - START_TIME))
            for i in nucs:
                line = [i] * len(seq_lst[0])
                seq_lst.append(line)
            mapped.extend(order_lst)
            logging.info("Finished adding all 5 categories in --- {:.3f} seconds ---".format(time.time() - START_TIME))
            seq_array = pd.DataFrame(seq_lst, columns=features_list)
            logging.info("Finished making DataFrame in --- {:.3f} seconds ---".format(time.time() - START_TIME))
            seq_array = pd.get_dummies(seq_array, columns=features_list)
            seq_array.drop(seq_array.tail(len(nucs)).index, inplace=True)
            logging.info("Finished one-hot encoding DF in --- {:.3f} seconds ---".format(time.time() - START_TIME))
            predictions = loaded_model.predict_proba(seq_array)
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
                if int(prediction) in VOC_dict:
                    VOC = VOC_dict[int(prediction)]
                else:
                    VOC = 'No'
                if len(prediction_dict[order_lst[index]]) > 18:#capture exact ST but CCNA
                    results_data2 = prediction_dict[order_lst[index]][:-4] + [prediction,str(score),VOC,'passed (exact ST but it does not have CC so CC was predicted)']
                elif 'None' in prediction_dict[order_lst[index]] or 'NA' in prediction_dict[order_lst[index]] or 'Missing' in prediction_dict[order_lst[index]]:
                    results_data2 = prediction_dict[order_lst[index]] + ['None','NA','NA','NA','NA',prediction,str(score),VOC,'passed'] #exact_matching results
                else:
                    results_data2 = prediction_dict[order_lst[index]] + ['Novel','NA','NA','NA','NA',prediction,str(score),VOC,'passed'] #exact_matching results
                prediction_results.append(results_data2)
        logging.info("Done with aligning to the reference in --- {:.3f} seconds ---".format(time.time() - START_TIME))
        #except:
        #    logging.critical("Could not parse the alignment")
    else:
        logging.critical("Could not run minimap2/gofasta")
    unmapped = list(set(prediction_dict.keys())-set(mapped))
    if len(unmapped) > 0:
        results_none = 18 * ['None'] #failed mapping
        unmapped_results = []
        for i in unmapped:
            None_list = [i] + results_none + ['failed (mapping)']
            unmapped_results.append(None_list)
#########Convergence of exact matches, prediction and failed##########
final_results = [(int(x[0].split('__',1)[0]),x) for x in exact_match]
if len(prediction_list) > 0:
    final_results.extend([(int(x[0].split('__',1)[0]),x) for x in prediction_results])
    if len(unmapped) > 0:
        final_results.extend([(int(x[0].split('__',1)[0]),x) for x in unmapped_results])
if len(failed_list) > 0:
    final_results.extend([(int(x[0].split('__',1)[0]),x) for x in failed_list_results])

sorted_final_results = sorted(final_results, key=itemgetter(0))
#####################OutPut###################
fo = open(output_file,'w')
new_details = ['Exact ST','First country seen','First date seen','Last country seen','Last date seen','CC','probability','Variant of Concern','Quality Check']
if e_matching == 1:
    fo.write("Sequence ID,GNUVID DB Version,{},{}\n".format(','.join(Genes),','.join(new_details)))
else:
    fo.write("Sequence ID,GNUVID DB Version,{}\n".format(','.join(new_details[-4:])))
for y in sorted_final_results:
    seqId = y[1][0].split('__',1)[-1]
    y_results = y[1][1:]
    if e_matching == 1:#full report
        fo.write('{},{},{}\n'.format(seqId,Classifier_version,','.join(y_results)))
    else:#short report no alleles
        fo.write('{},{},{}\n'.format(seqId,Classifier_version,','.join(y_results[-4:])))
logging.info("Finished Run in --- {:.3f} seconds ---".format(time.time() - START_TIME0))
logging.info("Typed the query isolate/s and wrote {}".format(output_file.rsplit(OS_SEPARATOR,1)[-1]))
logging.info("""Thanks for using GNUVID v2.2, I hope you found it useful.
References:
WhatsGNU 'Moustafa AM and Planet PJ 2020, Genome Biology;21:58'.
pandas 'Reback et  al. 2020, DOI:10.5281/zenodo.3509134'.
Scikit-learn 'Pedregosa et al. 2011, JMLR; 12:2825-2830'.
BLAST+ 'Camacho et al. 2009, BMC Bioinformatics; 10:421'.
GISAID 'Shu Y. and McCauley J. 2017, EuroSurveillance; 22:13'
The reference genome MN908947 'Wu et al. 2020, Nature; 579:265–269'
eBURST 'Feil et al. 2004, Journal of Bacteriology; 186:1518'
goeBURST 'Francisco et al. 2009, BMC Bioinformatics; 10:152'
minimap2 'Li H 2018, Bioinformatics; 34:18'
gofasta 'https://github.com/cov-ert/gofasta'
PHYLOViZ 2.0 'Nascimento et al. 2017, Bioinformatics; 33:128-129'
The manual is extensive and available to read at https://github.com/ahmedmagds/GNUVID
If you have problems, please file at https://github.com/ahmedmagds/GNUVID/issues""")

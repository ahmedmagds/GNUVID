#!/usr/bin/env python3
import os
import sys
import argparse
import tempfile
import joblib
import logging
import time
import subprocess
from collections import defaultdict
from collections import Counter
PARSER = argparse.ArgumentParser(
    prog="GNUVID_update_db.py",
    description="This script will update the compressed DB and isolates csv file",)
PARSER.add_argument("-q","--quiet",help="No screen output [default OFF]",action="store_true",)
PARSER.add_argument("output_db", type=str, help="output db and tsv prefix")
PARSER.add_argument("output_folder", type=str, help="output folder name")
PARSER.add_argument("isolates_report", type=str, help="Previous GNUVID DB isolates report (.txt)")
PARSER.add_argument("Comp_DB", type=str, help="Previous GNUVID compressed DB (.joblib)")
PARSER.add_argument("country_continent", type=str, help="csv file of GISAID Acc and country continent")
PARSER.add_argument("order_list", type=str, help="order list for input folder")
PARSER.add_argument("input_folder", type=str, help="folder of individual isolates (each contain 10 genes)")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
###########results folder#########
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
try:
    os.mkdir(ARGS.output_folder)
    RESULTS_FOLDER = ARGS.output_folder + OS_SEPARATOR
except:
    PARSER.exit(status=0,message="Folder exists, Please change --output_folder\n")
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
########parse DB report########
START_TIME = time.time()
Genes = ['ORF1ab','Surface_glycoprotein','ORF3a','Envelope_protein',
'Membrane_glycoprotein','ORF6','ORF7a','ORF8','Nucleocapsid_phosphoprotein','ORF10']
ST_allele_Dict = {}#to assign STs later {'1_1_1_1_2_1_1_1_10_1':'258'}
report_object = open(ARGS.isolates_report,'r')
report_object.seek(0)
header_line = (report_object.readline().rstrip()).split('\t')
ST_index = header_line.index('ST')
ORF1ab_index = (header_line.index('ORF1ab'))
report_object.seek(0)
report_object.readline()
final_report_list = []
gene_allele = defaultdict(list)
Previous_STs = []
Previous_isolates = 0
ST_dict_counter = Counter()
for line in report_object:
    Previous_isolates += 1
    line = line.rstrip()
    line_list = line.split('\t')
    final_report_list.append('\t'.join(line_list[:-1]))
    ST_number = line_list[ST_index]
    Alleles_profile = '_'.join(line_list[ORF1ab_index:ST_index])
    ST_allele_Dict[Alleles_profile] = ST_number
    Alleles_profile_ST = Alleles_profile + '_' + ST_number
    ST_dict_counter[Alleles_profile_ST] += 1
    Gene_counter = (header_line.index('ORF1ab')) - 1
    for gene in Genes:
        Gene_counter += 1
        allele_number = int(line_list[Gene_counter])
        gene_allele[gene].append(allele_number)
    Previous_STs.append(int(ST_number))
#setting the counter to the max of previous update
Allele_counter = Counter()
for gene in Genes:
    Allele_counter[gene] = max(gene_allele[gene])
logging.info(
    "Parsed the previous database isolates report in --- {:.3f} seconds ---".format(
        time.time() - START_TIME))
#####database fna files to be compressed######
DATABASE_FILES = ARGS.input_folder
DATABASE_FILES_LIST = []
list_order_object = open(ARGS.order_list, 'r')
for line in list_order_object:
    line = line.rstrip()
    DATABASE_FILES_LIST.append(DATABASE_FILES + line)
logging.info(
    "Added the new database files to a list --- {:.3f} seconds ---".format(
        time.time() - START_TIME))
###########parsing country continent file ###########
Continent_Dict = {}
Continent_object = open(ARGS.country_continent, 'r')
for line in Continent_object:
    line = line.rstrip()
    line_cc_list = line.split(',')
    Acc_number = line_cc_list[0]
    contninet = line_cc_list[2].split('/')[0].rstrip(' ').strip(' ')
    country = line_cc_list[2].split('/')[1].rstrip(' ').strip(' ')
    Continent_Dict[Acc_number] = [country,contninet]
logging.info(
    "Parsed the country continent metadata file --- {:.3f} seconds ---".format(
        time.time() - START_TIME))
#####Add to Comp DB#####
PROTEIN_COUNTER = 0
FILE_COUNTER = 0
strain_order_list = []
SEQUENCES_loaded_DICT = joblib.load(ARGS.Comp_DB)
SEQUENCES_DICT_DB = defaultdict(list)
for ptn in SEQUENCES_loaded_DICT:
    SEQUENCES_DICT_DB[ptn].extend(SEQUENCES_loaded_DICT[ptn])
logging.info(
    "Processed the previous compressed database in --- {:.3f} seconds ---".format(
        time.time() - START_TIME))
SEQUENCES_loaded_DICT = {}
Strains_ST_dict = {}
ST_counter = max(Previous_STs)
for DATABASE_FILE in DATABASE_FILES_LIST:
    DB_SEQUENCE_STRING = ""
    DB_SEQUENCE_INFO = ""
    Strain_ST = ''
    if DATABASE_FILE.endswith(".fna"):
        DATABASEFILE_OBJECT = open(DATABASE_FILE, "r")
        DB_LINE_CHECK = DATABASEFILE_OBJECT.readline()
        if not DB_LINE_CHECK.startswith(">"):
            logging.error("{} is not in a FASTA format".format(DATABASE_FILE))
            PARSER.exit(status=0, message="Database is not in a FASTA format\n")
        strain_order_list.append(DB_LINE_CHECK.lstrip(">").rsplit('|',1)[0])
        DATABASEFILE_OBJECT.seek(0)
        try:
            for line in DATABASEFILE_OBJECT:
                line = line.rstrip()
                if line.startswith(">"):
                    PROTEIN_COUNTER += 1
                    if len(DB_SEQUENCE_STRING) > 0:
                        gene_name = DB_SEQUENCE_INFO.rsplit('|',1)[-1]
                        Ns_count = 0
                        for Nuc in DB_SEQUENCE_STRING:
                            if Nuc not in ['A','C','G','T']:
                                Ns_count += 1
                        if Ns_count > 0:
                            PARSER.exit(status=0,
                            message="{} has ambiguity (e.g. N) in {}\n".format(DATABASE_FILE,gene_name))
                        if DB_SEQUENCE_STRING not in SEQUENCES_DICT_DB.keys():
                            Allele_counter[gene_name] += 1
                            Allele_number = str(Allele_counter[gene_name]) + '_'
                            Allele_name = gene_name + '_' + str(Allele_counter[gene_name])
                            SEQUENCES_DICT_DB[DB_SEQUENCE_STRING].append(Allele_name)
                            SEQUENCES_DICT_DB[DB_SEQUENCE_STRING].append(DB_SEQUENCE_INFO)
                        else:
                            SEQUENCES_DICT_DB[DB_SEQUENCE_STRING].append(DB_SEQUENCE_INFO)
                            Allele_number = str(SEQUENCES_DICT_DB[DB_SEQUENCE_STRING][0].rsplit('_',1)[-1]) + '_'
                        Strain_ST += Allele_number
                        DB_SEQUENCE_STRING = ""
                    DB_SEQUENCE_INFO = line.lstrip(">")
                else:
                    DB_SEQUENCE_STRING += line
            #repeat process for last line
            gene_name = DB_SEQUENCE_INFO.rsplit('|',1)[-1]
            if DB_SEQUENCE_STRING.count('N') > 0:
                PARSER.exit(status=0,
                message="{} has Ns in {}\n".format(DATABASEFILE_OBJECT,gene_name))
            if DB_SEQUENCE_STRING not in SEQUENCES_DICT_DB.keys():
                Allele_counter[gene_name] += 1
                Allele_number = str(Allele_counter[gene_name]) + '_'
                Allele_name = gene_name + '_' + str(Allele_counter[gene_name])
                SEQUENCES_DICT_DB[DB_SEQUENCE_STRING].append(Allele_name)
                SEQUENCES_DICT_DB[DB_SEQUENCE_STRING].append(DB_SEQUENCE_INFO)
            else:
                SEQUENCES_DICT_DB[DB_SEQUENCE_STRING].append(DB_SEQUENCE_INFO)
                Allele_number = str(SEQUENCES_DICT_DB[DB_SEQUENCE_STRING][0].rsplit('_',1)[-1]) + '_'
            Strain_ST += Allele_number
            ###check ST for isolate
            Strain_ST = Strain_ST.rstrip('_')
            if Strain_ST not in ST_allele_Dict:
                ST_counter += 1
                ST_allele_Dict[Strain_ST] = str(ST_counter)
                ST_profile = str(ST_counter)
            else:
                ST_profile = ST_allele_Dict[Strain_ST]
            final_ST = Strain_ST + '_' + ST_profile
            Strains_ST_dict[DATABASE_FILE.rsplit(OS_SEPARATOR, 1)[-1].split("_modified.fna")[0]] = final_ST
            ST_dict_counter[final_ST] += 1 # counts for each ST
            DATABASEFILE_OBJECT.close()
            FILE_COUNTER += 1
        except:
            logging.error(
                "Cannot process the Database fna file {} provided to a compressed database".format(DATABASE_FILE)
            )
            PARSER.exit(
                status=0,
                message="Cannot process the Database fna file provided to a compressed database\n",
            )
        if FILE_COUNTER in [10,100,1000,10000,50000,100000,300000,500000,700000,1000000,1500000,2000000]:
            logging.info("processed {} files in --- {:.3f} seconds ---".format(FILE_COUNTER, time.time() - START_TIME))
if bool(SEQUENCES_DICT_DB):
    logging.info(
        "processed {} gene sequences in {} file/s to a compressed database of {} variants in --- {:.3f} seconds ---".format(
            PROTEIN_COUNTER, len(DATABASE_FILES_LIST), len(SEQUENCES_DICT_DB), time.time() - START_TIME
        )
    )
################################
logging_allele_counts = []
for gene in Genes:#adding current allele counts in the dict
    logging_allele_counts.append(gene+'\t'+str(Allele_counter[gene]))
logging.info("Alleles Counts:\n{}".format('\n'.join(logging_allele_counts)))
logging.info("GNUVID assigned {} New STs for {} isolates".format(
        (len(ST_allele_Dict)-max(Previous_STs)), len(Strains_ST_dict)))
logging.info(
    "GNUVID has now a total of {} STs for a total of {} isolates".format(
        len(ST_allele_Dict), (len(Strains_ST_dict)+Previous_isolates)))
logging.info("Top 10 STs: {}".format(ST_dict_counter.most_common(10)))
######output db repoort#######
report_name = RESULTS_FOLDER + ARGS.output_db + '_DB_isolates_ST_report.txt'
report_object = open(report_name, 'w+')
report_object.write('Isolate\tDate\tCountry\tRegion\t{}\tST\n'.format('\t'.join(Genes)))
report_object.write('\n'.join(final_report_list))
report_object.write('\n')
Phylo_name = RESULTS_FOLDER + 'PHYLOVIZ_Alleles_' + ARGS.output_db + '_ST_{}.txt'.format(str(len(ST_allele_Dict)))
Phylo_obj = open(Phylo_name,'w')
Phylo_obj.write('ST\t{}\n'.format('\t'.join(Genes)))
for i in final_report_list:
    i_lst = i.split('\t')
    Phylo_obj.write('{}\t{}\n'.format(i_lst[-1],'\t'.join(i_lst[4:-1])))
for strain in strain_order_list:
    strain_data_list = strain.rsplit('|',2)
    ST_data = Strains_ST_dict[strain_data_list[-2]].split('_')
    Country = Continent_Dict[strain_data_list[-2]][0]
    Continent = Continent_Dict[strain_data_list[-2]][1]
    Phylo_obj.write('{}\t{}\n'.format(ST_data[-1],'\t'.join(ST_data[:-1])))
    report_object.write('{}\t{}\t{}\t{}\t{}\n'.format(strain,strain_data_list[-1],
                    Country,Continent,'\t'.join(ST_data)))
logging.info(
    "Typed the {} database isolates and wrote {}".format(
        len(Strains_ST_dict),report_name.rsplit('/',1)[-1]))
report_object.close()
Phylo_obj.close()
#########Add GNU score##########
for ptn_seq in SEQUENCES_DICT_DB:
    ptn_seq_lst = SEQUENCES_DICT_DB[ptn_seq]
    try:
        old_GNU = int(ptn_seq_lst[1])
        if len(ptn_seq_lst) >2:
            new_GNU = len(ptn_seq_lst[2:])
        else:
            new_GNU = 0
        combined_GNU = old_GNU + new_GNU
    except:
        combined_GNU = len(ptn_seq_lst[1:])
    SEQUENCES_DICT_DB[ptn_seq] = [ptn_seq_lst[0],str(combined_GNU)]
logging.info(
    "Added GNU score and allele numbers to the compressed database in --- {:.3f} seconds ---".format(
        time.time() - START_TIME
    )
)
#####Save database for first time as txt file#####
###########comp joblib######
output_GNUVID_db = RESULTS_FOLDER + ARGS.output_db + '_comp_db.joblib'
joblib.dump(SEQUENCES_DICT_DB, output_GNUVID_db, compress=9)
logging.info(
    "Saved the compressed database in --- {:.3f} seconds ---".format(
        time.time() - START_TIME
    )
)
##########################

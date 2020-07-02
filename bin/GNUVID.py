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

# DATE CREATED: May 15, 2020

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
import gzip
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from statistics import mean
import time
import argparse
import logging
import tempfile
import subprocess
from shutil import rmtree as rmt

START_TIME = time.time()

PARSER = argparse.ArgumentParser(
    prog="GNUVID.py",
    description="GNUVID v1.1 utilizes the natural\
 variation in public genomes of SARS-CoV-2 to rank gene sequences based on the number of observed exact \
 matches (the GNU score) in all known genomes of SARS-CoV-2. It types the genomes based on their unique \
 gene allele sequences. It types (using a whole genome MLST) your query genome in seconds.",
)
GROUP = PARSER.add_mutually_exclusive_group()
GROUP.add_argument(
    "-m",
    "--mkdatabase",
    type=str,
    help="you have to provide path to \
a folder of multiple fna files for compression",
)
GROUP.add_argument(
    "-d",
    "--database",
    type=str,
    help="you have to provide path to your compressed database",
)
PARSER.add_argument(
    "-l",
    "--list_order",
    type=str,
    help="you have to provide path to txt file with isolates ordered by collection date",
)
PARSER.add_argument(
    "-cc",
    "--country_continent",
    type=str,
    help="you have to provide path to csv file with a country to continent assignment, csv of first three columns from GISAID acknowledgment table",
)
PARSER.add_argument(
    "-o",
    "--output_folder",
    type=str,
    help="Database output prefix to be created for \
results (default: timestamped GNUVID_results in the current directory)",
)
PARSER.add_argument(
    "--force",
    help="Force overwriting existing results folder assigned with -o (default: off)",
    action="store_true",
)
PARSER.add_argument(
    "-p",
    "--prefix",
    type=str,
    help="Prefix for output compressed database \
(default: GNUVID)",
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
    version="%(prog)s 1.1",
)
PARSER.add_argument(
    "reference",
    type=str,
    help="full path to the reference (MN908947.3_cds.fna)",
)
PARSER.add_argument(
    "query_mode",
    type=str,
    choices=['WG', 'CDS'],
    help="select a mode from 'WG' or 'CDS' for query files",
)
PARSER.add_argument(
    "query_fna", type=str, help="Query Whole Genome or CDS (for the 10 ORFs) Nucleotide FASTA file/s to analyze (.fna)"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
if bool(vars(ARGS)["country_continent"]) and not bool(vars(ARGS)["mkdatabase"]):
    PARSER.exit(status=0, message="Error: You have to use -cc with -m\n")
if bool(vars(ARGS)["prefix"]) and not bool(vars(ARGS)["mkdatabase"]):
    PARSER.exit(status=0, message="Error: You have to use -p with -m\n")
if bool(vars(ARGS)["list_order"]) and not bool(vars(ARGS)["mkdatabase"]):
    PARSER.exit(status=0, message="Error: You have to use -l with -m\n")
if bool(vars(ARGS)["database"]) and bool(vars(ARGS)["prefix"]):
    PARSER.exit(status=0, message="Error: You cannot use -p with -d\n")
OS_SEPARATOR = os.sep
#########blast check##############
try:
    GETVERSION = subprocess.Popen("blastn -version", shell=True, stdout=subprocess.PIPE).stdout
    VERSION = GETVERSION.read()
    print("Found blastn (version:{})".format(VERSION.decode().splitlines()[1]))
except:
    PARSER.exit(status=0, message="Error: blastn cannot be found\n")
#####variables######
SEQUENCES_DICT = {}
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
#####create results folder######
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
#####query fna files to be processed######
QUERY = ARGS.query_fna
QUERY_LIST = []
try:
    for file in os.listdir(QUERY):
        if file.endswith(".fna"):
            QUERY_LIST.append(QUERY + file)
    logging.info(
        "You provided folder of {} fna files as queries".format(len(QUERY_LIST))
    )
    if len(QUERY_LIST) == 0:
        logging.error("The directory did not have any query fna files")
        PARSER.exit(
            status=0,
            message="The directory did not have any query fna files\n",
        )
    query_type = 'Folder'
except:
    if QUERY.endswith(".fna"):
        QUERY_LIST.append(QUERY)
        logging.info("You provided one fna file as a query")
    else:
        logging.error(
            "You did not provide single fna file or path to directory with multiple fna files"
        )
        PARSER.exit(
            status=0,
            message="You did not provide single fna file or path to directory with multiple fna files\n",
        )
    query_type = 'File'
query_blast_file = ARGS.reference
if ARGS.query_mode == 'WG':
    if query_type == 'Folder':
        QUERY_LIST_TEMP = []
        for QUERYFILE in QUERY_LIST:
            blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
            blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sseq sstart send pident qcovs' -out {}".format(query_blast_file,QUERYFILE, blast_report_tmp.name))
            #####Blast results Parser#####
            if blast_results == 0:
                try:
                    line_counter = 0
                    blast_report_tmp.seek(0)
                    for line in blast_report_tmp:
                        line_counter += 1
                    line_counter == 10
                    CDS_file = (
                        RESULTS_FOLDER
                        + (QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1]).split(".fna")[0]
                        + "_CDS.fna"
                    )
                    CDS_file_obj = open(CDS_file,'w')
                    blast_report_tmp.seek(0)
                    for line in blast_report_tmp:
                        line_list = line.rstrip().split("\t")
                        hit_seq = line_list[1].replace('-','')
                        hit_id = ('>'+(QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1]).split(".fna")[0] + '|'
                                + line_list[0] + '\n')
                        CDS_file_obj.write(hit_id+hit_seq+'\n')
                    blast_report_tmp.close()
                    QUERY_LIST_TEMP.append(CDS_file)
                    CDS_file_obj.close()
                except:
                    logging.critical(
                        "Could not parse blastn results for {}".format(
                        QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1].split(".fna")[0]))
            else:
                logging.critical(
                    "Could not run blastn for {}".format(
                    QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1].split(".fna")[0]))
    elif query_type == 'File':
        QUERY_LIST_TEMP = []
        for QUERYFILE in QUERY_LIST:
            blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
            blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sseq sstart send pident qcovs' -out {}".format(query_blast_file,QUERYFILE, blast_report_tmp.name))
            if blast_results == 0:
                #####Blast results Parser#####
                try:
                    line_counter = 0
                    blast_report_tmp.seek(0)
                    for line in blast_report_tmp:
                        line_counter += 1
                    line_counter == 10
                    CDS_file = (
                        RESULTS_FOLDER
                        + QUERYFILE.split(".fna")[0]
                        + "_CDS.fna"
                    )
                    CDS_file_obj = open(CDS_file,'w')
                    blast_report_tmp.seek(0)
                    for line in blast_report_tmp:
                        line_list = line.rstrip().split("\t")
                        hit_seq = line_list[1].replace('-','')
                        hit_id = ('>'+QUERYFILE.split(".fna")[0] + '|'
                                + line_list[0] + '\n')
                        CDS_file_obj.write(hit_id+hit_seq+'\n')
                    blast_report_tmp.close()
                    QUERY_LIST_TEMP.append(CDS_file)
                    CDS_file_obj.close()
                except:
                    logging.critical(
                        "Could not parse blastn results for {}".format(
                        QUERYFILE.split(".fna")[0]))
            else:
                logging.critical(
                    "Could not run blastn for {}".format(
                    QUERYFILE.split(".fna")[0]))
    else:
        logging.critical("Could not implement WG mode")
    QUERY_LIST = QUERY_LIST_TEMP
#####database fna files to be compressed######
if ARGS.mkdatabase:
    DATABASE_FILES = ARGS.mkdatabase
    DATABASE_FILES_LIST = []
    try:
        for file in os.listdir(DATABASE_FILES):
            if file.endswith(".fna"):
                DATABASE_FILES_LIST.append(DATABASE_FILES + file)
        logging.info(
            "You provided folder of {} Database fna files to be processed".format(len(DATABASE_FILES_LIST))
        )
        if len(DATABASE_FILES_LIST) == 0:
            logging.error("The Database directory did not have any fna files")
            PARSER.exit(
                status=0,
                message="The Database directory did not have any fna files\n",
            )
    except:
        PARSER.exit(
            status=0,
            message="You did not provide a directory with multiple fna files to construct the compressed database\n",
            )
    if ARGS.prefix:
        DB_PREFIX = ARGS.prefix
    else:
        DB_PREFIX = 'GNUVID'
    if ARGS.list_order:
        DATABASE_FILES_LIST = []
        list_order_object = open(ARGS.list_order, 'r')
        for line in list_order_object:
            line = line.rstrip()
            DATABASE_FILES_LIST.append(DATABASE_FILES + line)
    if ARGS.country_continent:
        Continent_Dict = {}
        Continent_object = open(ARGS.country_continent, 'r')
        for line in Continent_object:
            line = line.rstrip()
            line_cc_list = line.split(',')
            Acc_number = line_cc_list[0]
            contninet = line_cc_list[2].split('/')[0].rstrip(' ').strip(' ')
            country = line_cc_list[2].split('/')[1].rstrip(' ').strip(' ')
            Continent_Dict[Acc_number] = [country,contninet]
#####Run database for first time#####
PROTEIN_COUNTER = 0
FILE_COUNTER = 0
Genes = ['ORF1ab','Surface_glycoprotein','ORF3a','Envelope_protein',
'Membrane_glycoprotein','ORF6','ORF7a','ORF8','Nucleocapsid_phosphoprotein','ORF10']
Allele_counter = Counter()
for gene in Genes:
    Allele_counter[gene] = 0
strain_order_list = []
if ARGS.mkdatabase:
    SEQUENCES_DICT_DB = defaultdict(list)
    Strains_ST_dict = {}
    ST_dict_counter = Counter()
    ST_counter = 0
    ST_Dict = {}
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
                Strain_ST = Strain_ST.rstrip('_')
                if Strain_ST not in ST_Dict:
                    ST_counter += 1
                    ST_Dict[Strain_ST] = str(ST_counter)
                    ST_profile = str(ST_counter)
                else:
                    ST_profile = ST_Dict[Strain_ST]
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
            logging.info("processed file {} in --- {:.3f} seconds ---".format(FILE_COUNTER, time.time() - START_TIME))
    if bool(SEQUENCES_DICT_DB):
        logging.info(
            "processed {} gene sequences in {} file/s to a compressed database of {} variants in --- {:.3f} seconds ---".format(
                PROTEIN_COUNTER, len(DATABASE_FILES_LIST), len(SEQUENCES_DICT_DB), time.time() - START_TIME
            )
        )
    logging_allele_counts = []
    for gene in Genes:#adding current allele counts in the dict
        #SEQUENCES_DICT_DB['Allele_counts'].append(str(Allele_counter[gene]))
        logging_allele_counts.append(gene+'\t'+str(Allele_counter[gene]))
    logging.info(
        "Alleles Counts:\n{}".format(
            '\n'.join(logging_allele_counts)))
    logging.info(
        "GNUVID assigned {} STs for {} isolates".format(
            len(ST_Dict), len(Strains_ST_dict)))
    logging.info(
        "Top 10 STs: {}".format(
            ST_dict_counter.most_common(10)))
    report_name = RESULTS_FOLDER + DB_PREFIX + '_DB_isolates_report.txt'
    report_object = open(report_name, 'w+')
    if ARGS.country_continent:
        report_object.write('Isolate\tDate\tCountry\tRegion\t{}\tST\n'.format('\t'.join(Genes)))
    else:
        report_object.write('Isolate\tDate\tCountry\t{}\tST\n'.format('\t'.join(Genes)))
    for strain in strain_order_list:
        strain_data_list = strain.rsplit('|',2)
        ST_data = Strains_ST_dict[strain_data_list[-2]].split('_')
        if ARGS.country_continent:
            Country = Continent_Dict[strain_data_list[-2]][0]
            Continent = Continent_Dict[strain_data_list[-2]][1]
            report_object.write('{}\t{}\t{}\t{}\t{}\n'.format(strain,strain_data_list[-1],
                            Country,Continent,'\t'.join(ST_data)))
        else:
            Country = strain_data_list[0].split('/')[1]
            if Country == 'env':
                Country = strain_data_list[0].split('/')[2]
            report_object.write('{}\t{}\t{}\t{}\n'.format(strain,strain_data_list[-1],
                            Country,'\t'.join(ST_data)))
    logging.info(
        "Typed the {} database isolates and wrote {}".format(
            len(Strains_ST_dict),report_name.rsplit('/',1)[-1]))
#########Add GNU score##########
    for ptn_seq in SEQUENCES_DICT_DB:
        ptn_seq_ids_list = SEQUENCES_DICT_DB[ptn_seq]
        ptn_seq_GNU_score = len(ptn_seq_ids_list) - 1
        ptn_seq_ids_list.append(str(ptn_seq_GNU_score)) #GNU score
    logging.info(
        "Added GNU score and allele numbers to the compressed database in --- {:.3f} seconds ---".format(
            time.time() - START_TIME
        )
    )
#####Save database for first time as txt file#####
    try:
        TXT_FILE_NAME = (RESULTS_FOLDER
            + DB_PREFIX
            + "_comp_db.txt"
        )
        OUTPUT_FILE_DB = open(TXT_FILE_NAME, "w")
        for record in SEQUENCES_DICT_DB:
            OUTPUT_FILE_DB.write(
                "{}\t{}\n".format(record, "._/".join(SEQUENCES_DICT_DB[record]))
            )
        OUTPUT_FILE_DB.close()
        logging.info(
            "saved database ({}) of {} alleles as txt file in --- {:.3f} seconds ---".format(
                TXT_FILE_NAME, (len(SEQUENCES_DICT_DB)), time.time() - START_TIME
            )
        )
    except:
        logging.critical(
            "cannot save compressed database as txt file, this time will be ok as the compressed dictionary will be used"
        )
####load database file#########
if ARGS.mkdatabase:
    SEQUENCES_DICT = SEQUENCES_DICT_DB
    ST_allele_Dict = ST_Dict
    logging.info(
        "As you just created a compressed database using -m, it will be used this time, next time provide the database using -d"
    )
    OUTPUT_Reps = tempfile.NamedTemporaryFile(mode='w+')
    for record in SEQUENCES_DICT:
        ORF_name_allele = SEQUENCES_DICT[record][0]
        OUTPUT_Reps.write(
            ">{}\n{}\n".format(ORF_name_allele,record))
    #knowing the ST, CC, Region and genes positions in the headerline
    report_object.seek(0)
    header_line = (report_object.readline().rstrip()).split('\t')
    ST_index = header_line.index('ST')
    Gene_counter = (header_line.index('ORF1ab')) - 1
    try:
        CC_index = header_line.index('CC')
    except:
        CC_index = 'NA'
    #knowing the regions
    try:
        Region_index = header_line.index('Region')
    except:
        Region_index = 'NA'
    if Region_index != 'NA':
        report_object.seek(0)
        report_object.readline()
        Regions = []
        Regions_final_list = [] # this list has regions in order by their prevalence in the db
        for line in report_object:
            line = line.rstrip()
            Regions.append(line.split('\t')[3])
        Regions_cnt = Counter(Regions)
        Regions_cnt2 = OrderedDict(Regions_cnt.most_common())
        for i in Regions_cnt2:
            Regions_final_list.append(i)
    #capturing dates for alleles and prepare ST dict for topgenome like feature
    Alleles_dict = {}
    Top_ST_dict = {}
    #counter = 3
    for gene in Genes:
        Gene_counter += 1
        report_object.seek(0)
        report_object.readline()
        gene_all_alleles_dict = defaultdict(list)
        gene_allele_all_STs_dict = defaultdict(list)
        gene_allele_all_STs_dict_final = {}
        for line in report_object:
            line = line.rstrip()
            line_list = line.split('\t')
            allele_date = line_list[1]
            gene_allele = line_list[Gene_counter]
            gene_allele_ST = line_list[ST_index]
            if len(allele_date) > 7: #to avoid month-year and include only full dates
                gene_all_alleles_dict[gene_allele].append(allele_date) #capture dates for alleles
            gene_allele_all_STs_dict[gene_allele].append(gene_allele_ST) #capture all STs for allele
        for record in gene_allele_all_STs_dict:
            record_list = list(set(gene_allele_all_STs_dict[record])) #make set of all STs
            gene_allele_all_STs_dict_final[record] = record_list #Reducing from isolates number to ST number
        Alleles_dict[gene] = gene_all_alleles_dict #dates for the alleles
        Top_ST_dict[gene] = gene_allele_all_STs_dict_final #Dict that predict ST for isolate with novel genes
    #capturing dates, countries, CC and regions for STs
    report_object.seek(0)
    report_object.readline()
    ST_dates_dict = defaultdict(list)
    ST_country_dict = defaultdict(list)
    if Region_index != 'NA':
        ST_Region_dict = defaultdict(list)
    if CC_index != 'NA':
        CC_ST_dict = {}
    for line in report_object:
        line = line.rstrip()
        line_list = line.split('\t')
        ST_date = line_list[1]
        ST_number = line_list[ST_index]
        ST_country = line_list[2]
        ST_dates_dict[ST_number].append(ST_date)
        ST_country_dict[ST_number].append(ST_country)
        if Region_index != 'NA':
            ST_Region_dict[ST_number].append(line_list[Region_index])
        if CC_index != 'NA':
            CC_ST_dict[ST_number] = line_list[CC_index]
    if Region_index != 'NA':
        ST_Region_dict_final = {}
        for record in ST_Region_dict:
            total_ST_isolates = len(ST_Region_dict[record])
            ST_CC_percent_str = []
            regions_cnt = Counter(ST_Region_dict[record])
            regions_cnt_ordered = OrderedDict(regions_cnt.most_common())
            for j in Regions_final_list:
                try:
                    region_percent = str("{:.2f}".format(regions_cnt_ordered[j]*100/total_ST_isolates))
                    ST_CC_percent_str.append(region_percent)
                except:
                    ST_CC_percent_str.append('0')
            #this dict has percents for all regions for each ST
            ST_Region_dict_final[record] = ST_CC_percent_str
elif ARGS.database:
    ST_allele_Dict = {} #has to be parsed if -d and not -m
    SEQUENCES_DICT = {}
    if ARGS.database.endswith(".txt.gz"):
        with gzip.open(ARGS.database,'rt') as fz:
            logging.info(
                "opened previously created compressed txt.gz database in --- {:.3f} seconds ---".format(
                    time.time() - START_TIME
                )
            )
            for line in fz:
                line = line.rstrip()
                seq, ids = line.split("\t")
                listids = ids.split("._/")
                SEQUENCES_DICT[seq] = listids
    else:
        TXT_DB_FILEOBJECT = open(ARGS.database, "r")
        logging.info(
            "opened previously created compressed txt database in --- {:.3f} seconds ---".format(
                time.time() - START_TIME
            )
        )
        for line in TXT_DB_FILEOBJECT:
            line = line.rstrip()
            seq, ids = line.split("\t")
            listids = ids.split("._/")
            SEQUENCES_DICT[seq] = listids
    if bool(SEQUENCES_DICT):
        logging.info(
            "processed compressed txt database to dictionary in --- {:.3f} seconds ---".format(
                time.time() - START_TIME
            )
        )
    if ARGS.database.endswith(".txt") or ARGS.database.endswith(".txt.gz"):
        try:
            OUTPUT_Reps = tempfile.NamedTemporaryFile(mode='w+')
            for record in SEQUENCES_DICT:
                if record != 'Allele_counts':
                    ORF_name_allele = SEQUENCES_DICT[record][0]
                    OUTPUT_Reps.write(
                        ">{}\n{}\n".format(ORF_name_allele,record))
            strains_report_file = (
                ARGS.database.split("_comp_db")[0]
                + "_DB_isolates_report.txt"
            )
            report_object = open(strains_report_file,'r')
            report_object.seek(0)
            header_line = (report_object.readline().rstrip()).split('\t')
            ST_index = header_line.index('ST')
            Gene_counter = (header_line.index('ORF1ab')) - 1
            ORF1ab_index = (header_line.index('ORF1ab'))
            try:
                CC_index = header_line.index('CC')
            except:
                CC_index = 'NA'
            #knowing the regions
            try:
                Region_index = header_line.index('Region')
            except:
                Region_index = 'NA'
            if Region_index != 'NA':
                report_object.seek(0)
                report_object.readline()
                Regions = []
                Regions_final_list = [] # this list has regions in order by their prevalence in the db
                for line in report_object:
                    line = line.rstrip()
                    Regions.append(line.split('\t')[3])
                Regions_cnt = Counter(Regions)
                Regions_cnt2 = OrderedDict(Regions_cnt.most_common())
                for i in Regions_cnt2:
                    Regions_final_list.append(i)
            #capturing dates for alleles and prepare ST dict for topgenome like feature
            Alleles_dict = {}
            Top_ST_dict = {}
            #counter = 3
            for gene in Genes:
                Gene_counter += 1
                report_object.seek(0)
                report_object.readline()
                gene_all_alleles_dict = defaultdict(list)
                gene_allele_all_STs_dict = defaultdict(list)
                gene_allele_all_STs_dict_final = {}
                #gene_allele_ST_list = []
                for line in report_object:
                    line = line.rstrip()
                    line_list = line.split('\t')
                    allele_date = line_list[1]
                    gene_allele = line_list[Gene_counter]
                    gene_allele_ST = line_list[ST_index]
                    if len(allele_date) > 7: #to avoid month-year and include only full dates
                        gene_all_alleles_dict[gene_allele].append(allele_date) #capture dates for alleles
                    gene_allele_all_STs_dict[gene_allele].append(gene_allele_ST) #capture all STs for allele
                for record in gene_allele_all_STs_dict:
                    record_list = list(set(gene_allele_all_STs_dict[record])) #make set of all STs
                    gene_allele_all_STs_dict_final[record] = record_list #Reducing from isolates number to ST number
                Alleles_dict[gene] = gene_all_alleles_dict #dates for the alleles
                Top_ST_dict[gene] = gene_allele_all_STs_dict_final #Dict that predict ST for isolate with novel genes
            #capturing dates, countries, regions for STs
            report_object.seek(0)
            report_object.readline()
            ST_dates_dict = defaultdict(list)
            ST_country_dict = defaultdict(list)
            if Region_index != 'NA':
                ST_Region_dict = defaultdict(list)
            if CC_index != 'NA':
                CC_ST_dict = {}
            for line in report_object:
                line = line.rstrip()
                line_list = line.split('\t')
                ST_date = line_list[1]
                ST_number = line_list[ST_index]
                Alleles_profile = '_'.join(line_list[ORF1ab_index:ST_index])
                ST_allele_Dict[Alleles_profile] = ST_number
                ST_country = line_list[2]
                ST_dates_dict[ST_number].append(ST_date)
                ST_country_dict[ST_number].append(ST_country)
                if Region_index != 'NA':
                    ST_Region_dict[ST_number].append(line_list[Region_index])
                if CC_index != 'NA':
                    CC_ST_dict[ST_number] = line_list[CC_index]
            if Region_index != 'NA':
                ST_Region_dict_final = {}
                for record in ST_Region_dict:
                    total_ST_isolates = len(ST_Region_dict[record])
                    ST_CC_percent_str = []
                    regions_cnt = Counter(ST_Region_dict[record])
                    regions_cnt_ordered = OrderedDict(regions_cnt.most_common())
                    for j in Regions_final_list:
                        try:
                            region_percent = str("{:.2f}".format(regions_cnt_ordered[j]*100/total_ST_isolates))
                            ST_CC_percent_str.append(region_percent)
                        except:
                            ST_CC_percent_str.append('0')
                    #this dict has percents for all regions for each ST
                    ST_Region_dict_final[record] = ST_CC_percent_str
        except:
            logging.error(
                "Cannot open the compressed database txt file or DB_isolates_report.txt you provided"
            )
            PARSER.exit(
                status=0,
                message="Cannot open the compressed database txt file or DB_isolates_report.txt you provide\n",
            )
    else:
        logging.error(
            "No proper compressed database file.txt was provided using -d"
        )
        PARSER.exit(
            status=0,
            message="No proper compressed database file.txt was provided using -d\n",
        )
else:
    logging.error(
        "Neither you created new database using -m (file.fna) nor proper database file.txt was provided using -d"
    )
    PARSER.exit(
        status=0,
        message="Neither you created new database using -m (file.fna) nor proper database file.txt was provided using -d\n",
    )

#########GNUVID###########
REPORT_LIST = ["Query Gene","GNU score","length","Gene","sequence","Ns count","Allele number",
"First date seen", "Last date seen"]
##########Query strain report###########
files_ST_report = (
    RESULTS_FOLDER
    + "Query_isolates_GNUVID_ST_Report.txt"
)
files_ST_report_obj = open(files_ST_report, "w")
files_ST_report_obj.write('Isolate\t{}\tAllele profile\tST (level of variation)\tFirst Country\tFirst date seen\tlast date seen'.format(
'\t'.join(Genes)))
if Region_index != 'NA':
    files_ST_report_obj.write('\t{}'.format('\t'.join(Regions_final_list)))
if CC_index != 'NA':
    files_ST_report_obj.write('\tCC')
files_ST_report_obj.write('\n')
###########Query files Processing##############
for QUERYFILE in QUERY_LIST:
    QUERYFILE_OBJECT = open(QUERYFILE, "r")
    line_check = QUERYFILE_OBJECT.readline()
    if not line_check.startswith(">"):
        logging.error("Not a FASTA file: {}".format(QUERYFILE))
        PARSER.exit(status=0, message="Not a FASTA file\n")
    QUERYFILE_OBJECT.seek(0)
    file_report = (
        RESULTS_FOLDER
        + (QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1]).split(".fna")[0]
        + "_GNUVID_report.txt"
    )
    output_file_report = open(file_report, "w")
    logging.info(
        "opened report file for {}".format(
            (QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1]).split(".fna")[0]
        )
    )
    #Write GNUVID report header
    output_file_report.write("{}\n".format("\t".join(REPORT_LIST)))
    processed_counter = 0
    sequence_info = ""
    sequence_string = ""
    Strain_Alleles = {}
    for line in QUERYFILE_OBJECT:
        line = line.rstrip()
        if line.startswith(">"):
            if len(sequence_string) > 0:
                processed_counter += 1
                try:
                    ids_list = SEQUENCES_DICT[sequence_string]
                    function, allele_number = ids_list[0].rsplit('_',1)
                    Strain_Alleles[function] = allele_number
                    Ns_count = 0
                    for Nuc in sequence_string:
                        if Nuc not in ['A','C','G','T']:
                            Ns_count += 1
                    fst_date = Alleles_dict[function][allele_number][0]
                    lst_date = Alleles_dict[function][allele_number][-1]
                    query_sequence_details = [sequence_info, ids_list[-1],
                                    str(len(sequence_string)),function,
                                    sequence_string, str(Ns_count), allele_number,
                                    fst_date, lst_date]
                    ##############write to report#########
                    output_file_report.write("{}\n".format(
                        "\t".join(query_sequence_details)))
                except:
                    Ns_count = 0
                    for Nuc in sequence_string:
                        if Nuc not in ['A','C','G','T']:
                            Ns_count += 1
                    blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
                    OUTPUT_FILE_Zeros = tempfile.NamedTemporaryFile(mode='w+')
                    OUTPUT_FILE_Zeros.write(
                        ">{}\n{}\n".format(sequence_info, sequence_string))
                    OUTPUT_FILE_Zeros.seek(0)
                    OUTPUT_Reps.seek(0)
                    blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sacc qseq sstart send pident qcovs' -out {}".format(OUTPUT_FILE_Zeros.name, OUTPUT_Reps.name, blast_report_tmp.name))
                    if blast_results == 0:
                        #####Blast results Parser#####
                        blast_dict = {}
                        blast_report_tmp.seek(0)
                        percent_list = []
                        allele_list = []
                        for line2 in blast_report_tmp:
                            line2_list = line2.rstrip().split("\t")
                            percent_id = float(line2_list[-2])
                            percent_list.append(percent_id)
                            allele_list.append(int(line2_list[1].rsplit('_',1)[-1]))
                            if mean(percent_list) != percent_list[0]:
                                break
                        percent_list = percent_list[:-1]
                        allele_list = allele_list[:-1]
                        blast_report_tmp.seek(0)
                        function = blast_report_tmp.readline().rstrip().split("\t")[1]
                        allele_number = 'E' + str(min(allele_list))
                        blast_report_tmp.close()
                        Strain_Alleles[function.rsplit('_',1)[0]] = allele_number
                        if Ns_count == 0:
                            query_sequence_details = [sequence_info, '0',
                            str(len(sequence_string)),function, sequence_string,
                            str(Ns_count), allele_number, 'Novel', 'Novel']
                        else:
                            query_sequence_details = [sequence_info, '0',
                            str(len(sequence_string)),function, sequence_string,
                            str(Ns_count), allele_number, 'NA', 'NA']
                    else:
                        query_sequence_details = [sequence_info, '0',
                        str(len(sequence_string)),function, sequence_string,
                        str(Ns_count), 'blast error', 'NA', 'NA']
                    output_file_report.write("{}\n".format(
                            "\t".join(query_sequence_details)))
                sequence_string = ""
            sequence_info = line.lstrip(">")
        else:
            sequence_string += line
    processed_counter += 1
    try:
        ids_list = SEQUENCES_DICT[sequence_string]
        function, allele_number = ids_list[0].rsplit('_',1)
        Strain_Alleles[function] = allele_number
        Ns_count = 0
        for Nuc in sequence_string:
            if Nuc not in ['A','C','G','T']:
                Ns_count += 1
        fst_date = Alleles_dict[function][allele_number][0]
        lst_date = Alleles_dict[function][allele_number][-1]
        query_sequence_details = [sequence_info, ids_list[-1],
                        str(len(sequence_string)),function,
                        sequence_string, str(Ns_count), allele_number,
                        fst_date, lst_date]
        ##############write to report#########
        output_file_report.write("{}\n".format(
            "\t".join(query_sequence_details)))
    except:
        Ns_count = 0
        for Nuc in sequence_string:
            if Nuc not in ['A','C','G','T']:
                Ns_count += 1
        blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
        OUTPUT_FILE_Zeros = tempfile.NamedTemporaryFile(mode='w+')
        OUTPUT_FILE_Zeros.write(
            ">{}\n{}\n".format(sequence_info, sequence_string))
        OUTPUT_FILE_Zeros.seek(0)
        OUTPUT_Reps.seek(0)
        blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sacc qseq sstart send pident qcovs' -out {}".format(OUTPUT_FILE_Zeros.name, OUTPUT_Reps.name, blast_report_tmp.name))
        if blast_results == 0:
            #####Blast results Parser#####
            blast_dict = {}
            blast_report_tmp.seek(0)
            percent_list = []
            allele_list = []
            for line2 in blast_report_tmp:
                line2_list = line2.rstrip().split("\t")
                percent_id = float(line2_list[-2])
                percent_list.append(percent_id)
                allele_list.append(int(line2_list[1].rsplit('_',1)[-1]))
                if mean(percent_list) != percent_list[0]:
                    break
            percent_list = percent_list[:-1]
            allele_list = allele_list[:-1]
            blast_report_tmp.seek(0)
            function = blast_report_tmp.readline().rstrip().split("\t")[1]
            allele_number = 'E' + str(min(allele_list))
            blast_report_tmp.close()
            Strain_Alleles[function.rsplit('_',1)[0]] = allele_number
            if Ns_count == 0:
                query_sequence_details = [sequence_info, '0',
                str(len(sequence_string)),function, sequence_string,
                str(Ns_count), allele_number, 'Novel', 'Novel']
            else:
                query_sequence_details = [sequence_info, '0',
                str(len(sequence_string)),function, sequence_string,
                str(Ns_count), allele_number, 'NA', 'NA']
        else:
            query_sequence_details = [sequence_info, '0',
            str(len(sequence_string)),function, sequence_string,
            str(Ns_count), 'blast error', 'NA', 'NA']
        output_file_report.write("{}\n".format(
                "\t".join(query_sequence_details)))
    logging.info(
        "processed {} Genes of {} in {:.3F}".format(
            processed_counter,
            (QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1]).split(".fna")[0],
            time.time() - START_TIME,
        )
    )
    #########Isolates ST report#########
    strain_name = QUERYFILE.rsplit(OS_SEPARATOR, 1)[-1].split(".fna")[0]
    alleles_list = []
    for gene in Genes:
        try:
            alleles_list.append(Strain_Alleles[gene])
        except:
            alleles_list.append('NA')
    allele_STs_list = []
    try:
        Expected_ST = ST_allele_Dict['_'.join(alleles_list)]
        date_list = ST_dates_dict[Expected_ST]
        first_country = ST_country_dict[Expected_ST][0]
        Expected = 'Exact'
        if Region_index != 'NA':
            Regions_percent_list = ST_Region_dict_final[Expected_ST]
        if CC_index != 'NA':
            Expected_CC = CC_ST_dict[Expected_ST]
    except:
        alleles_list2 = []
        for i in alleles_list:
            alleles_list2.append(i.split('E')[-1])
        try:
            Expected_ST = ST_allele_Dict['_'.join(alleles_list2)]
            date_list = ST_dates_dict[Expected_ST]
            first_country = ST_country_dict[Expected_ST][0]
            if Region_index != 'NA':
                Regions_percent_list = ST_Region_dict_final[Expected_ST]
            if CC_index != 'NA':
                Expected_CC = CC_ST_dict[Expected_ST]
        except:
            for gene, gene_allele in zip(Genes, alleles_list2):
                allele_STs_list.extend(Top_ST_dict[gene][gene_allele])
            C = Counter(allele_STs_list)
            Expected_ST, matching_variants = C.most_common(1)[0]
            if CC_index != 'NA':
                Expected_CC = CC_ST_dict[Expected_ST]
            if Expected_ST != 'NA':
                if (10 - matching_variants) == 1:
                    Expected_ST = 'Novel' + '(SLV of {})'.format(Expected_ST)
                elif (10 - matching_variants) == 2:
                    Expected_ST = 'Novel' + '(DLV of {})'.format(Expected_ST)
                else:
                    Expected_ST = 'Novel' + '(more than DLV of {})'.format(Expected_ST)
            if Region_index != 'NA':
                Regions_percent_list = len(Regions_final_list)*['NA']
            date_list = ['NA']
            first_country = 'NA'
        Expected = 'Expected'
    files_ST_report_obj.write('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
    strain_name,'\t'.join(alleles_list),Expected,Expected_ST,first_country,
    date_list[0],date_list[-1]))
    if Region_index != 'NA':
        files_ST_report_obj.write('\t{}'.format('\t'.join(Regions_percent_list)))
    if CC_index != 'NA':
        files_ST_report_obj.write('\t'+Expected_CC)
    files_ST_report_obj.write('\n')
    QUERYFILE_OBJECT.close()
logging.info("Typed the query isolate/s and wrote Query_isolates_GNUVID_ST_Report.txt")
logging.info("Done in --- {:.3f} seconds ---".format(time.time() - START_TIME))
logging.info("""Thanks for using GNUVID1.1, I hope you found it useful.
Please cite WhatsGNU 'Moustafa AM and Planet PJ 2020, Genome Biology;21:58'.
Please also cite BLAST+ 'Camacho et al. 2009, BMC Bioinformatics;10:421' if you use GNUVID.
Please also cite GISAID 'Shu Y. and McCauley J. 2017, EuroSurveillance; 22:13'
Please also cite the reference genome MN908947 'Wu et al. 2020, Nature; 579:265–269'
Please also cite eBURST 'Feil et al. 2004,  Journal of Bacteriology; 186:1518'
Please also cite goeBURST 'Francisco et al. 2009, BMC Bioinformatics; 10:152'
Please also cite PHYLOViZ 2.0 'Nascimento et al. 2017, Bioinformatics; 33:128-129'
The manual is extensive and available to read at https://github.com/ahmedmagds/GNUVID
If you have problems, please file at https://github.com/ahmedmagds/GNUVID/issues""")

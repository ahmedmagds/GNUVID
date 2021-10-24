#!/usr/bin/env python3
import os
import sys
import argparse
import tempfile
import time
import subprocess
from collections import defaultdict
PARSER = argparse.ArgumentParser(
    prog="GNUVID_preprocessor.py",
    description="This script will preprocess the GISAID fasta file and metadata file",)
PARSER.add_argument("-N","--Ns_ratio",type=float,help="Ns percentage cutoff in the sequence (default: 0.01)",)
PARSER.add_argument('-l',"--length", type=int, help="sequence length cutoff (default: 29,300 bp)",)
PARSER.add_argument('-e',"--exclusion", type=str, help="previous isolates exclusion GISAID acc list")
PARSER.add_argument('-t',"--temp_dir", type=str, help="temp dir path")
PARSER.add_argument("prev_fasta", type=str, help="previous masked fasta file")
PARSER.add_argument("output_folder", type=str, help="output folder name")
PARSER.add_argument("exc_date", type=str, help="exclusion submission date for previous isolates (e.g. 2021-01-05)")
PARSER.add_argument("metadata", type=str, help="GISAID metadata report")
PARSER.add_argument("fasta_file", type=str, help="GISAID FASTA file")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
TIMESTR = time.strftime("%Y%m%d")
#########blast check##############
try:
    GETVERSION = subprocess.Popen("blastn -version", shell=True, stdout=subprocess.PIPE).stdout
    VERSION = GETVERSION.read()
    print("Found blastn (version:{})".format(VERSION.decode().splitlines()[1]))
except:
    PARSER.exit(status=0, message="Error: blastn cannot be found\n")
####################################
try:
    os.mkdir(ARGS.output_folder)
    RESULTS_FOLDER = ARGS.output_folder + OS_SEPARATOR
except:
    PARSER.exit(
        status=0,
        message="Folder exists, Please change --output_folder\n")
meta_obj = open(ARGS.metadata,'r')
epi_obj = open('epi_no_N_{}.txt'.format(TIMESTR),'w')
next_exc_obj = open('To_exclude_next_time_{}.txt'.format(TIMESTR),'w')
metadata_included_obj = open('metadata_updated_{}.csv'.format(TIMESTR),'w')
EXC_OBJECT = open('Excluded_Sequences_{}.csv'.format(TIMESTR), 'w')
########################
if ARGS.exclusion:
    exc_obj = open(ARGS.exclusion,'r')
    exc_lst = []
    for line in exc_obj:
        exc_lst.append(line.rstrip())
    exc_set = set(exc_lst)
else:
    exc_set = set()
if ARGS.Ns_ratio:
    Ns_ratio = ARGS.Ns_ratio
else:
    Ns_ratio = 0.01
if ARGS.length:
    LENGTH_CUTOFF = ARGS.length
else:
    LENGTH_CUTOFF = 29300 #98% of 29903
exc_date = ARGS.exc_date
###################
def fix_date(s_date):
    if (len(s_date) > 7) and (s_date.split('-')[0] in ['2021','2020', '2019']):
        if len(s_date) < 10:
            s_date_lst = s_date.split('-')
            if len(s_date_lst[1]) < 2:
                new_date = '0' + s_date_lst[1]
                s_date_lst[1] = new_date
            if len(s_date_lst[2]) < 2:
                new_date2 = '0' + s_date_lst[2]
                s_date_lst[2] = new_date2
            s_date2 = '-'.join(s_date_lst)
        else:
            s_date2 = s_date
    else:
        s_date2 = s_date
    return s_date2
###################
date_counter = 0
counter = 0
other_counter = 0
acc_counter = 0
meta_counter = 0
N_lst = []
meta_obj.readline()
date_year = []
inclusion_dict = {}
for line in meta_obj:
    line_list = line.rstrip().split('\t')
    isolate = line_list[0].replace(' ','_')
    seq_loc = line_list[4]
    aa_subs = line_list[14]
    seq_date = fix_date(line_list[3])
    sub_date = fix_date(line_list[15])
    seq_len = int(line_list[6])
    acc = line_list[2]
    fasta_name = isolate + '|' + seq_date + '|' + sub_date
    fasta_new_name = isolate + '|' + acc + '|' + seq_date
    next_exc_obj.write(acc+'\n')
    try:
        N_cont = float(line_list[20])
    except:
        N_cont = 0.0
        epi_obj.write(acc+'\n')
    N_lst.append(N_cont)
    #cutoffs are length and Ns and not previously in DB and right date format
    if seq_len >= LENGTH_CUTOFF and len(seq_date) > 7 and N_cont <= Ns_ratio and acc not in exc_set and (seq_date.split('-')[0] in ['2021','2020', '2019']):
        if exc_date == sub_date:#include sequences from exclusion submission date
            counter += 1
            date_year.append(seq_date.split('-')[0])
            metadata_included_obj.write('{},{},{},{},{}\n'.format(acc,isolate,seq_loc,seq_date,aa_subs))
            inclusion_dict[fasta_name] = [fasta_new_name,seq_date]
            if acc in exc_set:
                acc_counter += 1
        elif sorted([exc_date,sub_date]).index(sub_date) == 1:#include sequences newer than exclusion date
            counter += 1
            date_year.append(seq_date.split('-')[0])
            metadata_included_obj.write('{},{},{},{},{}\n'.format(acc,isolate,seq_loc,seq_date,aa_subs))
            inclusion_dict[fasta_name] = [fasta_new_name,seq_date]
            if acc in exc_set:
                acc_counter += 1
        else:#excluded for submission date being before exclusion submission date
            date_counter += 1
            EXC_OBJECT.write(fasta_name+',subm_date before excl_subm_date\n')
            #date_obj.write(acc+','+sub_date+'\n')
    elif acc in exc_set:# I will just include it in the metadata file
        meta_counter += 1
        EXC_OBJECT.write(fasta_name+',Included in Prev_DB\n')
        metadata_included_obj.write('{},{},{},{},{}\n'.format(acc,isolate,seq_loc,seq_date,aa_subs))
    else:#excluded for any of cutoffs
        other_counter += 1
        EXC_OBJECT.write(fasta_name+',Excluded for (len_date_Ns) cutoffs\n')
print(set(date_year))
print('min N: ',min(N_lst))
print('max N: ',max(N_lst))
print('avg N: ',sum(N_lst)/len(N_lst))
print('Included: ',counter)
print('Included from previous db: ',acc_counter)
print('Metadata Included for previous acc: ',meta_counter)
print('Excluded for date: ',date_counter)
print('Excluded for cutoffs: ',other_counter)
print('Total seqs: ',len(N_lst))
metadata_included_obj.close()
epi_obj.close()
meta_obj.close()
next_exc_obj.close()
##########FASTA to work on#################
#Ref_CDS = os.path.join(DB_Folder_Path,'MN908947.3_cds.fna')
Ref_CDS = 'MN908947.3_cds.fna'
Ref_WG = 'MN908947.3.fasta'
SEQUENCES_DICT = {}
SEQUENCE_STRING = ""
SEQUENCE_INFO = ""
FASTAFILE_OBJECT = open(ARGS.fasta_file, "r")
if ARGS.temp_dir:
    fasta_op_obj = tempfile.NamedTemporaryFile(mode='w+',dir =ARGS.temp_dir)
else:
    fasta_op_obj = tempfile.NamedTemporaryFile(mode='w+')
failed_blast_ext_counter = 0
failed_blast_run_counter = 0
failed_qc_counter = 0
passed_blast_counter = 0
file_counter = 0
order_dict = defaultdict(list)
prog_lst = [10,100,500,1000,5000,10000,20000,50000,100000,150000,200000,300000,
            400000,500000,600000,700000,800000,900000,1000000,1100000,1200000,
            1300000,1400000,1500000,1600000,1700000,1800000,1900000,2000000,
            2100000,2200000,2300000,2400000,2500000,2600000,2700000,2800000,
            2900000,3000000,3100000,3200000,3300000,3400000,3500000,3600000]
START_TIME = time.time()
done_list = []
for line in FASTAFILE_OBJECT:
    line = line.rstrip()
    if line.startswith(">"):
        if len(SEQUENCE_STRING) > 0:
            file_counter += 1
            #report file progress
            if file_counter in prog_lst:
                print('{} Passed from {} in {}'.format(passed_blast_counter,
                                    file_counter,(time.time() - START_TIME)))
            #I need to do blastn and check blast report here and if passed then output
            if SEQUENCE_INFO in inclusion_dict and SEQUENCE_INFO not in done_list:#done_list to exclude duplicated records
                if len(set(SEQUENCE_STRING[300:29300])) == 4:#quick rough qc exlusion step
                    blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
                    seq_file_tmp = tempfile.NamedTemporaryFile(mode='w+')
                    seq_file_tmp.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING+'\n')
                    seq_file_tmp.seek(0)
                    blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sseq sstart send pident qcovs' -out {}".format(Ref_CDS,seq_file_tmp.name,blast_report_tmp.name))
                    line_counter = 0
                    cov_list = []
                    if blast_results == 0:
                        blast_report_tmp.seek(0)
                        concat_seq = ''
                        ids_lst = []
                        seqs_lst = []
                        for line2 in blast_report_tmp:
                            line_counter += 1
                            line2 = line2.rstrip()
                            line_list2 = line2.split('\t')
                            hit_seq = line_list2[1].replace('-','')
                            seqs_lst.append(hit_seq)
                            ids_lst.append(line_list2[0])
                            concat_seq += hit_seq
                        if line_counter == 10 and len(set(concat_seq)) == 4 and len(set(ids_lst)) == 10:
                            new_name = inclusion_dict[SEQUENCE_INFO][0]
                            acc1 = new_name.split('|')[-2] + "_modified.fna"
                            file_name_output = RESULTS_FOLDER + acc1
                            file_name_object = open(file_name_output, 'w')
                            for id1, seq1 in zip(ids_lst, seqs_lst):
                                iso_id = '>' + new_name + '|' + id1
                                file_name_object.write(iso_id+'\n'+seq1+'\n')
                            file_name_object.close()
                            #make a csv order list to cat with previous records
                            order_dict[inclusion_dict[SEQUENCE_INFO][-1]].append(acc1)
                            fasta_op_obj.write('>'+new_name+'\n'+SEQUENCE_STRING+'\n')
                            passed_blast_counter += 1
                            done_list.append(SEQUENCE_INFO)
                        else:
                            EXC_OBJECT.write(SEQUENCE_INFO+',failed blast extraction step\n')
                            #excluded as not all genes there or ambiguity in hits or multiple hits/gene
                            failed_blast_ext_counter += 1
                    else:
                        EXC_OBJECT.write(SEQUENCE_INFO+',failed blast running step\n')
                        failed_blast_run_counter += 1
                        #blast failed
                    blast_report_tmp.close()
                    seq_file_tmp.close()
                else:
                    EXC_OBJECT.write(SEQUENCE_INFO+',failed ambiguity QC\n')
                    failed_qc_counter += 1
                    #excluded for qc 500:29000
            SEQUENCE_STRING = ""
        SEQUENCE_INFO = line.lstrip(">").replace(' ','_')
    else:
        SEQUENCE_STRING += line
#repeat for last record
file_counter += 1
#report file progress
if file_counter in prog_lst:
    print('{} Passed from {} in {}'.format(passed_blast_counter,
                        file_counter,(time.time() - START_TIME)))
#I need to do blastn and check blast report here and if passed then output
if SEQUENCE_INFO in inclusion_dict and SEQUENCE_INFO not in done_list:
    if len(set(SEQUENCE_STRING[300:29300])) == 4:#quick rough qc exlusion step
        blast_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
        seq_file_tmp = tempfile.NamedTemporaryFile(mode='w+')
        seq_file_tmp.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING+'\n')
        seq_file_tmp.seek(0)
        blast_results = os.system("blastn -task blastn -query {} -subject {} -evalue 0.000001 -outfmt '6 qseqid sseq sstart send pident qcovs' -out {}".format(Ref_CDS,seq_file_tmp.name,blast_report_tmp.name))
        line_counter = 0
        cov_list = []
        if blast_results == 0:
            blast_report_tmp.seek(0)
            concat_seq = ''
            ids_lst = []
            seqs_lst = []
            for line2 in blast_report_tmp:
                line_counter += 1
                line2 = line2.rstrip()
                line_list2 = line2.split('\t')
                hit_seq = line_list2[1].replace('-','')
                seqs_lst.append(hit_seq)
                ids_lst.append(line_list2[0])
                concat_seq += hit_seq
            if line_counter == 10 and len(set(concat_seq)) == 4 and len(set(ids_lst)) == 10:
                new_name = inclusion_dict[SEQUENCE_INFO][0]
                acc1 = new_name.split('|')[-2] + "_modified.fna"
                file_name_output = RESULTS_FOLDER + acc1
                file_name_object = open(file_name_output, 'w')
                for id1, seq1 in zip(ids_lst, seqs_lst):
                    iso_id = '>' + new_name + '|' + id1
                    file_name_object.write(iso_id+'\n'+seq1+'\n')
                file_name_object.close()
                #make a csv order list to cat with previous records
                order_dict[inclusion_dict[SEQUENCE_INFO][-1]].append(acc1)
                fasta_op_obj.write('>'+new_name+'\n'+SEQUENCE_STRING+'\n')
                passed_blast_counter += 1
                done_list.append(SEQUENCE_INFO)
            else:
                EXC_OBJECT.write(SEQUENCE_INFO+',failed blast extraction step\n')
                #excluded as not all genes there or ambiguity in hits or multiple hits/gene
                failed_blast_ext_counter += 1
        else:
            EXC_OBJECT.write(SEQUENCE_INFO+',failed blast running step\n')
            failed_blast_run_counter += 1
            #blast failed
        blast_report_tmp.close()
        seq_file_tmp.close()
    else:
        EXC_OBJECT.write(SEQUENCE_INFO+',failed ambiguity QC\n')
        failed_qc_counter += 1
        #excluded for qc 300:29300
FASTAFILE_OBJECT.close()
fasta_op_obj.seek(0)
print('Passed Blast: ',passed_blast_counter)
print('Failed Blast extraction: ',failed_blast_ext_counter)
print('Failed Blast run: ',failed_blast_run_counter)
print('Failed pre-blast Amibguity QC: ',failed_qc_counter)
#################################################
sorted_dates = sorted(list(order_dict.keys()))
Order_OBJECT = open('Files_Order_list_{}.txt'.format(TIMESTR), "w")
for s_seq_date in sorted_dates:
    Order_OBJECT.write('\n'.join(order_dict[s_seq_date])+'\n')
Order_OBJECT.close()
################minimap2####################
if ARGS.temp_dir:
    aln_report_tmp = tempfile.NamedTemporaryFile(mode='w+',dir =ARGS.temp_dir)
else:
    aln_report_tmp = tempfile.NamedTemporaryFile(mode='w+')
aln_results = os.system('minimap2 -a -x asm5 {} {} 2> minimap2.log | gofasta sam toMultiAlign --reference {} > {}'.format(Ref_WG,fasta_op_obj.name,Ref_WG,aln_report_tmp.name))
aln_report_tmp.seek(0)
fasta_op_obj.close()

###########mask regions#####################
def mask_regions(seq_string,pos_lst,genes_pos_lst,reference_genome):
    seq_str_lst = list(seq_string)
    for i in pos_lst:
        seq_str_lst[i] = 'N'
    for j in genes_pos_lst:
        if seq_str_lst[j] not in ['A','G','T','C','-']:
            seq_str_lst[j] = reference_genome[j]
    new_seq_string = ''.join(seq_str_lst)
    return new_seq_string

####masking the starts and ends
#1..240 and 29675..29903 which means 0..239 and 29674..29902 include C241T
#1..265 and 29675..29903 which means 0..264 and 29674..29902 exlude untranslated
#1..265 (265)
#266..21555 21563..25384 (21556-21562: 21555-21562)
#21563..25384 25393..26220 (25385-25392: 25384-25392)
#25393..26220 26245..26472 (26221-26244: 26220-26244)
#26245..26472 26523..27191 (26473-26522: 26472-26522)
#26523..27191 27202..27387 (27192-27201: 27191-27201)
#27202..27387 27394..27759 (27388-27393: 27387-27393)
#27394..27759 27894..28259 (27760-27893: 27759-27893)
#27894..28259 28274..29533 (28260-28273: 28259-28273)
#28274..29533 29558..29674 (29534-29557: 29533-29557)
#29675..29903 (29675..29903: 29674-29903)
positions_list = list(range(265))
positions_list.extend(list(range(21555,21562,1)))
positions_list.extend(list(range(25384,25392,1)))
positions_list.extend(list(range(26220,26244,1)))
positions_list.extend(list(range(26472,26522,1)))
positions_list.extend(list(range(27191,27201,1)))
positions_list.extend(list(range(27387,27393,1)))
positions_list.extend(list(range(27759,27893,1)))
positions_list.extend(list(range(28259,28273,1)))
positions_list.extend(list(range(29533,29557,1)))
positions_list.extend(list(range(29674,29903,1)))

genes_position_list = list(range(265,21555,1))
genes_position_list.extend(list(range(21562,25384,1)))
genes_position_list.extend(list(range(25392,26220,1)))
genes_position_list.extend(list(range(26244,26472,1)))
genes_position_list.extend(list(range(26522,27191,1)))
genes_position_list.extend(list(range(27201,27387,1)))
genes_position_list.extend(list(range(27393,27759,1)))
genes_position_list.extend(list(range(27893,28259,1)))
genes_position_list.extend(list(range(28273,29533,1)))
genes_position_list.extend(list(range(29557,29674,1)))

ref_obj = open(Ref_WG,'r')
ref_obj.readline()
seq_str = ''
for line in ref_obj:
    line = line.rstrip()
    seq_str += line
ref_seq = list(seq_str)
ref_obj.close()
final_dict = {}

#masked_file = ARGS.output_fasta.split('fna')[0] + '_masked.fna'
#masked_OBJECT = open(masked_file,'w')
prev_fasta_obj = open(ARGS.prev_fasta,'a')#make sure previous ends with new line
SEQUENCE_STRING = ""
for line in aln_report_tmp:
    line = line.rstrip()
    if line.startswith(">"):
        if len(SEQUENCE_STRING) > 0:
            NEW_SEQUENCE_STRING = mask_regions(SEQUENCE_STRING,positions_list,genes_position_list,ref_seq)
            prev_fasta_obj.write('>'+SEQUENCE_INFO+'\n'+NEW_SEQUENCE_STRING+'\n')
            SEQUENCE_STRING = ""
        SEQUENCE_INFO = line.lstrip(">")
    else:
        SEQUENCE_STRING += line
NEW_SEQUENCE_STRING = mask_regions(SEQUENCE_STRING,positions_list,genes_position_list,ref_seq)
prev_fasta_obj.write('>'+SEQUENCE_INFO+'\n'+NEW_SEQUENCE_STRING+'\n')
aln_report_tmp.close()
prev_fasta_obj.close()
#################################

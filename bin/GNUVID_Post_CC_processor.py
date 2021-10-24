#!/usr/bin/env python3
import os
import sys
import argparse
import time
from collections import defaultdict
from collections import Counter
PARSER = argparse.ArgumentParser(
    prog="GNUVID_Post_CC_processor.py",
    description="This script will assign CC after Phyloviz and modify names in fasta file",)
PARSER.add_argument("-l","--level", type=int, help="level of locus variant to assign CC (e.g. SLV, DLV) [Default: 2]")
PARSER.add_argument("-n","--number_connections", type=int, help="number of connections to assign CC [Default: 20]")
PARSER.add_argument("output_path", type=str, help="output path folder for aln")
PARSER.add_argument("eBURST_MST_report", type=str, help="eBURST MST txt report")
PARSER.add_argument("ST_GNUVID_report", type=str, help="ST GNUVID csv report")
PARSER.add_argument("fasta_aln", type=str, help="path to Multifasta.fna name")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
##########################
eBURST_obj = open(ARGS.eBURST_MST_report, 'r')
GNUVID_obj = open(ARGS.ST_GNUVID_report, 'r')
output_name = ARGS.ST_GNUVID_report.split('.txt')[0] + '_CC_assigned.txt'
output_obj = open(output_name, 'w')
eBURST_Dict = defaultdict(list)
if ARGS.level:
    assigned_level = ARGS.level
else:
    assigned_level = 2
if ARGS.number_connections:
    assigned_connections = ARGS.number_connections
else:
    assigned_connections = 20

############################
for line in eBURST_obj:
    if '(level:' in line:
        line = line.rstrip()
        level_value = int(line.split('(level: ')[1].split(')')[0])
        if level_value <= assigned_level:
            CC, ST_level = line.split(' -- ')
            ST = ST_level.split(' (')[0]
            eBURST_Dict[ST].append(CC)
            eBURST_Dict[CC].append(ST)
print(len(eBURST_Dict)) #total Connections
##########make dict of levels##########
eBURST_obj.seek(0)
Level_Dict = {}
for line in eBURST_obj:
    if '(level:' in line:
        line = line.rstrip()
        level_value = int(line.split('(level: ')[1].split(')')[0])
        CC, ST_level = line.split(' -- ')
        ST = ST_level.split(' (')[0]
        key1 = CC  + '_' + ST ## using key1 and 2 to search easier later.
        key2 = ST + '_' + CC
        Level_Dict[key1] = level_value
        Level_Dict[key2] = level_value
############################
ST_founders = []
ST_founders_length = []
for record in eBURST_Dict:
    if len(eBURST_Dict[record]) >= assigned_connections:
        ST_founders.append(record)

output_dict  = {}
#removing founders from each other if they overlap like old 945 and 277
for record in ST_founders:
    record_list = eBURST_Dict[record]
    for i in ST_founders:
        if i in record_list:
            record_list.remove(i)
    output_dict[record] = record ## adding CC for the ST itself i.e. CC277 for ST277
    for j in eBURST_Dict[record]: ##making a  dictionary of {ST:CC}
        if j not in output_dict:
            output_dict[j] = record
        else:
            output_dict[j] = 'NA'
##################################
header_string = GNUVID_obj.readline().rstrip()+'\tCC\n'
output_obj.write(header_string)
counter = 0
unassigned_STs = set()
for line in GNUVID_obj:
    line = line.rstrip()
    line_list = line.split('\t')
    Strain_ST = line_list[-1]
    try:
        CC = output_dict[Strain_ST]
        if CC == 'NA':
            counter += 1
            unassigned_STs.add(line_list[-1])
        output_obj.write(line+'\t'+CC+'\n')
    except:
        try:
            CC = output_dict[eBURST_Dict[Strain_ST][0]]
            parent_ST = eBURST_Dict[Strain_ST][0]
            CC_parent_ST = CC + '_' + parent_ST
            Strain_ST_parent_ST = Strain_ST + '_' + parent_ST
            total_levels = Level_Dict[CC_parent_ST] + Level_Dict[Strain_ST_parent_ST]
            if total_levels <= assigned_level:
                output_obj.write(line+'\t'+CC+'\n')
            else:
                counter += 1
                output_obj.write(line+'\tNA\n')
                unassigned_STs.add(line_list[-1])
        except:
            counter += 1
            output_obj.write(line+'\tNA\n')
            unassigned_STs.add(line_list[-1])
print('ST_founders',len(ST_founders))
print(len(output_dict))
print(len(set(output_dict.values())))
print(counter)
print('unassigned_STs',len(unassigned_STs))
print('done CC assignment')
output_obj.close()
##########deidentification########
output_obj = open(output_name, 'r')
Output_GNUVID = output_name.rsplit('.txt')[0] + '_deidentified.txt'
Output_GNUVID_obj = open(Output_GNUVID, 'w')
header_string = output_obj.readline().rstrip() + '\tST_CC_name\n'
Output_GNUVID_obj.write(header_string)
ST_dict = Counter()
CC_dict = {}
CC_list = []
for line in output_obj:
    line = line.rstrip()
    line_list = line.split('\t')
    Strain_ST = line_list[-2]
    ST_dict[Strain_ST] += 1
    Strain_CC = line_list[-1]
    if Strain_CC != 'NA':
        CC_list.append(Strain_CC)
    Strain_acc = line_list[0].split('|')[-2]
    ST_name_rank = 'ST' + Strain_ST + '_' + str(ST_dict[Strain_ST])
    Strain_new_name = ST_name_rank + '_CC' + Strain_CC
    Output_GNUVID_obj.write(line+'\t'+Strain_new_name+'\n')
    CC_dict[Strain_acc] = Strain_new_name
    CC_dict[ST_name_rank] = Strain_new_name
Output_GNUVID_obj.close()
print('done with deidentification')
output_obj.close()
print('Number of CCs: ',len(Counter(CC_list)))
###########multifasta aln##############
in_fasta_aln_obj = open(ARGS.fasta_aln, 'r')
output_fasta_aln = ARGS.output_path + ARGS.fasta_aln.rsplit('.fna')[0] + '_checked.fna'
output_fasta_aln_obj = open(output_fasta_aln, 'w')
unmatched_ids = []
unmatched_CCs = []
in_fasta_aln_obj.seek(0)
START_TIME = time.time()
SEQUENCES_DICT = {}
SEQUENCE_STRING = ""
for line in in_fasta_aln_obj:
    if line.startswith(">"):
        if len(SEQUENCE_STRING) > 0:
            if 'EPI_ISL_' in SEQUENCE_INFO:
                new_name = CC_dict[SEQUENCE_INFO.split('|')[-2]]
            else:
                new_name = CC_dict[SEQUENCE_INFO.split('_CC')[0]]
            CC_name = SEQUENCE_INFO.split('_CC')[-1]
            if SEQUENCE_INFO != new_name:
                unmatched_ids.append(SEQUENCE_INFO)
                if 'EPI_ISL_' not in CC_name:
                    unmatched_CCs.append(CC_name)
                output_fasta_aln_obj.write('>'+new_name+'\n'+SEQUENCE_STRING)
            else:
                output_fasta_aln_obj.write('>'+new_name+'\n'+SEQUENCE_STRING)
            SEQUENCE_STRING = ""
        SEQUENCE_INFO = line.lstrip(">").rstrip()
    else:
        SEQUENCE_STRING += line
if 'EPI_ISL_' in SEQUENCE_INFO:
    new_name = CC_dict[SEQUENCE_INFO.split('|')[-2]]
else:
    new_name = CC_dict[SEQUENCE_INFO.split('_CC')[0]]
CC_name = SEQUENCE_INFO.split('_CC')[-1]
if SEQUENCE_INFO != new_name:#number of mismatched isolates names
    unmatched_ids.append(SEQUENCE_INFO)
    if 'EPI_ISL_' not in CC_name:#number of CCs that had mismatches
        unmatched_CCs.append(CC_name)
    output_fasta_aln_obj.write('>'+new_name+'\n'+SEQUENCE_STRING)
else:
    output_fasta_aln_obj.write('>'+new_name+'\n'+SEQUENCE_STRING)
in_fasta_aln_obj.close()
print(time.time() - START_TIME)
print('1st & last record: ',unmatched_ids[0],unmatched_ids[-1])
print('unmatched_ids: ',len(unmatched_ids))
print('unmatched_CCs: ', len(Counter(unmatched_CCs)))
output_fasta_aln_obj.close()
##############################
"""
snp-sites -v -o Multifasta_159515_chked_mmap_aln_masked.vcf Multifasta_159515_chked_mmap_aln_masked.fna
snp-sites -o Multifasta_159515_chked_mmap_aln_masked.aln Multifasta_159515_chked_mmap_aln_masked.fna
GNUVID_Training.py 0.3 Multifasta_159515_chked_mmap_aln_masked.aln Multifasta_159515_chked_mmap_aln_masked.vcf
./GNUVID_Predict_NAs_DB.py Multifasta_159515_aligned_masked_checked.fna
./GNUVID_name_changer_to_ST_CC.py GNUVID_updated_P1_01062021/GNUVID_P1_01062021_comp_db.txt Multifasta_159515_aligned.fna GNUVID_01062021_P1_DB_isolates_report_CC_assigned.txt
"""
##############################
snp_vcf = os.system('snp-sites -v -o {}.vcf {}'.format(output_fasta_aln.split('.')[0],output_fasta_aln))
snp_aln = os.system('snp-sites -o {}.aln {}'.format(output_fasta_aln.split('.')[0],output_fasta_aln))
#if snp_aln == 0 and snp_vcf == 0:
#    gnuvid = os.system('GNUVID_Training.py 0.3 {}.aln {}.vcf'.format(output_fasta_aln.split('.')[0],output_fasta_aln.split('.')[0]))
#else:
#    print('snp-sites failed')

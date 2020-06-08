#!/usr/bin/env python3
import os
import sys
import argparse
from collections import defaultdict
PARSER = argparse.ArgumentParser(
    prog="clonal_complex_assigner.py",
    description="clonal complex assigner",
)
PARSER.add_argument(
    "-l",
    "--level", type=int, help="level of locus variant to assign CC (e.g. SLV, DLV) [Default: 2]"
)
PARSER.add_argument(
    "-n",
    "--number_connections", type=int, help="number of connections to assign CC [Default: 20]"
)
PARSER.add_argument(
    "-r",
    "--resolve", type=str,
    help="provide csv file of 3 columns, 1)conflict (Assign_CC or Founder)\
    2)ST 3)CC"
)
PARSER.add_argument(
    "output", type=str, help="output name"
)
PARSER.add_argument(
    "eBURST_MST_report", type=str, help="eBURST MST csv report"
)
PARSER.add_argument(
    "ST_GNUVID_report", type=str, help="ST GNUVID csv report"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
##########################
eBURST_obj = open(ARGS.eBURST_MST_report, 'r')
GNUVID_obj = open(ARGS.ST_GNUVID_report, 'r')
output_obj = open(ARGS.output, 'w')
eBURST_Dict = defaultdict(list)
if ARGS.level:
    assigned_level = ARGS.level
else:
    assigned_level = 2
if ARGS.number_connections:
    assigned_connections = ARGS.number_connections
else:
    assigned_connections = 20
if ARGS.resolve:
    Resolve_Founders = {}
    Resolve_CC = {}
    resolve_obj = open(ARGS.resolve, 'r')
    for line in resolve_obj:
        line = line.rstrip()
        resolve_list = line.split(',')
        if str(resolve_list[0]) == 'Assign_CC':
            Resolve_CC[str(resolve_list[1])] = str(resolve_list[2])
        elif resolve_list[0] == 'Founder':
            Resolve_Founders[str(resolve_list[1])] = str(resolve_list[2])

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
            print('conflict Assignment of ST{} to CC{} as previously assigned to CC{}'.format(j, record, output_dict[j]))
if ARGS.resolve:
    for record in Resolve_CC:
        output_dict[record] = Resolve_CC[record]
        print('conflict resolved for ST{} assigned to CC{}'.format(record, Resolve_CC[record]))
print(len(output_dict))
print(ST_founders)
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


print(len(ST_founders))
print(len(output_dict))
print(len(set(output_dict.values())))
print(set(output_dict.values()))
print(counter)
print(len(unassigned_STs))

#!/usr/bin/env python3
# PROGRAM: GNUVID is a Python3 program that ranks protein sequences in a genome
# fna file generated from annotation programs based on the number of observed
# exact protein matches in a public or private database.

# Copyright (C) 2019 Ahmed M. Moustafa

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

import sys
import os
import argparse
import gzip
from collections import Counter
from collections import OrderedDict

PARSER = argparse.ArgumentParser(
    prog="GNUVID_database_customizer.py", description="Database_customizer script for GNUVID v1.3.",)
GROUP = PARSER.add_mutually_exclusive_group()
GROUP.add_argument("-g", "--GenBank_RefSeq", help="fna files from GenBank or RefSeq", action="store_true",)
GROUP.add_argument("-p", "--prokka", help="fna files from prokka", action="store_true",)
PARSER.add_argument("-l", "--list_csv", type=str, help="a file.csv of 3+ columns: file_name, old locustag, new locustag and optionally metadata",)
PARSER.add_argument("-i", "--individual_files", help="individual modified files", action="store_true",)
PARSER.add_argument("prefix_name", type=str, help="prefix name for the output folder and the one concatenated modified file")
PARSER.add_argument("directory_path", type=str, help="path to directory of fna, RAST txt or gff files")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
#########process files in a directory to a list########
DIRECTORY_PATH = ARGS.directory_path
FILES_LIST = []
for file in os.listdir(DIRECTORY_PATH):
    if file.endswith(".fna"):
        FILES_LIST.append(DIRECTORY_PATH + file)
print("You provided folder of {} fna files to be processed".format(len(FILES_LIST)))
######################process_csv######################
#CNT = Counter()
order_list = []
if ARGS.list_csv:
    FILE_NAME_DICT = {}
    CSV_FILE_OBJECT = open(ARGS.list_csv, 'r')
    for line in CSV_FILE_OBJECT:
        locustags_list = []
        line = line.rstrip()
        csv_line_list = line.split(',')
        if len(csv_line_list) < 3:
            PARSER.exit(status=0, message="Error: number of columns less than 3\n")
        if '' in csv_line_list:
            PARSER.exit(status=0, message="Error: empty cell detected in the csv file, use NA instead\n")
        if len(csv_line_list) == 3:
            strain_name_separator = csv_line_list[2]
        else:
            strain_name_separator = '_'.join(csv_line_list[2:]) + '_'
        strain_name_separator = strain_name_separator + '|'
        #strain_name_separator = strain_name_separator
        #print(csv_line_list[2].split('hCoV-19/'))
        order_list.append(DIRECTORY_PATH + csv_line_list[0])
        #Country = csv_line_list[2].split('hCoV-19/')[1].split('/')[0]
        #CNT[Country] += 1
        locustags_list.append(csv_line_list[1])
        locustags_list.append(strain_name_separator)
        FILE_NAME_DICT[csv_line_list[0]] = locustags_list
    #ORDERED_CNT = OrderedDict(CNT.most_common())
####################OUTPUT_FILE_NAME##################
FOLDER_PATH = os.path.abspath(DIRECTORY_PATH).rsplit(OS_SEPARATOR, 1)[0] + OS_SEPARATOR
FILE_EXTENSION = '.fna'
OUTPUT_FOLDER = FOLDER_PATH + ARGS.prefix_name + OS_SEPARATOR
try:
    os.mkdir(OUTPUT_FOLDER)
except:
    PARSER.exit(status=0, message="Error: Folder exists, choose another prefix_name\n")
'''if ARGS.list_csv:
    if bool(ORDERED_CNT):
        METADATA_FILE_NAME = OUTPUT_FOLDER + 'metadata_frequency.csv'
        METADATA_FILE_OBJECT = open(METADATA_FILE_NAME, 'w')
        for i in ORDERED_CNT:
            METADATA_FILE_OBJECT.write(i+','+str(ORDERED_CNT[i])+'\n')
        METADATA_FILE_OBJECT.close()'''
#######################main########################
for file_name in order_list:
    file_object = open(file_name, 'r')
    file_name_stripped = file_name.rsplit(OS_SEPARATOR, 1)[-1]
    if " " in file_name_stripped:
        file_name_stripped = file_name_stripped.replace(' ', '_')
    if "|" in file_name_stripped:
        file_name_stripped = file_name_stripped.replace('|', '_')
    if ARGS.individual_files:
        file_name_modified = OUTPUT_FOLDER + file_name_stripped.rsplit(".", 1)[0] + "_modified.fna"
        individual_file_object = open(file_name_modified, 'w')
    if ARGS.GenBank_RefSeq:
        filedata = file_object.read()
        if ARGS.list_csv:
            strain_name_carrot_separator = '>' + FILE_NAME_DICT[file_name_stripped][1]
            filedata = filedata.replace(">", strain_name_carrot_separator)
            if ARGS.individual_files:
                individual_file_object.write(filedata)
        else:
            strain_name_carrot_separator = '>'+file_name_stripped.split(".fna")[0]+'|'
            filedata = filedata.replace(">", strain_name_carrot_separator)
            if ARGS.individual_files:
                individual_file_object.write(filedata)
    elif ARGS.prokka:
        filedata = file_object.read()
        if ARGS.list_csv:
            old_locustag = '>' + FILE_NAME_DICT[file_name_stripped][0] + '_'
            #old_locustag = '>' + FILE_NAME_DICT[file_name_stripped][0]
            new_locustag = '>' + FILE_NAME_DICT[file_name_stripped][1]
            filedata = filedata.replace(old_locustag, new_locustag)
            if ARGS.individual_files:
                individual_file_object.write(filedata)
        else:
            original_strain_name = '>' + file_name_stripped.split(".fna")[0]
            original_strain_name_separator = original_strain_name + '_'
            strain_name_carrot_separator = original_strain_name + '|'
            filedata = filedata.replace(original_strain_name_separator, strain_name_carrot_separator)
            if ARGS.individual_files:
                individual_file_object.write(filedata)
    else:
        print("You have to use one of the two options -g or -p")
    if ARGS.individual_files:
        individual_file_object.close()

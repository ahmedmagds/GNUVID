#!/usr/bin/env python3
# PROGRAM: GNUVID_FASTA_divider is a Python3 program that will take
#concatenated FASTA file and make individual FASTA files
#Quality check will be done and report will be given

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


import os
import sys
from collections import defaultdict
import time
import argparse

START_TIME = time.time()

PARSER = argparse.ArgumentParser(
    prog="GNUVID_FASTA_divider.py",
    description="FASTA Divider",
)
PARSER.add_argument(
    "-l",
    "--length",
    type=int,
    help="sequence length cutoff (default: 29,000 bp)",
)
PARSER.add_argument(
    "-N",
    "--Ns_percent",
    type=float,
    help="Ns percentage cutoff in the sequence (default: 1.0%)",
)
PARSER.add_argument(
    "output_folder", type=str, help="output folder name & quality report prefix"
)
PARSER.add_argument(
    "fasta_file", type=str, help="concatenated fasta file"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
#####variables######
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
OS_SEPARATOR = os.sep
if ARGS.length:
    LENGTH_CUTOFF = ARGS.length
else:
    LENGTH_CUTOFF = 29000
if ARGS.Ns_percent:
    Ns_CUTOFF = ARGS.Ns_percent
else:
    Ns_CUTOFF = 1.0
os.mkdir(ARGS.output_folder)
RESULTS_FOLDER = ARGS.output_folder + OS_SEPARATOR
report_file = RESULTS_FOLDER + ARGS.output_folder + "_quality_report.txt"
report_file_object = open(report_file, 'w')
####################
SEQUENCES_DICT = {}
SEQUENCE_STRING = ""
SEQUENCE_INFO = ""
FASTAFILE_OBJECT = open(ARGS.fasta_file, "r")
LINE_CHECK = FASTAFILE_OBJECT.readline()
if not LINE_CHECK.startswith(">"):
    logging.error("{} is not in a FASTA format".format(DATABASE_FILE))
    PARSER.exit(status=0, message="Database is not in a FASTA format\n")
FASTAFILE_OBJECT.seek(0)
for line in FASTAFILE_OBJECT:
    line = line.rstrip()
    if line.startswith(">"):
        if len(SEQUENCE_STRING) > 0:
            SEQUENCES_DICT[SEQUENCE_INFO] = SEQUENCE_STRING
            SEQUENCE_STRING = ""
        SEQUENCE_INFO = line.lstrip(">")
    else:
        SEQUENCE_STRING += line
SEQUENCES_DICT[SEQUENCE_INFO] = SEQUENCE_STRING
FASTAFILE_OBJECT.close()
#############################
report_file_object.write('Strain\tAccession\tCountry\tDate\tLength\t%Ns\tQuality\n')
for record in SEQUENCES_DICT:
    accession_number,strain_date = record.rsplit("|",2)[-2:]
    Seq_string = SEQUENCES_DICT[record]
    Seq_len = len(Seq_string)
    Ns_percent = "{:.2f}".format(Seq_string.count("N")*100/Seq_len)
    Country = record.split("/")[1].split('/',0)[0]
    file_name = RESULTS_FOLDER + accession_number + ".fna"
    if (Seq_len >= LENGTH_CUTOFF) and (float(Ns_percent) <= Ns_CUTOFF):
        file_name_object = open(file_name, 'w')
        file_name_object.write('>'+accession_number+'\n'+Seq_string+'\n')
        file_name_object.close()
        report_file_object.write('{}\t{}\t{}\t{}\t{}\t{}\tPassed\n'.format(
                record,accession_number,Country,strain_date,Seq_len,Ns_percent))
    else:
        report_file_object.write('{}\t{}\t{}\t{}\t{}\t{}\tFailed\n'.format(
                record,accession_number,Country,strain_date,Seq_len,Ns_percent))
report_file_object.close()

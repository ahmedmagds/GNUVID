#!/usr/bin/env python3
import os
import sys
import argparse
PARSER = argparse.ArgumentParser(
    prog="Extract_fasta_sequence_blast_report.py",
    description="extract fasta sequence from blastn output",
)
PARSER.add_argument(
    "-v",
    "--version",
    help="print version and exit",
    action="version",
    version="%(prog)s 1.1",
)
PARSER.add_argument(
    "output_folder", type=str, help="output folder name & quality report prefix"
)
PARSER.add_argument(
    "directory_path", type=str, help="path to directory of blast reports"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
######################################
counter = 0
DIRECTORY_PATH = ARGS.directory_path
FILES_LIST = []
for file in os.listdir(DIRECTORY_PATH):
    if file.endswith("_results.txt") and os.stat(DIRECTORY_PATH + file).st_size > 0:
        FILES_LIST.append(DIRECTORY_PATH + file)
    elif file.endswith("_results.txt") and os.stat(DIRECTORY_PATH + file).st_size == 0:
        counter += 1
print("You provided folder of {} blast reports files to be processed".format(len(FILES_LIST)))
print("The folder had {} empty blast reports or did not end with _results.txt".format(str(counter)))
####################OUTPUT_FILE_NAME##################
FILE_EXTENSION = '.fna'
os.mkdir(ARGS.output_folder)
RESULTS_FOLDER = ARGS.output_folder + OS_SEPARATOR
OUTPUT_FILE_NAME2 = RESULTS_FOLDER + ARGS.output_folder + '_more_than_1_record.txt'
OUTPUT_FILE_OBJECT2 = open(OUTPUT_FILE_NAME2, 'a+')
OUTPUT_FILE_OBJECT2.write('Strain\tNumber of hits\n')
######################################
file_with_multiple_records_counter = 0
for file_name in FILES_LIST:
    file_name_stripped = file_name.rsplit(OS_SEPARATOR, 1)[-1]
    file_object = open(file_name, 'r')
    line_counter = 0
    cov_list = []
    for line in file_object:
        line_counter += 1
    if line_counter == 10:
        file_object.seek(0)
        file_name_output = RESULTS_FOLDER + (file_name_stripped.split('_results.txt')[0]) + ".fna"
        file_name_object = open(file_name_output, 'w')
        for line in file_object:
            line = line.rstrip()
            line_list = line.split('\t')
            hit_seq = line_list[1].replace('-','')
            hit_id = ('>'+file_name_stripped.split('_results.txt')[0] + '_'
                    + line_list[0] + '\n')
            file_name_object.write(hit_id+hit_seq+'\n')
        file_name_object.close()
    else:
        file_with_multiple_records_counter += 1
        OUTPUT_FILE_OBJECT2.write((file_name_stripped.split('_results.txt')[0])+'\t'+str(line_counter)+'\n')
print("{} blast reports included from {} unempty reports ".format(
        (len(FILES_LIST)-file_with_multiple_records_counter),len(FILES_LIST)))
OUTPUT_FILE_OBJECT2.close()

#!/usr/bin/env python3
import os
import sys
import argparse
from collections import Counter
from collections import defaultdict
from datetime import date
from operator import itemgetter
PARSER = argparse.ArgumentParser(
    prog="Extract_US_genomes.py",
    description="Extract records from GNUVID_report for certain states")
PARSER.add_argument("States", nargs='*', help="States of interest")
PARSER.add_argument("GNUVID_report", type=str, help="GNUVID strain report")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
if not ARGS.States:
    PARSER.exit(status=0, message="Error: You did not provide at least 1 State\n")
States = ARGS.States
OS_SEPARATOR = os.sep
############################
INPUT_GNUVID_report = open(ARGS.GNUVID_report,'r')
header_line = INPUT_GNUVID_report.readline()
State_dict = defaultdict(list)
for line in INPUT_GNUVID_report:
    line = line.rstrip()
    line_list = line.split('\t')
    record_date = line_list[1]
    if line_list[2] == 'USA' and '/USA/' in line_list[0]:
        State_code = line_list[0].split('/USA/')[1][0:2]
        if State_code in States:
            State_dict[State_code].append((record_date, line))
dates_list = ['2020-01-15','2020-02-01','2020-02-16', '2020-03-01',
'2020-03-16', '2020-04-01','2020-04-16', '2020-05-01','2020-05-16',
'2020-06-01','2020-06-16', '2020-07-01','2020-07-16', '2020-08-01',
'2020-08-16','2020-09-01', '2020-09-16','2020-10-01', '2020-10-16',
'2020-11-01', '2020-11-16','2020-12-01','2020-12-16']
dates_names = {'2020-01-15':'End_Jan','2020-02-01':'Mid_Feb','2020-02-16':'End_Feb',
 '2020-03-01':'Mid_Mar','2020-03-16':'End_Mar', '2020-04-01':'Mid_Apr',
 '2020-04-16':'End_Apr', '2020-05-01':'Mid_May','2020-05-16':'End_May',
 '2020-06-01':'Mid_Jun','2020-06-16':'End_Jun', '2020-07-01':'Mid_Jul',
 '2020-07-16':'End_Jul', '2020-08-01':'Mid_Aug','2020-08-16':'End_Aug',
 '2020-09-01':'Mid_Sep', '2020-09-16':'End_Sep', '2020-10-01':'Mid_Oct',
 '2020-10-16':'End_Oct', '2020-11-01':'Mid_Nov', '2020-11-16':'End_Nov',
 '2020-12-01':'Mid_Dec', '2020-12-16':'End_Dec'}
output_script = open('Temporal_plot_collector_curve.sh','w')
for State_name in State_dict:
    os.mkdir(State_name)
    RESULTS_FOLDER = State_name + OS_SEPARATOR
    sorted_list = sorted(State_dict[State_name], key=itemgetter(0))
    period_dict = defaultdict(list)
    for record in sorted_list:
        if record[0] in dates_list:
            date_index = dates_list.index(record[0])
            period_name = dates_names[dates_list[date_index]]
            period_dict[period_name].append(record[1])
        else:
            try:
                temp_list = dates_list.copy()
                temp_list.append(record[0])
                sorted_temp = sorted(temp_list)
                record_index = (sorted_temp.index(record[0])) - 1
                period_name = dates_names[dates_list[record_index]]
                period_dict[period_name].append(record[1])
            except:
                print(record)
                sys.exit()
    #print(period_dict)
    counter = 0
    output_file_list = open('{}_order.txt'.format(State_name),'w')
    output_script.write('../Temporal_plot_Introductions_Importations.py {0}_order.txt {0} {1} {0}/\n'.format(State_name, ARGS.GNUVID_report))
    for time_interval in dates_names.values():
        if period_dict[time_interval]:
            file_name = RESULTS_FOLDER + 'GNUVID_1020_' + State_name + '_' + time_interval+ '.txt'
            OUTPUT_report = open(file_name,'w')
            output_file_list.write(file_name.split('/')[-1]+'\n')
            OUTPUT_report.write(header_line)
            OUTPUT_report.write('\n'.join(period_dict[time_interval]))
            counter += len(period_dict[time_interval])
            OUTPUT_report.close()
    print(State_name,' included genomes: ', counter)

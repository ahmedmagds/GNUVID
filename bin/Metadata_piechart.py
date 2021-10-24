#!/usr/bin/env python3
# this script will make pie charts for GNUVID STs and CCs
import sys
import os
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
from collections import OrderedDict
PARSER = argparse.ArgumentParser(
    prog="Metadata_piechart.py",
    description="metadata piechart script for GNUVID v2.4. It will pie-plot region distribution",)
PARSER.add_argument("-l", "--legend", help="Add legend (default: off)", action="store_true",)
PARSER.add_argument("output", type=str, help="output folder name")
PARSER.add_argument("ST_CC", type=str,
help="ST/CC of interest in a text file (e.g. ST256 (separated by new line) CC4)")
PARSER.add_argument("GNUVID_report", type=str, help="GNUVID strain report")
ARGS = PARSER.parse_args()
###############################
OS_SEPARATOR = os.sep
try:
    os.mkdir(ARGS.output)
    RESULTS_FOLDER = ARGS.output + OS_SEPARATOR
except:
    PARSER.exit(
            status=0,
            message="Folder exists, Please change output name\n")
#########process ST/CC in text file##################
cnt = Counter()
GNU_report_dict = {}
ST_CC_object = open(ARGS.ST_CC,'r')
ST_CC_list = []
for line in ST_CC_object:
    line = line.rstrip()
    ST_CC_list.append(line)
ST_CC_object.close()
#################################
file_object = open(ARGS.GNUVID_report,'r')
file_object.seek(0)
file_object.readline()
Regions = []
Regions_final_list = []
for line in file_object:
    line = line.rstrip()
    Regions.append(line.split('\t')[3])
Regions_cnt = Counter(Regions)
Regions_cnt2 = OrderedDict(Regions_cnt.most_common())
for i in Regions_cnt2:
    Regions_final_list.append(i)
Summary_file   = RESULTS_FOLDER + 'Summary_metadata_pie.txt'
Summary_obj = open(Summary_file,'w')
Summary_obj.write('ST/CC\t{}\n'.format('\t'.join(Regions_final_list)))
###############################
for i in ST_CC_list:
    file_object.seek(0)
    file_object.readline()
    metadata_list = []
    title = i
    if i.startswith('ST'):
        ST_CC = i.split('ST')[1]
        column = -2
    elif i.startswith('CC'):
        ST_CC = i.split('CC')[1]
        column = -1
    else:
        PARSER.exit(status=0,message="One or more ST/CC in the text file does not start with ST or CC\n",)
    for line in file_object:
        line = line.rstrip()
        line_list = line.split('\t')
        if line_list[column] == ST_CC:
            metadata_list.append(line_list[3])
    metadata_Count = Counter(metadata_list)
    print(metadata_Count)
    ST_CC_counts = []
    ST_CC_counts_str = []
    Summary_obj.write(title+'\t')
    for j in Regions_final_list:
        ST_CC_counts.append(metadata_Count[j])
        ST_CC_counts_str.append(str(metadata_Count[j]))
    Summary_obj.write('\t'.join(ST_CC_counts_str))
    fig1, ax1 = plt.subplots(figsize=(4.8, 4.8))
    xx = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#000000','#8c564b']
    pie = ax1.pie(ST_CC_counts, startangle=90, colors=xx)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    if ARGS.legend:
        plt.legend(pie[0],Regions_final_list, bbox_to_anchor=(1,0), loc="best",
                          bbox_transform=plt.gcf().transFigure)
    ax1.set_title(title, fontsize=20)
    #plt.legend(pie[0],labels,loc='center left', bbox_to_anchor=(-0.1, 1.),
    #       fontsize=8)
    #plt.show()
    #plt.subplots_adjust()
    #plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    figure_name = '{}{}_metadata_pie.png'.format(RESULTS_FOLDER,title)
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.savefig(figure_name, format='png', bbox_inches='tight', dpi=300)
    Summary_obj.write('\n')
    plt.close()

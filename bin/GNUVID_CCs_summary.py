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

# DATE CREATED: July 1, 2020

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
from collections import defaultdict
from collections import Counter
import argparse

PARSER = argparse.ArgumentParser(
    prog="GNUVID_CCs_summary.py",
    description="GNUVID_CCs_summary summarizes the GNUVID DB_isolates_report")
PARSER.add_argument(
    "inactive_date",
    type=str,
    help="an inactive date cutoff, usually 1 month before release date, in this format (2020-06-03) to assign status"
)
PARSER.add_argument(
    "quiet_date", type=str, help="a quiet date cutoff, usually 2 weeks before release date, in this format (2020-06-03) to assign status"
)
PARSER.add_argument(
    "DB_isolates_report", type=str, help="GNUVID_DB_isolates_report to analyze that has STs and CCs (.txt)"
)
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
#############################
inactive_date = ARGS.inactive_date
quiet_date = ARGS.quiet_date
release_date = [inactive_date, quiet_date]
##############################
output_report_file = (
          ARGS.DB_isolates_report.split("_DB_isolates_report.txt")[0]
          + "_CCs_report.txt")
output_report_object = open(output_report_file,'w')
output_report_file2 = (
          ARGS.DB_isolates_report.split("_DB_isolates_report.txt")[0]
          + "_CCs_report.md")
output_report_object2 = open(output_report_file2,'w')
input_report_object = open(ARGS.DB_isolates_report,'r')
header_line = (input_report_object.readline().rstrip()).split('\t')
ST_index = header_line.index('ST')
try:
  CC_index = header_line.index('CC')
except:
  PARSER.exit(
      status=0,
      message="The report does not have CC column, run goeBURST\n")
#knowing the regions
try:
  Region_index = header_line.index('Region')
except:
  PARSER.exit(
      status=0,
      message="The report does not have Region\n")
#capturing dates, countries, regions for STs
input_report_object.seek(0)
input_report_object.readline()
CC_country_dict = defaultdict(list)
CC_dates_dict = defaultdict(list)
CC_region_dict = defaultdict(list)
CC_isolates_dict = defaultdict(list)
CC_STs_dict = defaultdict(list)
CC_list = []
for line in input_report_object:
  line = line.rstrip()
  line_list = line.split('\t')
  if line_list[CC_index] != "NA":
      ST_date = line_list[1]
      ST_country = line_list[2]
      ST_region = line_list[Region_index]
      ST_number = line_list[ST_index]
      CC_number = int(line_list[CC_index])
      if CC_number not in CC_list:
          CC_list.append(CC_number)
      if ST_date.count('-') == 2:
          if len(ST_date) == 10:
              CC_dates_dict[CC_number].append(ST_date)
          else:
              ST_date_list = ST_date.split('-')
              if len(ST_date_list[1]) == 1:
                  ST_date_list[1] = ('0'+ST_date_list[1])
              if len(ST_date_list[2]) == 1:
                  ST_date_list[2] = ('0'+ST_date_list[2])
              ST_date = '-'.join(ST_date_list)
              CC_dates_dict[CC_number].append(ST_date)
      CC_country_dict[CC_number].append(ST_country)
      CC_region_dict[CC_number].append(ST_region)
      CC_STs_dict[CC_number].append(ST_number)
      CC_isolates_dict[CC_number].append(line_list[0])
######Writing report######
output_report_header = 'Clonal Complex\tNumber of STs\tNumber of isolates\tMost common 5 countries\tMost common Region\tDate range\tStatus\n'
output_report_object.write(output_report_header)
output_report_object2.write('| Clonal Complex            | Number of STs | Number of isolates | Most common 5 countries                             | Most common Region                             | Date range                 |   Status |\n|--------------------------|---------------|--------------------|----------------------------------------------------|-----------------------------------------------|---------------------------|---------|\n')
for CC in sorted(CC_list):
    release_date = [inactive_date, quiet_date]
    STs_count = len(set(CC_STs_dict[CC]))
    isolates_count = len(CC_isolates_dict[CC])
    sorted_dates = sorted(CC_dates_dict[CC])
    dates_range = sorted_dates[0] + ' to ' + sorted_dates[-1]
    if sorted_dates[-1] in release_date:
        date_index = release_date.index(sorted_dates[-1])
        if date_index == 0:
            CC_state = "Quiet"
        else:
            CC_state = "Active"
    else:
        release_date.append(sorted_dates[-1])
        state_date = sorted(release_date).index(sorted_dates[-1])
        if state_date == 0:
            CC_state = "Inactive"
        elif state_date == 1:
            CC_state = "Quiet"
        else:
            CC_state = "Active"

    Top_5_countries = Counter(CC_country_dict[CC]).most_common(5)
    Countries_list = []
    for i in Top_5_countries:
        country_percent = i[0] + " ({:.0%})".format(i[1]/isolates_count)
        Countries_list.append(country_percent)
    Top_Region = Counter(CC_region_dict[CC]).most_common(1)[0] #tuple
    Top_Region_percent = Top_Region[0] + " ({:.0%})".format(Top_Region[1]/isolates_count)
    output_report_object.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
            CC,STs_count,isolates_count,', '.join(Countries_list),
            Top_Region_percent, dates_range, CC_state))
    if CC_state == "Active":
        CC_state = "**Active**"
        CC = "**" + str(CC) + "**"
    output_report_object2.write('| {} | {} | {} | {} | {} | {} | {} |\n'.format(
            CC,STs_count,isolates_count,', '.join(Countries_list),
            Top_Region_percent, dates_range, CC_state))

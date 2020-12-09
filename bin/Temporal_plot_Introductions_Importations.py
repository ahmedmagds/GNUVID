#!/usr/bin/env python3
import os
import sys
import argparse
from collections import Counter
from collections import defaultdict
from datetime import date
from operator import itemgetter
import matplotlib.pyplot as plt
PARSER = argparse.ArgumentParser(
    prog="Temporal_plot_Introductions_Exportations.py",
    description="Temporal plot for circulating CCs and number of Introductions/Exportations",)
PARSER.add_argument("-a","--alleles",help="include the 10 ORFs calculations [default OFF]",action="store_true",)
PARSER.add_argument("list",type=str,help="Files List ordered by month")
PARSER.add_argument("State", type=str, help="State code of interest")
PARSER.add_argument("GNUVID_report", type=str, help="GNUVID strain report")
PARSER.add_argument("directory", type=str, help="ST GNUVID tab report")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
#############################CC Temporal Plot###################################
output_folder = '{}_Temporal_plot_Introductions_Exportations'.format(ARGS.State)
os.mkdir(output_folder)
RESULTS_FOLDER = output_folder + OS_SEPARATOR
QUERY = ARGS.directory
time_list = []
QUERY_LIST = []
list_file_object = open(ARGS.list, 'r')
for line in list_file_object:
    line = line.rstrip()
    time_interval = line.split('.txt')[0]
    time_list.append(time_interval)
    QUERY_LIST.append(QUERY + line)
print('#############################################')
print("You provided folder of {} GNUVID report files for {}".format(len(QUERY_LIST),ARGS.State))
##################################
all_dict = defaultdict(list)
all_dict_times = defaultdict(list)
total_genomes_no_ambig = []
for QUERYFILE in QUERY_LIST:
    GNUVID_obj = open(QUERYFILE, 'r')
    op_file = RESULTS_FOLDER + QUERYFILE.rsplit('/',1)[-1].split('.txt')[0] + '_report.txt'
    time_name = QUERYFILE.rsplit('/',1)[-1].split('.txt')[0]
    output_CC_obj = open(op_file, 'w')
    GNUVID_obj.readline()
    ST_list = []
    CC_list = []
    for line in GNUVID_obj:
        line = line.rstrip()
        line_list = line.split('\t')
        Strain_CC = line_list[-2]
        Strain_ST = line_list[-3]
        if line_list[-3] != "Novel":
            total_genomes_no_ambig.append(Strain_ST)
        ST_list.append(Strain_ST)
        CC_list.append(Strain_CC)
    ST_C = Counter(ST_list)
    most_occur_ST = ST_C.most_common()
    CC_C = Counter(CC_list)
    most_occur_CC = CC_C.most_common()
    #print(op_file,' ',CC_C)
    for CC_name in most_occur_CC:
        all_dict[CC_name[0]].append(int(CC_name[1]))
        all_dict_times[CC_name[0]].append(time_name)
    output_CC_obj.write('CC\tCount\n')
    output_CC_obj.write(
        "\n".join("{}\t{}".format(x[0], x[1]) for x in most_occur_CC)
    )
    output_CC_obj.write('\n#################\n')
    output_CC_obj.write('ST\tCount\n')
    output_CC_obj.write(
        "\n".join("{}\t{}".format(x[0], x[1]) for x in most_occur_ST)
    )
    output_CC_obj.close()
    GNUVID_obj.close()
CC_values  = all_dict.keys()
#print(CC_values)
#print(all_dict_times)
file_name2 = 'Temporal_plot_summary_{}.txt'.format(ARGS.State)
Output_CC_obj2 = open(file_name2, 'w')
Output_CC_obj2.write('\t{}\tTotal_genomes\n'.format('\t'.join(CC_values)))
#print(time_list)
each_CC_dict = {}
final_list_percent = []
for y in time_list:
    final_list = []
    Output_CC_obj2.write('{}\t'.format(y))
    for CC in CC_values:
        if y in all_dict_times[CC]:
            CC_index = all_dict_times[CC].index(y)
            CC_counts_list = all_dict[CC]
            final_list.append(CC_counts_list[CC_index])
            each_CC_dict[CC] = str(sum(CC_counts_list))
        else:
            final_list.append(0)
    #print(final_list)
    total_genomes = sum(final_list)
    print(y,': ',total_genomes)
    final_list_str = [str(x) for x in final_list]
    final_list_str.append(str(total_genomes))
    tmp_list_percent = [str('{:.4f}'.format(x/total_genomes)) for x in final_list]
    final_list_percent.append(tmp_list_percent)
    Output_CC_obj2.write('{}\n'.format('\t'.join(final_list_str)))
total_per_CC = []
for CC2 in CC_values:
    total_per_CC.append(each_CC_dict[CC2])
Output_CC_obj2.write('Total_per_CC\t{}\n'.format('\t'.join(total_per_CC)))
Output_CC_obj2.write('\n#################\n')
Output_CC_obj2.write('\t{}\tTotal_genomes\n'.format('\t'.join(CC_values)))
for y,z in zip(time_list,final_list_percent):
    Output_CC_obj2.write('{}\t{}\n'.format(y,'\t'.join(z)))
Output_CC_obj2.close()
print('Total number of genomes included for Introductions/Exportations analysis: ',
        len(total_genomes_no_ambig))

##########################Alleles Collector Curve###############################
# Query list  from previous step
input_file_object = open(QUERY_LIST[0], 'r')
Genes = input_file_object.readline().split('\t')[4:15]
indices = [4,5,6,7,8,9,10,11,12,13,14]
input_file_object.close()
Times = ['End_Jan','Mid_Feb','End_Feb','Mid_Mar','End_Mar','Mid_Apr',
'End_Apr','Mid_May','End_May', 'Mid_Jun','End_Jun', 'Mid_Jul', 'End_Jul',
'Mid_Aug','End_Aug','Mid_Sep', 'End_Sep','Mid_Oct']
#####################
time_dict_raw = defaultdict(list)
time_dict_percent = defaultdict(list)
op_file1 = 'Allelic_diversity_{}_results.txt'.format(ARGS.directory.split('/')[0])
op_file2 = RESULTS_FOLDER + 'Novel_STs_{}_results.txt'.format(ARGS.directory.split('/')[0])
Output_obj = open(op_file1, "w")
Output_obj2 = open(op_file2, "w")
Output_obj2.write('Time_period\tNumber_of_Novel_STs\tNumber of Distinct STs\tNovel_STs_percentage\tSTs\n')
All_STs = set()
INPUT_NOVEL_STs_list = []
for QUERYFILE in QUERY_LIST:
    counter = 0
    QUERYFILE_OBJECT = open(QUERYFILE, "r")
    QUERYFILE_OBJECT.readline()
    time_period = QUERYFILE.rsplit('/',1)[-1].split('.txt')[0].split('_',3)[-1]
    Alleles_ST_numbers_dict = defaultdict(list)
    for Gene in Genes:
        Alleles_ST_numbers_dict[Gene]
    for line in QUERYFILE_OBJECT:
        line = line.rstrip()
        line_list = line.split('\t')
        if line_list[14] != "Novel":
            counter += 1
            for Gene,Index in zip(Genes,indices):
                Alleles_ST_numbers_dict[Gene].append(int(line_list[Index]))
    #########Reporting############
    #print(time_period, '\t', counter)
    for record in Genes:
        period_alleles = Alleles_ST_numbers_dict[record]
        #time_dict_set[time_period].extend(period_alleles)
        time_dict_raw[time_period].append(str(len(set(period_alleles))))
        try:
            time_dict_percent[time_period].append('{:.2f}'.format(len(set(period_alleles))/counter))
        except:
            if len(set(period_alleles)) == 0 and counter == 0:
                time_dict_percent[time_period].append('{:.2f}'.format(0))
    time_dict_raw[time_period].append(str(counter))
    #time_dict_percent[time_period].append(str(counter))
    #capturing novel STs in each period
    period_STs = set(Alleles_ST_numbers_dict['ST'])
    Novel_STs = period_STs - All_STs
    Novel_STs_list = [('ST'+str(x)) for x in Novel_STs]
    All_STs = All_STs.union(period_STs)
    try:
        Novel_STs_percent = '{:.2f}'.format(len(Novel_STs)/len(period_STs))
    except:
        if len(Novel_STs) == 0 and len(period_STs) == 0:
            Novel_STs_percent = '{:.2f}'.format(0)
    time_dict_raw[time_period].append(str(len(Novel_STs)))
    time_dict_percent[time_period].append(Novel_STs_percent)
    Output_obj2.write('{}\t{}\t{}\t{}\t{}\n'.format(time_period,len(Novel_STs),len(period_STs),Novel_STs_percent,'\t'.join(Novel_STs_list)))
    Novel_STs_list.insert(0, time_period)
    INPUT_NOVEL_STs_list.append(Novel_STs_list)
#print('\t','\t'.join(Genes),'\tTotal')


##########################Introductions/Exportations############################
period_dict = {}
Novel_STs_list = []
for time_ST_list in INPUT_NOVEL_STs_list:
    Novel_STs = time_ST_list[1:]
    for i in Novel_STs:
        period_dict[i[2:]] = time_ST_list[0]
        Novel_STs_list.append(i[2:])
Introductions_dict = defaultdict(list)
US_Introductions_dict = defaultdict(list)
#############################
State_code = ARGS.State
INPUT_GNUVID_report = open(ARGS.GNUVID_report,'r')
header_line = INPUT_GNUVID_report.readline().rstrip()
op_file1 = RESULTS_FOLDER + 'STs_multiple_countries_ordered_{}_introductions.txt'.format(ARGS.State)
op_file2 = RESULTS_FOLDER + 'STs_multiple_countries_ordered_{}_all.txt'.format(ARGS.State)
Output_obj3 = open(op_file1, "w")
Output_obj4 = open(op_file2, "w")
#Output_obj = open('STs_multiple_regions_ordered.txt', "w")
ST_country_dict = defaultdict(list)
date_country_dict = defaultdict(list)
ST_CC = {}
ST_dates = defaultdict(list)
all_dates = defaultdict(list)
all_state_dates = defaultdict(list)
State_ST_dates = defaultdict(list)
State_code_USA = '/USA/' + State_code
ST_states = defaultdict(list)
for line in INPUT_GNUVID_report:
    line = line.rstrip()
    line_list = line.split('\t')
    if line_list[-3] != "Novel":
        country = line_list[2]
        row_date = line_list[1]
        #country = line_list[3]#region
        Strain_ST = line_list[-3]
        ST_CC[Strain_ST] = line_list[-2]
        ST_country_dict[Strain_ST].append(country)
        if len(row_date) < 10:
            ST_date_lst = row_date.split('-')
            if len(ST_date_lst[1]) < 2:
                new_date = '0' + ST_date_lst[1]
                ST_date_lst[1] = new_date
            if len(ST_date_lst[2]) < 2:
                new_date2 = '0' + ST_date_lst[2]
                ST_date_lst[2] = new_date2
            row_date = '-'.join(ST_date_lst)
        date_country_dict[Strain_ST].append((row_date,country))
        all_dates[Strain_ST].append(row_date)
        if State_code_USA in line_list[0]:
            all_state_dates[Strain_ST].append(row_date)
            State_ST_dates[Strain_ST].append(row_date)
        else:
            ST_dates[Strain_ST].append((row_date,country))#solving the order of countries issue
        if '/USA/' in line_list[0]:
            State_name = line_list[0].split('/USA/')[-1][0:2]
            ST_states[Strain_ST].append((row_date,State_name))
print('total number of STs: ',len(State_ST_dates))
counter = 0
counter_exp = 0
counter_overseas = 0
STs_successful = []
for record in Novel_STs_list:
    countries_list = ST_country_dict[record]
    countries_count = len(set(ST_country_dict[record]))
    if countries_count >= 2:
        STs_successful.append(record)
#STs_successful_sorted = sorted(STs_successful, key = lambda x: x[1],reverse=True)
#print(STs_successful_sorted)
header = 'ST\tCC\tPeriod\tNumber of countries\tNumber of isolates\tNumber of isolates {}\tFirst_seen\t{}_date\tOrigin\tdays\tCountries\n'.format(State_code,State_code)
Output_obj3.write(header)
Output_obj4.write(header)
for nov_ST in Novel_STs_list:
    new_list = []
    countries_list = ST_country_dict[nov_ST]
    sorted_countries_list = sorted(date_country_dict[nov_ST], key=itemgetter(0))
    isolates_count = len(countries_list)
    countries_count = len(set(countries_list))
    CC = ST_CC[nov_ST]
    ST_date = sorted(ST_dates[nov_ST], key=itemgetter(0))
    State_date = sorted(State_ST_dates[nov_ST])
    ST_period = period_dict[nov_ST]
    isolates_count_State = len(all_state_dates[nov_ST])
    if not ST_date:#in case the list is empty because all dates were 2020 or 2020-month
        ST_date.append(('',''))
    if not State_date:#in case the list is empty because all dates were 2020 or 2020-month
        State_date.append('')
    try:
        if len(ST_date[0][0]) > 7 and len(State_date[0]) > 7:
            dates = [ST_date[0][0], State_date[0]]
            sorted_dates = sorted(dates)
            if len(set(dates)) == 1:
                origin = State_code
                days = '0'
            elif sorted_dates.index(State_date[0]) == 0:
                origin = State_code
                State_date_l = [int(x) for x in sorted_dates[0].split('-')]
                other_date_l = [int(x) for x in sorted_dates[1].split('-')]
                days = str((date(State_date_l[0],State_date_l[1],State_date_l[2])
                            - date(other_date_l[0],other_date_l[1],other_date_l[2])).days)
            else:
                origin = 'other'
                State_date_l = [int(x) for x in sorted_dates[1].split('-')]
                other_date_l = [int(x) for x in sorted_dates[0].split('-')]
                days = str((date(State_date_l[0],State_date_l[1],State_date_l[2])
                            - date(other_date_l[0],other_date_l[1],other_date_l[2])).days)
        else:
            if len(set(countries_list)) == 1 and len(State_date[0]) > 7:
                origin = State_code
                days = '0'
            else:
                origin = 'NA'
                days = 'NA'
    except:
        print(nov_ST)
        print(ST_date)
        print(State_date)
    if len(sorted_countries_list) > 0:
        for j in sorted_countries_list:
            if j[1] not in new_list:
                new_list.append(j[1])
    for i in countries_list:#capture countries that does not have date (i.e. only year or month)
        if i not in new_list:
            new_list.append(i)
    if len(State_date[0]) < 7:
        state_1st_date = sorted(all_state_dates[nov_ST])[0]
    else:
        state_1st_date = State_date[0]
    if len(ST_date[0][0]) < 7:
        other_1st_date = sorted(all_dates[nov_ST])[0]
    else:
        other_1st_date = ST_date[0][0]
    Output_obj4.write(nov_ST+'\t'+CC+'\t'+ST_period+'\t'+str(countries_count)+'\t'
    +str(isolates_count) +'\t'+str(isolates_count_State)+'\t' +other_1st_date+'\t'+state_1st_date+'\t'
    +origin+'\t'+days+'\t'+'\t'.join(new_list)+'\n')
    if origin == 'other' and int(days) >= 10:
        if new_list[0] == 'USA':
            sorted_ST_states = sorted(ST_states[nov_ST], key=itemgetter(0))
            try:
                first_State_code = '(' + sorted_ST_states[0][1] + ')'
            except:
                first_State_code = '(undetermined)'
        else:
            first_State_code = '(overseas)'
        Output_obj3.write(nov_ST+'\t'+CC+'\t'+ST_period+'\t'+str(countries_count)+'\t'
        +str(isolates_count) +'\t'+str(isolates_count_State)+'\t' +other_1st_date+'\t'+state_1st_date+'\t'
        +origin+' '+first_State_code+'\t'+days+'\t'+'\t'.join(new_list)+'\n')
        counter +=1
        Introductions_dict[ST_period].append(nov_ST)
        if first_State_code == '(overseas)':
            counter_overseas +=1
        if first_State_code != '(overseas)':
            US_Introductions_dict[ST_period].append(nov_ST)
    if origin == ARGS.State and int(days) <= -10:
        counter_exp +=1
#########################Alleles Collector Curve Report#########################
for j in Introductions_dict:
    novel_count = int(time_dict_raw[j][-1])
    time_dict_raw[j].append(str(len(Introductions_dict[j])))
    if novel_count != 0:
        time_dict_percent[j].append('{:.2f}'.format(len(Introductions_dict[j])/novel_count))
    else:
        time_dict_percent[j].append('{:.2f}'.format(0))
for j in US_Introductions_dict:
    introduced_count = int(time_dict_raw[j][-1])
    time_dict_raw[j].append(str(len(US_Introductions_dict[j])))
    if introduced_count != 0:
        time_dict_percent[j].append('{:.2f}'.format(len(US_Introductions_dict[j])/introduced_count))
    else:
        time_dict_percent[j].append('{:.2f}'.format(0))

if ARGS.alleles:
    Output_obj.write('\t'+'\t'.join(Genes[:-1])+'\tDistinct STs\tTotal # Genomes\tNovel STs\tAll Introduced STs\tIntroduced from US States\n')
else:
    Output_obj.write('\tDistinct STs\tTotal # Genomes\tNovel STs\tAll Introduced STs\tIntroduced from US States\n')
for period in Times:
    if ARGS.alleles:
        Output_obj.write(period+'\t'+'\t'.join(time_dict_raw[period])+'\n')
    else:
        Output_obj.write(period+'\t'+'\t'.join(time_dict_raw[period][-5:])+'\n')
Output_obj.write('########################\n')
#print('\t','\t'.join(Genes),'\tTotal')
if ARGS.alleles:
    Output_obj.write('\t'+'\t'.join(Genes[:-1])+'\tDistinct STs/Total # Genomes\tNovel STs/Distinct STs\tAll Introduced STs/Novel STs\tIntroduced from US States/All Introduced STs\n')
else:
    Output_obj.write('\tDistinct STs/Total # Genomes\tNovel STs/Distinct STs\tAll Introduced STs/Novel STs\tIntroduced from US States/All Introduced STs\n')
for period in Times:
    if ARGS.alleles:
        Output_obj.write(period+'\t'+'\t'.join(time_dict_percent[period])+'\n')
    else:
        Output_obj.write(period+'\t'+'\t'.join(time_dict_percent[period][-4:])+'\n')
#print(record,'\t',len(set(Alleles_ST_numbers_dict[record])))
Output_obj.write('########################\n\
Total number of genomes included for Introductions/Exportations analysis: {}\n\
Total number of STs: {}\n\
Total number of ST-introductions: {}\n\
Total number of overseas ST-introductions: {}\n\
Total number of USA (domestic) ST-introductions: {}\n\
Total number of ST-Exportations: {}\n'.format(len(total_genomes_no_ambig),
len(State_ST_dates),counter,counter_overseas,counter-counter_overseas,counter_exp))
print('Total number of ST-introductions: ', counter)
print('Total number of overseas ST-introductions: ', counter_overseas)
print('Total number of USA (domestic) ST-introductions: ', counter-counter_overseas)
print('Total number of ST-Exportations: ', counter_exp)
print('#############################################')

# Scatter plot on top of lines
#plt.subplot(212)
'Distinct STs/Total # Genomes	Novel STs/Distinct STs	All Introduced STs/Novel STs	Introduced from US States/All Introduced STs'
for index,line_color in zip([-4,-3,-2,-1],['r','b','g','k']):
    counter = 4
    x = []
    y = []
    for period in Times:
        if time_dict_percent[period]:
            if float(time_dict_percent[period][index]) != 0.0:
                x.append(Times.index(period) + counter)
                y.append(float(time_dict_percent[period][index]))
        counter += 1
    plt.plot(x, y, line_color)
    plt.scatter(x, y, c=line_color)
plt.title(ARGS.State)
plt.xlabel('Weeks since the start of the pandemic in December', fontsize=12, fontname="sans-serif", fontweight="bold")
plt.ylabel('Ratios', fontsize=12, fontname="sans-serif", fontweight="bold")
plt.xticks([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],fontsize=12, fontname="sans-serif")
plt.yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=12, fontname="sans-serif")
plt.savefig('Introductions_Ratios_{}.png'.format(ARGS.State), format='png', bbox_inches='tight', dpi=300)
plt.close()

plt.figure(figsize=(20,7))
for index,line_color in zip([-4,-2],['r','g']):
    counter = 4
    x = []
    y = []
    for period in Times:
        if time_dict_percent[period]:
            if float(time_dict_percent[period][index]) != 0.0:
                x.append(Times.index(period) + counter)
                y.append(float(time_dict_percent[period][index]))
        counter += 1
    plt.plot(x, y, line_color)
    plt.scatter(x, y, c=line_color)
plt.title(ARGS.State,fontsize=32, fontname="arial", fontweight="bold")
plt.xlabel('Weeks since the start of the pandemic in December', fontsize=32, fontname="arial", fontweight="bold")
plt.ylabel('Ratios', fontsize=32, fontname="arial", fontweight="bold")
ax = plt.subplot()
ax.spines['bottom'].set_color('#000000')
ax.spines['top'].set_color('#000000')
plt.setp(ax.spines.values(), linewidth=5)
ax.xaxis.set_tick_params(length=9,width=5)
ax.yaxis.set_tick_params(length=9,width=5)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xticks([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],fontsize=32, fontname="arial",fontweight="bold")
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize=32, fontname="arial",fontweight="bold")
plt.savefig('Two_Introductions_Ratios_{}.png'.format(ARGS.State), format='png', bbox_inches='tight', dpi=300)
plt.close()

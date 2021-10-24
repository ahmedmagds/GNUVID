#!/usr/bin/env python3
import os
import sys
import argparse
import time
from collections import defaultdict
from collections import Counter
from sklearn.model_selection import train_test_split
PARSER = argparse.ArgumentParser(
    prog="GNUVID_Subsample_STs.py",
    description="This script will subsample STs from fasta file",)
PARSER.add_argument("-t","--test",help="only test data [default OFF]",action="store_true",)
PARSER.add_argument("-m","--min_test",type=int,help="minimum test size [Default: 140,000]",)
PARSER.add_argument("fasta_aln", type=str, help="path to Multifasta.fna name")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
##########################
###########multifasta aln##############
in_fasta_aln_obj = open(ARGS.fasta_aln, 'r')
if ARGS.min_test:
    test_size = ARGS.min_test
else:
    test_size = 140000
if ARGS.test:
    subsample = 'testonly'
    CC_dict = defaultdict(list)
    seq_header = []
    seq_CC = []
    for line in in_fasta_aln_obj:
        if line.startswith('>'):
            ST1,CC1 = line.rstrip().lstrip('>').split('_CC')
            if int(ST1.split('_')[-1]) > 1 and CC1 != 'NA':
                seq_header.append(line.rstrip().lstrip('>'))
                seq_CC.append(CC1)
                CC_dict[CC1].append(seq_header)
    X_train,X_test,y_train,y_test=train_test_split(seq_header,seq_CC,test_size=test_size,random_state=1)
    print('Number of CCs in unused data',len(Counter(y_train)),flush=True)
    print('Number of CCs in test data',len(Counter(y_test)),flush=True)
    #tmp_lst = []
    #for CC in CC_dict:
    #    if len(CC_dict[CC]) == 1:
    #        tmp_lst.extend(CC_dict[CC])
    #print(tmp_lst[:15])
    #print(X_test[:10],X_test[-10:])
    #ext_lst = X_test + tmp_lst
    #print(ext_lst[:10],ext_lst[-10:])
    #X_set = set(ext_lst)
    X_set = set(X_test)
    #y_set_plus = set([x.split('_CC')[-1] for x in ext_lst])
    #print('Number of CCs in test data after adding singletons',len(y_set_plus),flush=True)
else:
    subsample = 'both'
if subsample == 'both':
    output_fasta_aln = ARGS.fasta_aln.rsplit('.fna')[0] + '_Train_subsampled.fna'
    output_fasta_aln_obj = open(output_fasta_aln, 'w')
    output_fasta_aln2 = ARGS.fasta_aln.rsplit('.fna')[0] + '_Test_subsampled.fna'
    output_fasta_aln_obj2 = open(output_fasta_aln2, 'w')
else:
    output_fasta_aln2 = ARGS.fasta_aln.rsplit('.fna')[0] + '_Test_subsampled.fna'
    output_fasta_aln_obj2 = open(output_fasta_aln2, 'w')
SEQUENCE_STRING = ""
counter = 0
counter2 = 0
CC_list = []
CC_all = []
in_fasta_aln_obj.seek(0)
for line in in_fasta_aln_obj:
    if line.startswith(">"):
        if len(SEQUENCE_STRING) > 0:
            CC = SEQUENCE_INFO.split('_CC')[-1]
            if CC != 'NA':
                CC_all.append(CC)
            if subsample == 'both':
                if '_1_CC' in SEQUENCE_INFO and '_CCNA' not in SEQUENCE_INFO:
                    output_fasta_aln_obj.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING)
                    counter += 1
                if SEQUENCE_INFO in X_set:
                    output_fasta_aln_obj2.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING)
                    CC_list.append(CC)
                    counter2 += 1
            else:
                if SEQUENCE_INFO in X_set:
                    output_fasta_aln_obj2.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING)
                    CC_list.append(CC)
                    counter2 += 1
            SEQUENCE_STRING = ""
        SEQUENCE_INFO = line.lstrip(">").rstrip()
    else:
        SEQUENCE_STRING += line
CC = SEQUENCE_INFO.split('_CC')[-1]
if CC != 'NA':
    CC_all.append(CC)
if subsample == 'both':
    if '_1_CC' in SEQUENCE_INFO and '_CCNA' not in SEQUENCE_INFO:
        output_fasta_aln_obj.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING)
        counter += 1
    if SEQUENCE_INFO in X_set:
        output_fasta_aln_obj2.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING)
        CC_list.append(CC)
        counter2 += 1
else:
    if SEQUENCE_INFO in X_set:
        output_fasta_aln_obj2.write('>'+SEQUENCE_INFO+'\n'+SEQUENCE_STRING)
        CC_list.append(CC)
        counter2 += 1
in_fasta_aln_obj.close()
if subsample == 'both':
    print('Training records included: ',counter,flush=True)
    print('Testing records included: ',counter2,flush=True)
    output_fasta_aln_obj.close()
else:
    print('Testing records included: ',counter2,flush=True)
CCs = '{} Testing CCs included of total CCs: {}'.format(len(Counter(CC_list)),len(Counter(CC_all)))
print(CCs,flush=True)
output_fasta_aln_obj2.close()
##############################

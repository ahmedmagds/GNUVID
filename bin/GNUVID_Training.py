#!/usr/bin/env python3
import os
import pickle
import sys
import argparse
import pandas as pd
import psutil
import numpy as np
import time
from sklearn.datasets import make_classification
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix, make_scorer
from sklearn.model_selection import cross_val_score
import joblib
#################
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
###############################
PARSER = argparse.ArgumentParser(
    prog="GNUVID_Training.py",
    description="This script will Train on SARS-CoV-2 Seqs",)
PARSER.add_argument("-c","--cross_val",help="run cross validation on the training set",action="store_true",)
PARSER.add_argument("-p","--testing_Percent",type=float,help="training/testing percent [default 0.3]")
PARSER.add_argument("-t","--test_data",type=str,help="If given will be used for testing instead of using testing_Percent of the fasta_aln")
PARSER.add_argument("fasta_aln", type=str, help="Training aln file")
PARSER.add_argument("features", type=str, help="features file (.vcf or .txt)")
if len(sys.argv) == 1:
    PARSER.print_help()
    sys.exit(0)
ARGS = PARSER.parse_args()
OS_SEPARATOR = os.sep
if ARGS.testing_Percent:
    testing_Percent = ARGS.testing_Percent #training/testing percent
else:
    testing_Percent = 0.3
aln_file = ARGS.fasta_aln #sequence file
VCF_file = ARGS.features # has the nucleotide(feature) positions
VCF_OBJECT = open(VCF_file,'r')
#########Parse VCF features list############
memory_op = open('memory_usage.txt','a')
TIMESTR = time.strftime("%Y%m%d_%H%M")
TIMESTR2 = time.strftime("%m%d%Y")
FO_name = 'GNUVIDML_report_' + TIMESTR + '.txt'
OUTPUT_OBJECT = open(FO_name,'w')
START_TIME = time.time()
features_list = []
postitions_list = []
if '.vcf' in VCF_file:
    for line in VCF_OBJECT:
        if '#' not in line:
            features_list.append(line.split()[1])
            postitions_list.append(int(line.split()[1])-1)
    op_name = 'SNPs_{}_{}.txt'.format(str(len(features_list)),TIMESTR2)
    op = open(op_name,'w')
    op.write('\n'.join(features_list))
    op.close()
else:
    for line in VCF_OBJECT:
        features_list.append(line.rstrip())
        postitions_list.append(int(line.rstrip())-1)
VCF_OBJECT.close()
features_list.insert(0, 'CC')
print('Features ',len(features_list)-1)
OUTPUT_OBJECT.write('Features {}\n'.format(len(features_list)-1))
memory_op.write('RAM memory % used after features: {}'.format(psutil.virtual_memory()[3]))
print('RAM memory % used after features: {}'.format(psutil.virtual_memory()[3]),flush=True)
print(("Finished Features processing in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
###########Parse the alignment file#########
def process_aln_file(seq_file,memory_op,testing):
    SEQ_OBJECT = open(seq_file,'r')
    SEQUENCES_LIST = []
    order_list = []
    SEQUENCE_STRING = ''
    counter = 0
    for line in SEQ_OBJECT:
        line = line.rstrip()
        if line.startswith(">"):
            if (len(SEQUENCE_STRING) > 0):
                if SEQUENCE_INFO.split('_CC')[-1] != 'NA':
                    counter += 1
                    if counter in [1000,50000,100000,200000,300000,400000,500000,600000,700000]:
                        memory_op.write('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter))
                        print('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter),flush=True)
                    lst = list(SEQUENCE_STRING)
                    if testing =='y':
                        lst = [lst[ind] for ind in postitions_list]
                    lst.insert(0,SEQUENCE_INFO.split('_CC')[-1])
                    SEQUENCES_LIST.append(lst)
                SEQUENCE_STRING = ""
            SEQUENCE_INFO = line.lstrip(">")
            order_list.append(SEQUENCE_INFO)
        else:
            SEQUENCE_STRING += line
    if SEQUENCE_INFO.split('_CC')[-1] != 'NA':
        counter += 1
        if counter in [1000,50000,100000,200000,300000,400000,500000,600000,700000]:
            memory_op.write('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter))
            print('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],counter),flush=True)
        lst = list(SEQUENCE_STRING)
        if testing =='y':
            lst = [lst[ind] for ind in postitions_list]
        lst.insert(0,SEQUENCE_INFO.split('_CC')[-1])
        SEQUENCES_LIST.append(lst)
    SEQ_OBJECT.close()
    return SEQUENCES_LIST, order_list, counter
###################################
if '.aln' in aln_file:
    Tn_SEQUENCES_LIST,Tn_order_list, Tn_counter = process_aln_file(aln_file,memory_op, 'n')
    print('Genome in aln: ',len(Tn_order_list))
    print('Genome included: ',len(Tn_SEQUENCES_LIST))
    OUTPUT_OBJECT.write('Genome in aln: {}\n'.format(len(Tn_order_list)))
    OUTPUT_OBJECT.write('Genome included: {}\n'.format(len(Tn_SEQUENCES_LIST)))
    memory_op.write('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],Tn_counter))
    print('RAM memory % used: {} for {} seqs'.format(psutil.virtual_memory()[3],Tn_counter),flush=True)
    print(("Finished Seqs processing in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
    ##########Make a DataFrame from the Sequences list and One-hot Encoding#################
    seq_array = pd.DataFrame(Tn_SEQUENCES_LIST, columns=features_list)
    memory_op.write('RAM memory % used after DF: {}'.format(psutil.virtual_memory()[3]))
    print('RAM memory % used after DF: {}'.format(psutil.virtual_memory()[3]),flush=True)
    print(("Finished DF in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
    dummyHeaders = features_list[1:]
    # add extra rows to ensure all categories (ATGC-) represented,
    # otherwise fewer columns will be created when get_dummies called
    nucs = ['A', 'C', 'G', 'T', '-']
    length_seq_lst = len(Tn_SEQUENCES_LIST[0])
    del Tn_SEQUENCES_LIST
    for i in nucs:
    	line = [i] * length_seq_lst
    	seq_array.loc[len(seq_array)] = line
    print('RAM memory used after adding ATGC: {}'.format(psutil.virtual_memory()[3]),flush=True)
    print(("Finished adding ATGC in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
    # get one-hot encoding
    seq_array = pd.get_dummies(seq_array, columns=dummyHeaders)
    print('RAM memory used after get_dummies: {}'.format(psutil.virtual_memory()[3]),flush=True)
    print(("Finished one-hot encoding in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
    # get rid of the fake data we just added
    seq_array.drop(seq_array.tail(len(nucs)).index, inplace=True)
    feature_cols = list(seq_array)
    # remove the last column from the DataFrame (the predictable values).
    seed = 1
    h = feature_cols.pop(0)
    X = seq_array[feature_cols]
    y = seq_array[h]
    print('RAM memory used after XY: {}'.format(psutil.virtual_memory()[3]),flush=True)
    print('all_y',len(list(set(y))))
    if ARGS.test_data:
        X_train,y_train = X,y
        Ts_SEQUENCES_LIST,Ts_order_list, Ts_counter = process_aln_file(ARGS.test_data,memory_op,'y')
        seq_array_ts = pd.DataFrame(Ts_SEQUENCES_LIST, columns=features_list)
        memory_op.write('RAM memory % used after DF: {}'.format(psutil.virtual_memory()[3]))
        print('RAM memory % used after DF: {}'.format(psutil.virtual_memory()[3]),flush=True)
        print(("Finished DF in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
        dummyHeaders_ts = features_list[1:]
        # add extra rows to ensure all categories (ATGC-) represented,
        # otherwise fewer columns will be created when get_dummies called
        nucs = ['A', 'C', 'G', 'T', '-']
        length_seq_lst_ts = len(Ts_SEQUENCES_LIST[0])
        del Ts_SEQUENCES_LIST
        for i in nucs:
        	line = [i] * length_seq_lst_ts
        	seq_array_ts.loc[len(seq_array_ts)] = line
        print('RAM memory used after adding ATGC: {}'.format(psutil.virtual_memory()[3]),flush=True)
        print(("Finished adding ATGC in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
        # get one-hot encoding
        seq_array_ts = pd.get_dummies(seq_array_ts, columns=dummyHeaders_ts)
        print('RAM memory used after get_dummies: {}'.format(psutil.virtual_memory()[3]),flush=True)
        print(("Finished one-hot encoding in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
        seq_array_ts.drop(seq_array_ts.tail(len(nucs)).index, inplace=True)
        feature_cols_ts = list(seq_array_ts)
        h_ts = feature_cols_ts.pop(0)
        X_test = seq_array_ts[feature_cols_ts]
        y_test = seq_array_ts[h_ts]
    else:
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=testing_Percent,random_state=seed)
    data_pickled = 'Training_data_{}.pickle'.format(TIMESTR)
    with open(data_pickled,"wb") as f:
        pickle.dump(X_train, f)
        pickle.dump(X_test, f)
        pickle.dump(y_train, f)
        pickle.dump(y_test, f)
    print('RAM memory used after Train_test split: {}'.format(psutil.virtual_memory()[3]),flush=True)
    print('train_y',len(list(set(y_train))))
    print('test_y',len(list(set(y_test))))
    print(("Finished preparing the sequences in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
    print("#########################################")
    OUTPUT_OBJECT.write('all_y: {}\n'.format(len(list(set(y)))))
    OUTPUT_OBJECT.write('train_y: {}\n'.format(len(list(set(y_train)))))
    OUTPUT_OBJECT.write('test_y: {}\n'.format(len(list(set(y_test)))))
    OUTPUT_OBJECT.write('Finished preparing the sequences in --- {:.3f} seconds ---\n'.format(time.time() - START_TIME))
    OUTPUT_OBJECT.write("#########################################\n")
elif '.pickle' in aln_file:
    seed = 1
    with open(aln_file, "rb") as f:
        X_train = pickle.load(f)
        X_test = pickle.load(f)
        y_train = pickle.load(f)
        y_test = pickle.load(f)
    print('train_y',len(list(set(y_train))),flush=True)
    print('test_y',len(list(set(y_test))),flush=True)
    OUTPUT_OBJECT.write('train_y: {}\n'.format(len(list(set(y_train)))))
    OUTPUT_OBJECT.write('test_y: {}\n'.format(len(list(set(y_test)))))
    print(("Finished preparing the sequences in --- {:.3f} seconds ---".format(time.time() - START_TIME)),flush=True)
################Classifier Training and cross validation##################
scoring = 'accuracy'
# Define models to train
'''
names = ["Random Forest2_400_s7","Random Forest10","Random Forest5",
"Random Forest5_400_s7","Random Forest4_400_s4","Random Forest10_300_s4",
"Random Forest10_200_s4","Random Forest20_200_s4",]
#names = ["Decision Tree","Random Forest", "Neural Net",
#            "SVM RBF", 'Logistic Regression']
'RandomForestClassifier(n_estimators=10,n_jobs=10)'
#classifiers = [RandomForestClassifier(n_estimators=2,max_depth=400,n_jobs=2,min_samples_split=7)]
classifiers = [RandomForestClassifier(n_estimators=2,max_depth=400,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=10,n_jobs=2),RandomForestClassifier(n_estimators=5,n_jobs=2),
RandomForestClassifier(n_estimators=5,max_depth=400,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=4,max_depth=400,n_jobs=2,min_samples_split=4),
RandomForestClassifier(n_estimators=10,max_depth=300,n_jobs=2,min_samples_split=4),
RandomForestClassifier(n_estimators=10,max_depth=200,n_jobs=2,min_samples_split=4),
RandomForestClassifier(n_estimators=20,max_depth=200,n_jobs=2,min_samples_split=4)]

names = ["Random Forest2_200_s7","Random Forest2_300_s7","Random Forest2_400_s7",
"Random Forest2_500_s7","Random Forest2_300_s2","Random Forest2_300_s4",
"Random Forest2_300_s7","Random Forest2_200_s10",]
classifiers = [
RandomForestClassifier(n_estimators=2,max_depth=200,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=2,max_depth=300,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=2,max_depth=400,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=2,max_depth=500,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=2,max_depth=300,n_jobs=2,min_samples_split=2),
RandomForestClassifier(n_estimators=2,max_depth=300,n_jobs=2,min_samples_split=4),
RandomForestClassifier(n_estimators=2,max_depth=300,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=2,max_depth=200,n_jobs=2,min_samples_split=10)
]'''
names = ["Random Forest100_20_s2","Random Forest100_20_s7","Random Forest100_50_s2",
"Random Forest100_50_s7","Random Forest100_100_s2","Random Forest100_100_s7",
"Random Forest50_50_s2","Random Forest50_50_s7",]
classifiers = [
RandomForestClassifier(n_estimators=100,max_depth=20,n_jobs=2,min_samples_split=2),
RandomForestClassifier(n_estimators=100,max_depth=20,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=100,max_depth=50,n_jobs=2,min_samples_split=2),
RandomForestClassifier(n_estimators=100,max_depth=50,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=100,max_depth=100,n_jobs=2,min_samples_split=2),
RandomForestClassifier(n_estimators=100,max_depth=100,n_jobs=2,min_samples_split=7),
RandomForestClassifier(n_estimators=50,max_depth=50,n_jobs=2,min_samples_split=2),
RandomForestClassifier(n_estimators=50,max_depth=50,n_jobs=2,min_samples_split=7)
]
#classifiers = [
#    DecisionTreeClassifier(),
#    RandomForestClassifier(n_estimators=10,n_jobs=10),
#    MLPClassifier(alpha=1),
#    SVC(kernel = 'rbf'),
#    LogisticRegression(multi_class='multinomial',max_iter=200)]

# evaluate each model in turn

models = zip(names, classifiers)
for name, model in models:
    START_TIME = time.time()
    print('RAM memory used before Training: {}'.format(psutil.virtual_memory()[3]),flush=True)
    if ARGS.cross_val:
        kfold = model_selection.StratifiedKFold(n_splits = 5)#, random_state =seed
        print('RAM memory used before CV: {}'.format(psutil.virtual_memory()[3]),flush=True)
        cv_results = model_selection.cross_val_score(model, X_train, y_train, cv = kfold, n_jobs=1,pre_dispatch=2,scoring = scoring)
        msg = '{0}: {1} ({2})\n'.format(name, cv_results.mean(), cv_results.std())
        print(msg,flush=True)
        OUTPUT_OBJECT.write(msg)
        print('RAM memory used after CV: {}'.format(psutil.virtual_memory()[3]),flush=True)
        print("Validating on test data set",flush=True)
    model.fit(X_train, y_train)
    print('RAM memory used after model fit: {}'.format(psutil.virtual_memory()[3]),flush=True)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)
    name_no_space = name.replace(' ','')
    model_joblib = "GNUVIDML_{}_{}_uncomp.joblib".format(name_no_space,TIMESTR)
    joblib.dump(model, model_joblib, compress=0)
    model_joblib = "GNUVIDML_{}_{}.joblib".format(name_no_space,TIMESTR)
    joblib.dump(model, model_joblib, compress=9)
    print('RAM memory used after prediction: {}'.format(psutil.virtual_memory()[3]),flush=True)
    #print("Confusion Matrix Classification report")
    #print(metrics.classification_report(y_test, y_pred, digits=3),flush=True)
    recall_0 =  set(y_test) - set(y_pred)
    print('CCs with Zero Recall {}'.format(len(recall_0)),flush=True)
    OUTPUT_OBJECT.write(metrics.classification_report(y_test, y_pred, digits=3))
    OUTPUT_OBJECT.write('CCs with Zero Recall {} {}\n'.format(len(recall_0),(set(y_test) - set(y_pred))))
    print("Overall Stats",flush=True)
    print("accuracy: " + str(accuracy_score(y_test, y_pred)),flush=True)
    print("f1 score: " + str(f1_score(y_test, y_pred, average="macro")),flush=True)
    print("precision: " + str(precision_score(y_test, y_pred, average="macro")),flush=True)
    print("recall: " + str(recall_score(y_test, y_pred, average="macro")),flush=True)
    print("Matthews correlation coefficient (MCC): " + str(metrics.matthews_corrcoef(y_test, y_pred)),flush=True)
    try:
        print("ROC_AUC_weighted: " + str(metrics.roc_auc_score(y_test, y_prob, average="weighted",multi_class='ovr')),flush=True)
        print("ROC_AUC_macro: " + str(metrics.roc_auc_score(y_test, y_prob, average="macro",multi_class='ovr')),flush=True)
    except:
        print('could not calculate AUC',flush=True)
    OUTPUT_OBJECT.write("Overall Stats\n")
    OUTPUT_OBJECT.write("accuracy: " + str(accuracy_score(y_test, y_pred))+ '\n')
    OUTPUT_OBJECT.write("f1 score: " + str(f1_score(y_test, y_pred, average="macro"))+ '\n')
    OUTPUT_OBJECT.write("precision: " + str(precision_score(y_test, y_pred, average="macro"))+ '\n')
    OUTPUT_OBJECT.write("recall: " + str(recall_score(y_test, y_pred, average="macro"))+ '\n')
    OUTPUT_OBJECT.write("Matthews correlation coefficient (MCC): " + str(metrics.matthews_corrcoef(y_test, y_pred))+ '\n')
    try:
        OUTPUT_OBJECT.write("ROC_AUC_weighted: " + str(metrics.roc_auc_score(y_test, y_prob, average="weighted",multi_class='ovr'))+ '\n')
        OUTPUT_OBJECT.write("ROC_AUC_macro: " + str(metrics.roc_auc_score(y_test, y_prob, average="macro",multi_class='ovr'))+ '\n')
    except:
        print('could not calculate AUC',flush=True)
    print(("Finished {} in --- {:.3f} seconds ---".format(name,time.time() - START_TIME)),flush=True)
    OUTPUT_OBJECT.write("Finished {} in --- {:.3f} seconds ---\n###########################\n".format(name,time.time() - START_TIME))
    print("#########################################")
OUTPUT_OBJECT.close()

'''
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.experimental import enable_halving_search_cv  # noqa
from sklearn.model_selection import HalvingGridSearchCV
from sklearn import datasets
base_estimator = RandomForestClassifier(random_state=0)
random_grid = {'max_depth': [300, 400, 500],
 'min_samples_leaf': [1, 2, 3],
 'min_samples_split': [2, 3, 4],
 'n_estimators': [3,4,5]}
sh = HalvingGridSearchCV(base_estimator, random_grid, cv=3,factor=2,n_jobs=3).fit(X_train, y_train)
#384 288 144 72 36 18
#81,41,20
#17382 34656 69312 138624 277248
print(sh.n_resources_,flush=True)
print(sh.n_candidates_,flush=True)
print(sh.n_remaining_candidates_,flush=True)
print(sh.max_resources_,flush=True)
print(sh.min_resources_,flush=True)
print(sh.n_iterations_,flush=True)
print(sh.n_possible_iterations_,flush=True)
print(sh.n_required_iterations_,flush=True)
print(sh.best_estimator_,flush=True)
print(sh.best_score_,flush=True)
print(sh.best_params_,flush=True)
print(sh.best_index_,flush=True)
#rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,
# n_iter = 50, cv = 2, verbose=2, random_state=42, n_jobs = -1)
RFname = "Random Forest" + str(sh.best_params_['n_estimators']) + '_' + str(sh.best_params_['max_depth'])
names = [RFname]
if 'max_features' in sh.best_params_.keys():
    classifiers = [RandomForestClassifier(max_depth=sh.best_params_['max_depth'],
    min_samples_leaf= sh.best_params_['min_samples_leaf'],min_samples_split=sh.best_params_['min_samples_split'],
    n_estimators=sh.best_params_['n_estimators'],max_features=sh.best_params_['max_features'])]
else:
    classifiers = [RandomForestClassifier(max_depth=sh.best_params_['max_depth'],
    min_samples_leaf= sh.best_params_['min_samples_leaf'],min_samples_split=sh.best_params_['min_samples_split'],
    n_estimators=sh.best_params_['n_estimators'])]

y_pred = sh.best_estimator_.predict(X_test)
y_prob = sh.best_estimator_.predict_proba(X_test)
name_no_space = names[0].replace(' ','')
model_joblib = "GNUVIDML_{}_{}.joblib".format(name_no_space,TIMESTR)
joblib.dump(sh.best_estimator_, model_joblib, compress=0)
print("Confusion Matrix Classification report",flush=True)
print(metrics.classification_report(y_test, y_pred, digits=3),flush=True)
recall_0 =  set(y_test) - set(y_pred)
print('CCs with Zero Recall {}'.format(len(recall_0)),recall_0,flush=True)
OUTPUT_OBJECT.write(metrics.classification_report(y_test, y_pred, digits=3))
OUTPUT_OBJECT.write('CCs with Zero Recall {}\n'.format(set(y_test) - set(y_pred)))
print("Overall Stats",flush=True)
print("accuracy: " + str(accuracy_score(y_test, y_pred)),flush=True)
print("f1 score: " + str(f1_score(y_test, y_pred, average="macro")),flush=True)
print("precision: " + str(precision_score(y_test, y_pred, average="macro")),flush=True)
print("recall: " + str(recall_score(y_test, y_pred, average="macro")),flush=True)
print("Matthews correlation coefficient (MCC): " + str(metrics.matthews_corrcoef(y_test, y_pred)),flush=True)
try:
    print("ROC_AUC_weighted: " + str(metrics.roc_auc_score(y_test, y_prob, average="weighted",multi_class='ovr')),flush=True)
    print("ROC_AUC_macro: " + str(metrics.roc_auc_score(y_test, y_prob, average="macro",multi_class='ovr')),flush=True)
except:
    print('could not calculate AUC',flush=True)
OUTPUT_OBJECT.write("Overall Stats\n")
OUTPUT_OBJECT.write("accuracy: " + str(accuracy_score(y_test, y_pred))+ '\n')
OUTPUT_OBJECT.write("f1 score: " + str(f1_score(y_test, y_pred, average="macro"))+ '\n')
OUTPUT_OBJECT.write("precision: " + str(precision_score(y_test, y_pred, average="macro"))+ '\n')
OUTPUT_OBJECT.write("recall: " + str(recall_score(y_test, y_pred, average="macro"))+ '\n')
OUTPUT_OBJECT.write("Matthews correlation coefficient (MCC): " + str(metrics.matthews_corrcoef(y_test, y_pred))+ '\n')
try:
    OUTPUT_OBJECT.write("ROC_AUC_weighted: " + str(metrics.roc_auc_score(y_test, y_prob, average="weighted",multi_class='ovr'))+ '\n')
    OUTPUT_OBJECT.write("ROC_AUC_macro: " + str(metrics.roc_auc_score(y_test, y_prob, average="macro",multi_class='ovr'))+ '\n')
except:
    print('could not calculate AUC',flush=True)
print(("Finished {} in --- {:.3f} seconds ---".format(names[0],time.time() - START_TIME)),flush=True)
OUTPUT_OBJECT.write("Finished {} in --- {:.3f} seconds ---\n###########################\n".format(names[0],time.time() - START_TIME))
print("#########################################")
OUTPUT_OBJECT.close()'''

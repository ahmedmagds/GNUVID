#!/usr/bin/env python3
import os
import sys
import argparse
import joblib
import pandas as pd
import time
from sklearn.datasets import make_classification
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix, make_scorer
from sklearn.model_selection import cross_val_score
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
testing_Percent = float(sys.argv[1]) #training/testing percent
seq_file = sys.argv[2] #sequence file
SEQ_OBJECT = open(seq_file,'r')
VCF_file = sys.argv[3] # has the nucleotide(feature) positions
VCF_OBJECT = open(VCF_file,'r')
##############################
TIMESTR = time.strftime("%Y%m%d_%H%M")
FO_name = 'GNUVIDML_report_' + TIMESTR + '.txt'
OUTPUT_OBJECT = open(FO_name,'w')
START_TIME = time.time()
features_list = []
for line in VCF_OBJECT:
    if '#' not in line:
        features_list.append(line.split()[1])
features_list.insert(0, 'CC')
print('Features ',len(features_list)-1)
OUTPUT_OBJECT.write('Features {}\n'.format(len(features_list)-1))
###########Parse the alignment file and produce a list of the 15136 features#########
SEQUENCES_LIST = []
order_list = []
SEQUENCE_STRING = ''
for line in SEQ_OBJECT:
    line = line.rstrip()
    if line.startswith(">"):
        if (len(SEQUENCE_STRING) > 0):
            if SEQUENCE_INFO.split('_CC')[-1] != 'NA':
                lst = list(SEQUENCE_STRING)
                lst.insert(0,SEQUENCE_INFO.split('_CC')[-1])
                SEQUENCES_LIST.append(lst)
            SEQUENCE_STRING = ""
        SEQUENCE_INFO = line.lstrip(">")
        order_list.append(SEQUENCE_INFO)
    else:
        SEQUENCE_STRING += line
if SEQUENCE_INFO.split('_CC')[-1] != 'NA':
    lst = list(SEQUENCE_STRING)
    lst.insert(0,SEQUENCE_INFO.split('_CC')[-1])
    SEQUENCES_LIST.append(lst)
SEQ_OBJECT.close()
print('Genome in aln: ',len(order_list))
print('Genome included: ',len(SEQUENCES_LIST))
OUTPUT_OBJECT.write('Genome in aln: {}\n'.format(len(order_list)))
OUTPUT_OBJECT.write('Genome included: {}\n'.format(len(SEQUENCES_LIST)))
##########Make a DataFrame from the Sequences list and One-hot Encoding#################
seq_array = pd.DataFrame(SEQUENCES_LIST, columns=features_list)
dummyHeaders = features_list[1:]
# add extra rows to ensure all categories (ATGC-) represented,
# otherwise fewer columns will be created when get_dummies called
nucs = ['A', 'C', 'G', 'T', '-']
for i in nucs:
	line = [i] * len(SEQUENCES_LIST[0])
	seq_array.loc[len(seq_array)] = line
# get one-hot encoding
seq_array = pd.get_dummies(seq_array, columns=dummyHeaders)
# get rid of the fake data we just added
seq_array.drop(seq_array.tail(len(nucs)).index, inplace=True)
feature_cols = list(seq_array)
# remove the last column from the DataFrame (the predictable values).
seed = 1
h = feature_cols.pop(0)
X = seq_array[feature_cols]
y = seq_array[h]
print('all_y',len(list(set(y))))
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=testing_Percent,random_state=seed)
print('train_y',len(list(set(y_train))))
print('test_y',len(list(set(y_test))))
print(("Finished preparing the sequences in --- {:.3f} seconds ---".format(time.time() - START_TIME)))
print("#########################################")
OUTPUT_OBJECT.write('all_y: {}\n'.format(len(list(set(y)))))
OUTPUT_OBJECT.write('train_y: {}\n'.format(len(list(set(y_train)))))
OUTPUT_OBJECT.write('test_y: {}\n'.format(len(list(set(y_test)))))
OUTPUT_OBJECT.write('Finished preparing the sequences in --- {:.3f} seconds ---\n'.format(time.time() - START_TIME))
OUTPUT_OBJECT.write("#########################################\n")
################Classifier Training and cross validation##################
scoring = 'accuracy'
# Define models to train
names = ["Random Forest"]
#names = ["Decision Tree","Random Forest", "Neural Net",
#            "SVM RBF", 'Logistic Regression']
classifiers = [RandomForestClassifier(n_estimators=10,n_jobs=10)]
#classifiers = [
#    DecisionTreeClassifier(),
#    RandomForestClassifier(n_estimators=10,n_jobs=10),
#    MLPClassifier(alpha=1),
#    SVC(kernel = 'rbf'),
#    LogisticRegression(multi_class='multinomial',max_iter=200)]
models = zip(names, classifiers)
# evaluate each model in turn
for name, model in models:
    START_TIME = time.time()
    kfold = model_selection.KFold(n_splits = 5, random_state =seed)
    cv_results = model_selection.cross_val_score(model, X_train, y_train, cv = kfold, n_jobs=20,scoring = scoring)
    msg = '{0}: {1} ({2})\n'.format(name, cv_results.mean(), cv_results.std())
    print(msg)
    OUTPUT_OBJECT.write(msg)
    print("Validating on test data set")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Confusion Matrix Classification report")
    print(metrics.classification_report(y_test, y_pred, digits=3))
    OUTPUT_OBJECT.write(metrics.classification_report(y_test, y_pred, digits=3))
    print("Overall Stats")
    print("accuracy: " + str(accuracy_score(y_test, y_pred)))
    print("f1 score: " + str(f1_score(y_test, y_pred, average="macro")))
    print("precision: " + str(precision_score(y_test, y_pred, average="macro")))
    print("recall: " + str(recall_score(y_test, y_pred, average="macro")))
    OUTPUT_OBJECT.write("Overall Stats\n")
    OUTPUT_OBJECT.write("accuracy: " + str(accuracy_score(y_test, y_pred))+ '\n')
    OUTPUT_OBJECT.write("f1 score: " + str(f1_score(y_test, y_pred, average="macro"))+ '\n')
    OUTPUT_OBJECT.write("precision: " + str(precision_score(y_test, y_pred, average="macro"))+ '\n')
    OUTPUT_OBJECT.write("recall: " + str(recall_score(y_test, y_pred, average="macro"))+ '\n')
    name_no_space = name.replace(' ','')
    model_joblib = "GNUVIDML_{}.joblib".format(name_no_space)
    joblib.dump(model, model_joblib, compress=9)
    print(("Finished {} in --- {:.3f} seconds ---".format(name,time.time() - START_TIME)))
    OUTPUT_OBJECT.write("Finished {} in --- {:.3f} seconds ---\n###########################\n".format(name,time.time() - START_TIME))
    print("#########################################")
OUTPUT_OBJECT.close()

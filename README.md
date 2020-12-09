[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ahmedmagds/GNUVID.svg?branch=master)](https://travis-ci.org/ahmedmagds/GNUVID)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3927063.svg)](https://doi.org/10.5281/zenodo.3927063)
# GNUVID
**G**ene **N**ovelty **U**nit-based **V**irus **ID**entification for **SARS-CoV-2**
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It was created to type SARS-CoV-2 genomes using a whole genome multilocus sequence typing (wgMLST) approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assigns allele numbers to each of the 10 ORFs and a Sequence Type (ST) to each genome, based on its profile of unique gene allele sequences. It is based on our recent panallelome approach implemented in [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU). It can type your query genome in seconds. As of GNUVID 1.5, GNUVID_Predict.py is a speedy algorithm for assigning Clonal Complexes to new genomes, which uses a Machine Learning Random Forest Classifier.<br/>

A pre-print of the paper **Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread** can be found here: https://www.biorxiv.org/content/10.1101/2020.06.08.139055v1

A table of acknowledgements for the 69686 GISAID SARS-CoV-2 sequences used here is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_06_17_00.xls
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_acknowledgement_table_2020_10_22_16-merged.pdf

## Globally circulating clonal complexes as  of 2020-10-20:

- 69686 GISAID sequences have been included in this analysis.

- GNUVID compressed the 696860 ORFs in the 69686 genomes to 37921 unique alleles.

- 35010 Sequence Types (STs) have been assigned in this dataset and were clustered in 154 clonal complexes (CCs).

- 84 new CCs have been assigned.

- 94 CCs have been Inactive (i.e. Last time seen more than 1 month before 2020-10-20).

- 26 CCs have gone Quiet (i.e. Last seen 2-4 weeks before 2020-10-20).

- 34 CCs have been Active (i.e. Last seen within the 2 weeks before 2020-10-20).

- CC70, CC26, CC343, CC439, CC927, CC1434, CC11290, CC13202, CC13669 and CC17244 have now been called CC550, CC750, CC9999, CC2649, CC1179, CC2175, CC18372, CC13208, CC12995 and CC13413 respectively.


**Minimum spanning tree of the 35010 STs showing the 154 CCs**

![Image of CCs](https://github.com/ahmedmagds/GNUVID/blob/master/db/MST_10202020.png)

The 34 Active CCs are in red. The pie charts show the percentage distribution of genomes from the different geographic regions in each CC.

**The table below shows summary information of the 34 Active Clonal Complexes (CCs). A full list for the 154 CCs (including inactive and quiet) can be found [here](https://github.com/ahmedmagds/GNUVID/tree/master/db)**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex. Starting from the DB update (10/20/2020), **the ten defining SNPs (C241,C3037,A23403,C8782,G11083,G25563,G26144,T28144,G28882,C22227)** for the seven GISAID clades are reported for each CC for easier correlation between the two systems.


| Clonal Complex | Number of STs | Number of isolates | Most common 5 countries | Most common Region | Date range | Status | Defining SNPs | GISAID Clade |
|----------------|---------------|--------------------|-------------------------|--------------------|------------|--------|---------------|--------------|
| **300** | 4577 | 9266 | United Kingdom (47%), USA (15%), Portugal (5%), Australia (4%), Russia (3%) | Europe (67%) | 2020-01-24 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **317** | 144 | 393 | Japan (34%), USA (23%), United Kingdom (16%), Spain (4%), Switzerland (4%) | Asia (41%) | 2020-02-26 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **399** | 275 | 630 | United Kingdom (59%), Peru (11%), Canada (6%), Belgium (4%), Italy (3%) | Europe (74%) | 2020-03-02 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **498** | 343 | 707 | United Kingdom (45%), USA (42%), Switzerland (3%), Canada (2%), Spain (1%) | Europe (53%) | 2020-03-05 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **3859** | 79 | 260 | United Kingdom (98%), Norway (2%) | Europe (100%) | 2020-04-13 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **5447** | 343 | 609 | United Kingdom (62%), India (24%), Saudi Arabia (7%), Netherlands (1%), Ireland (1%) | Europe (66%) | 2020-02-16 to 2020-10-11 | **Active** | TTGCGTGTGC | GH |
| **20544** | 30 | 98 | United Kingdom (100%) | Europe (100%) | 2020-05-05 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| **21976** | 52 | 93 | United Kingdom (58%), South Africa (32%), India (8%), USA (2%) | Europe (58%) | 2020-05-21 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **23107** | 47 | 141 | United Kingdom (100%) | Europe (100%) | 2020-06-15 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **25545** | 92 | 198 | United Kingdom (72%), Belgium (22%), Netherlands (2%), France (2%), Germany (2%) | Europe (100%) | 2020-07-09 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **25780** | 20 | 58 | United Kingdom (95%), New Zealand (3%), USA (2%) | Europe (95%) | 2020-04-06 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| **26377** | 231 | 643 | United Kingdom (95%), Spain (2%), Netherlands (2%), Ireland (1%), Switzerland (0%) | Europe (100%) | 2020-07-18 to 2020-10-13 | **Active** | TTGCGGGTGT | GV |
| **26711** | 234 | 629 | United Kingdom (100%) | Europe (100%) | 2020-07-21 to 2020-10-08 | **Active** | TTGCTGGTAC | Not Applicaple |
| **26754** | 119 | 284 | United Kingdom (74%), Norway (21%), Netherlands (1%), Spain (1%), France (1%) | Europe (100%) | 2020-06-20 to 2020-10-11 | **Active** | TTGCGGGTGT | GV |
| **27413** | 52 | 232 | United Kingdom (100%) | Europe (100%) | 2020-07-28 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **27693** | 387 | 1102 | United Kingdom (99%), Netherlands (0%), Spain (0%), Ireland (0%), France (0%) | Europe (100%) | 2020-07-31 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| **27700** | 65 | 161 | United Kingdom (99%), Norway (1%) | Europe (100%) | 2020-07-31 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **27950** | 61 | 174 | United Kingdom (97%), Netherlands (2%), New Zealand (1%) | Europe (99%) | 2020-08-04 to 2020-10-08 | **Active** | TTGCGGGTGT | GV |
| **28012** | 67 | 202 | United Kingdom (100%) | Europe (100%) | 2020-08-04 to 2020-10-06 | **Active** | TTGCGGGTGT | GV |
| **28179** | 253 | 632 | United Kingdom (100%) | Europe (100%) | 2020-06-02 to 2020-10-10 | **Active** | TTGCGGGTAC | GR |
| **28445** | 104 | 309 | United Kingdom (89%), Norway (9%), Netherlands (1%), France (0%), Sweden (0%) | Europe (100%) | 2020-08-08 to 2020-10-08 | **Active** | TTGCGTGTGC | GH |
| **28513** | 46 | 120 | United Kingdom (99%), Australia (1%) | Europe (99%) | 2020-03-24 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **28786** | 73 | 165 | United Kingdom (100%) | Europe (100%) | 2020-08-11 to 2020-10-08 | **Active** | TTGCGGGTGC | G |
| **29310** | 24 | 71 | United Kingdom (99%), Ireland (1%) | Europe (100%) | 2020-08-17 to 2020-10-07 | **Active** | TTGCGGGTGT | GV |
| **29516** | 37 | 117 | United Kingdom (99%), Netherlands (1%) | Europe (100%) | 2020-08-19 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| **29952** | 39 | 107 | United Kingdom (100%) | Europe (100%) | 2020-06-08 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **30174** | 61 | 140 | United Kingdom (98%), Bangladesh (1%), Russia (1%) | Europe (99%) | 2020-07-10 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **30362** | 29 | 116 | United Kingdom (100%) | Europe (100%) | 2020-08-27 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| **30431** | 30 | 65 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-10-06 | **Active** | TTGCGGGTAT | Not Applicaple |
| **30498** | 29 | 85 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-10-06 | **Active** | TTGCTGGTAC | Not Applicaple |
| **30499** | 37 | 93 | United Kingdom (100%) | Europe (100%) | 2020-07-17 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **31179** | 216 | 606 | United Kingdom (100%), Spain (0%) | Europe (100%) | 2020-09-01 to 2020-10-09 | **Active** | TTGCGGGTGT | GV |
| **31744** | 78 | 177 | United Kingdom (100%) | Europe (100%) | 2020-09-08 to 2020-10-09 | **Active** | TTGCGGGTGT | GV |
| **31942** | 79 | 236 | United Kingdom (100%) | Europe (100%) | 2020-09-02 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |

***The ten defining SNPs in order (C241,C3037,A23403,C8782,G11083,G25563,G26144,T28144,G28882,C22227)**

## Installation
### Dependencies
* [Python3.x](https://www.python.org/downloads/)
* [Blastn](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
* [MAFFT](https://mafft.cbrc.jp/alignment/software/source.html)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [scikit-learn](https://scikit-learn.org/stable/install.html)
### Clone the Github repository
GNUVID is a command-line application written in Python3. Simply download and use! **You will have to install dependencies!**
```
$git clone https://github.com/ahmedmagds/GNUVID
$cd GNUVID/bin
$chmod +x *.py
$pwd
#pwd will give you a path/to/folder/having/GNUVID which you will use in next command
$export PATH=$PATH:/path/to/folder/having/GNUVID/bin
```
If you need it permanently, you can add this last line to your .bashrc or .bash_profile.

### Test
* Type GNUVID_Predict.py -h and it should output help screen.
* Type GNUVID_Predict.py -v and you should see an output like GNUVID.py 1.5.

## Usage for GNUVID_Predict.py
### Input
1. Query whole genome FASTA file (.fna) (it can have multiple genomes as separate FASTA records).
### Simple
**GNUVID_Predict.py will use exact matching to identify alleles of the 10 ORFs. If any novelty or ambiguity seen, Random Forest Classifier is used to classify your new genome to one of the Clonal complexes (CC))**
```
$GNUVID_Predict.py new_genomes.fasta
```
### Use with more options
```
$GNUVID_Predict.py -i -o new_genomes_GNUVID new_genomes.fasta
```
### Command line options
```
usage: GNUVID_Predict.py [-h] [-o OUTPUT_FOLDER] [-i] [-f] [-q] [-v] query_fna

GNUVID v1.5 uses the natural variation in public genomes of SARS-CoV-2 to rank
gene sequences based on the number of observed exact matches (the GNU score)
in all known genomes of SARS-CoV-2. It assigns a sequence type to each genome
based on its profile of unique gene allele sequences. It can type (using whole
genome multilocus sequence typing; wgMLST) your query genome in seconds.
GNUVID_Predict is a speedy algorithm for assigning Clonal Complexes to new
genomes, which uses machine learning Random Forest Classifier, implemented as
of GNUVID 1.5.

positional arguments:
  query_fna             Query Whole Genome Nucleotide FASTA file to analyze
                        (.fna)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Output folder and prefix to be created for results
                        (default: timestamped GNUVID_results in the current
                        directory)
  -i, --individual      Individual Output file for each genome showing the
                        allele sequence and GNU score for each gene allele
  -f, --force           Force overwriting existing results folder assigned
                        with -o (default: off)
  -q, --quiet           No screen output [default OFF]
  -v, --version         print version and exit
```
### Output
#### Always
**GNUVID_results_date_time.csv** (csv file, specify different name using -o option)

Sequence ID | GNUVID DB Version | ORF1ab | Surface_glycoprotein | ORF3a | Envelope_protein | Membrane_glycoprotein | ORF6 | ORF7a | ORF8 | Nucleocapsid_phosphoprotein | ORF10 | Exact ST | First Country seen | First date seen | Last country seen | Last date seen | CC | probability |
----------- | ----------------- | ------ | -------------------- | ----- | ---------------- | --------------------- | ---- | ----- | ---- | --------------------------- | ----- | -------- | ------------------ | --------------- | ----------------- | -------------- | -- | -----------  |
isolate_x | 10/20/20 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | China | 2019-12-30 | India | 2020-08-12 | 4 | Exact |
isolate_y | 10/20/20 | Novel | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Novel | NA | NA | NA | NA | 4 | 0.9 |
isolate_z | 10/20/20 | None | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | None | NA | NA | NA | NA | 4 | 0.8 |

* Column 1: Query Sequence name
* Column 2: GNUVID Database version (results will vary as more genomes are added to the DB)
* Columns 3-12: The allele numbers for the 10 ORFs (If None, it means the allele was not seen in the database but has degenerate bases (N) so cannot be called novel)
* Column 13: ST
* Column 14: First Country where the ST was seen (only if exact)
* Column 15: First Date when the ST was seen (only if exact)
* Column 16: Last Country where the ST was seen (only if exact)
* Column 17: Last Date when the ST was seen (only if exact)
* Column 18: Clonal Complex (CC) assigned
* Column 19: Probability of the assignment (if exact, it means this is an exact match to a previous genome in the database)<br/>

**GNUVID_date_time.log** (Log file, e.g. GNUVID_20200607_170457.log)

#### Optional with -i
**Genome1.csv** (csv output file)
GNUVID DB Version
Query Gene | GNUVID DB Version | GNU score | length | sequence | Ns count | Allele number | First date seen | Last date seen |
---------- | ----------------- | --------- | ------ | -------- | -------- | ------------- | --------------- | -------------- |
isolate_x_ORF1ab | 10/20/20 | 2000 | 21290 | ATGTAA | 0 | 1 | 2019-12-24 | 2020-05-04 |
isolate_x_ORF10 | 10/20/20 | 0 | 117 | ATGTAA | 0 | Novel | NA | NA |

* Column 1: Query Gene name
* Column 2: GNUVID Database version (results will vary as more genomes are added to the DB
* Column 3: GNU score (number of exact matches in the database, GNU=0 novel allele never seen before)
* Column 4: Query gene sequence length
* Column 5: Gene sequence
* Column 6: Number of Ns and degenerate bases in the query gene sequence
* Column 7: Alelle number from the database (If None, it means the allele was not seen in the database but has degenerate bases (N) so cannot be called novel)
* Column 8: First date this allele was seen (NA if novel)
* Column 9: Last date this allele was seen (NA if novel)<br/>

Note: This report should have 10 rows for the ORFs. It will be produced for each genome. It is valuable if you interested to know more about each ORF allele and how many times it was seen globally (GNU score) and when it was first- and last- time seen.

**Instructions for how to use GNUVID.py for compression and classification [here](https://github.com/ahmedmagds/GNUVID/tree/master/bin)**

## Bugs
Please submit via the GitHub issues page: https://github.com/ahmedmagds/GNUVID/issues
## Software Licence
GPLv3: https://github.com/ahmedmagds/GNUVID/blob/master/LICENSE
## Source Data
The data used in GNUVID is from GISAID, but sequences were anonymized to fit with guidelines. Appropriate acknowledgements for the labs that provided the original SARS-CoV-2 genome sequences to GISAID are also provided here<br/>
## Citations
### GNUVID
Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread<br/>
[Moustafa AM and Planet PJ 2020, bioRxiv;2020.06.08.139055](https://doi.org/10.1101/2020.06.08.139055)<br/>
### References
* [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU) 'Moustafa AM and Planet PJ 2020, Genome Biology;21:58'.
* MAFFT version 7 'Katoh and Standley 2013, Molecular Biology and Evolution;30:772-780'.
* pandas 'Reback et  al. 2020, DOI:10.5281/zenodo.3509134'.
* Scikit-learn 'Pedregosa et al. 2011, JMLR; 12:2825-2830'.
* BLAST+ 'Camacho et al. 2009, BMC Bioinformatics; 10:421'.
* GISAID 'Shu Y. and McCauley J. 2017, EuroSurveillance; 22:13'.
* The reference genome MN908947 'Wu et al. 2020, Nature; 579:265–269'.
* eBURST 'Feil et al. 2004,  Journal of Bacteriology; 186:1518'.
* goeBURST 'Francisco et al. 2009, BMC Bioinformatics; 10:152'.
* PHYLOViZ 2.0 'Nascimento et al. 2017, Bioinformatics; 33:128-129'.
## Author
Ahmed M. Moustafa: [ahmedmagds](https://github.com/ahmedmagds)<br/>
Twitter: [Ahmed_Microbes](https://twitter.com/Ahmed_Microbes)

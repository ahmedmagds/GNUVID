[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ahmedmagds/GNUVID.svg?branch=master)](https://travis-ci.org/ahmedmagds/GNUVID)
[![Anaconda_cloud](https://anaconda.org/bioconda/gnuvid/badges/version.svg)](https://anaconda.org/bioconda/gnuvid)
[![Anaconda_downloads](https://anaconda.org/bioconda/gnuvid/badges/downloads.svg)](https://anaconda.org/bioconda/gnuvid)
[![Anaconda_install](https://anaconda.org/bioconda/gnuvid/badges/installer/conda.svg)](https://anaconda.org/bioconda/gnuvid)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3927063.svg)](https://doi.org/10.5281/zenodo.4313855)
# GNUVID
**G**ene **N**ovelty **U**nit-based **V**irus **ID**entification for **SARS-CoV-2**
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It was created to type SARS-CoV-2 genomes using a whole genome multilocus sequence typing (wgMLST) approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assigns allele numbers to each of the 10 ORFs and a Sequence Type (ST) to each genome, based on its profile of unique gene allele sequences. It is based on our recent panallelome approach implemented in [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU). It can type your query genome in seconds. As of GNUVID v2.1, GNUVID_Predict.py is a speedy algorithm for assigning Clonal Complexes to new genomes, which uses a Machine Learning Random Forest Classifier.<br/>

A pre-print of the paper **Emerging SARS-CoV-2 diversity revealed by rapid whole genome sequence typing** can be found here: https://www.biorxiv.org/content/10.1101/2020.12.28.424582v1

A table of acknowledgements for the 159515 GISAID SARS-CoV-2 sequences used here is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_06_17_00.xls
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_acknowledgement_table_2021_01_06-merged.pdf

## Install and use as simple as
Make a new environment and install GNUVID in it
```
conda create -n GNUVID -c bioconda gnuvid
conda activate GNUVID
```

## Globally circulating clonal complexes as  of 2021-01-06:

- 159515 GISAID sequences have been included in this analysis.

- GNUVID compressed the 1595150 ORFs in the 159515 genomes to 89491 unique alleles.

- 81097 Sequence Types (STs) have been assigned in this dataset and were clustered in 406 clonal complexes (CCs).

- 252 new CCs have been assigned.

- 133 CCs have been Inactive (i.e. Last time seen more than 1 month before 2021-01-06).

- 209 CCs have gone Quiet (i.e. Last seen 2-4 weeks before 2021-01-06).

- 64 CCs have been Active (i.e. Last seen within the 2 weeks before 2021-01-06).

- CC70, CC26, CC343, CC439, CC927, CC1434, CC11290, CC13202, CC13669 and CC17244 have now been called CC550, CC750, CC9999, CC2649, CC1179, CC2175, CC18372, CC13208, CC12995 and CC13413 respectively.

## GNUVID now assigns genomes to the three new Variants of Concern:
- **CC81085 represents the Brazilian P.1 lineage (a.k.a. 20J/501Y.V3).**
- **CC71014 represents the South African B.1.351 lineage (a.k.a. 20H/501Y.V2).**
- **10 CCs represent the UK B.1.1.7 lineage (a.k.a. 20I/501Y.V1 Variant of Concern (VOC) 202012/01). (10 CCs: 46649, 45062, 49676, 54949, 54452, 58534, 57630, 66559, 62415 and 67441).**

**Minimum spanning tree of the 81097 STs showing the 406 CCs**

![Image of CCs](https://github.com/ahmedmagds/GNUVID/blob/master/db/MST_01062021.png)

**The table below shows summary information of the 67 Active Clonal Complexes (CCs). A full list for the 406 CCs (including inactive and quiet) can be found [here](https://github.com/ahmedmagds/GNUVID/tree/master/db)**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex. Starting from the DB update (01/06/2021), the GISAID clades are reported for each CC for easier correlation between the two systems.


| Clonal Complex | Number of STs | Number of isolates | Most common 5 countries | Most common Region | Date range | Status | Variant of Concern (%isolates) | GISAID Clade |
|----------------|---------------|--------------------|-------------------------|--------------------|------------|--------|--------------------------------|--------------|
| **81085** | 15 | 22 | Brazil (77%), Japan (18%), USA (5%) | South America (77%) | 2020-12-04 to 2021-01-18 | **Active** | P.1 (100) | GR |
| **71014** | 35 | 35 | South Africa (89%), France (3%), United Kingdom (3%), Sweden (3%), South Korea (3%) | Africa (89%) | 2020-10-22 to 2020-12-26 | **Active** | B.1.351 (100) | GH |
| **45062** | 197 | 518 | United Kingdom (98%), Portugal (1%), France (0%), Finland (0%), Italy (0%) | Europe (100%) | 2020-09-20 to 2020-12-29 | **Active** | B.1.1.7 (100) | GR |
| **46649** | 1647 | 3429 | United Kingdom (96%), Denmark (2%), Portugal (0%), Italy (0%), Finland (0%) | Europe (100%) | 2020-09-30 to 2020-12-29 | **Active** | B.1.1.7 (100) | GR |
| **49676** | 123 | 351 | United Kingdom (99%), Netherlands (1%), Pakistan (0%) | Europe (100%) | 2020-10-11 to 2020-12-25 | **Active** | B.1.1.7 (100) | GR |
| **54452** | 57 | 102 | United Kingdom (99%), Sweden (1%) | Europe (100%) | 2020-10-21 to 2020-12-28 | **Active** | B.1.1.7 (100) | GR |
| 54949 | 36 | 92 | United Kingdom (92%), Netherlands (8%) | Europe (100%) | 2020-10-22 to 2020-12-22 | Quiet | B.1.1.7 (100) | GR |
| **57630** | 222 | 484 | United Kingdom (97%), France (1%), Australia (0%), Israel (0%), Portugal (0%) | Europe (99%) | 2020-10-29 to 2020-12-28 | **Active** | B.1.1.7 (100) | GR |
| **58534** | 231 | 438 | United Kingdom (97%), France (1%), Portugal (1%), Denmark (0%), Israel (0%) | Europe (99%) | 2020-10-29 to 2020-12-28 | **Active** | B.1.1.7 (100) | GR |
| 62415 | 30 | 71 | United Kingdom (96%), USA (4%) | Europe (96%) | 2020-11-06 to 2020-12-21 | Quiet | B.1.1.7 (100) | GR |
| **66559** | 42 | 94 | United Kingdom (98%), France (1%), Italy (1%) | Europe (100%) | 2020-11-08 to 2020-12-27 | **Active** | B.1.1.7 (100) | GR |
| 67441 | 48 | 85 | United Kingdom (99%), Netherlands (1%) | Europe (100%) | 2020-11-08 to 2020-12-22 | Quiet | B.1.1.7 (100) | GR |
| **255** | 3238 | 5568 | USA (21%), United Kingdom (17%), India (8%), France (6%), Netherlands (5%) | Europe (57%) | 2020-01-24 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| **258** | 6737 | 12935 | USA (66%), Denmark (5%), United Kingdom (5%), Netherlands (4%), France (3%) | North America (69%) | 2020-02-16 to 2020-12-28 | **Active** | Not_VOC (0.007730963) | GH |
| **300** | 10460 | 17836 | United Kingdom (38%), USA (16%), Russia (4%), Denmark (4%), India (3%) | Europe (64%) | 2020-01-24 to 2020-12-28 | **Active** | Not_VOC (0) | GR |
| **333** | 158 | 396 | USA (53%), Canada (11%), France (7%), Slovenia (7%), United Kingdom (6%) | North America (63%) | 2020-02-29 to 2020-12-23 | **Active** | Not_VOC (0) | GH |
| **338** | 210 | 487 | USA (69%), Denmark (6%), Canada (5%), United Kingdom (4%), Colombia (2%) | North America (74%) | 2020-02-29 to 2020-12-24 | **Active** | Not_VOC (0) | GH |
| **399** | 856 | 1521 | United Kingdom (48%), Peru (10%), Denmark (7%), Belgium (5%), Canada (4%) | Europe (73%) | 2020-03-02 to 2020-12-29 | **Active** | Not_VOC (0) | GR |
| **498** | 305 | 586 | USA (46%), United Kingdom (31%), Denmark (5%), Mexico (4%), South Africa (2%) | North America (51%) | 2020-03-05 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| **800** | 473 | 743 | Saudi Arabia (38%), United Kingdom (21%), India (17%), Norway (5%), Indonesia (5%) | Asia (64%) | 2020-02-03 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| **1455** | 181 | 283 | United Kingdom (70%), Denmark (11%), France (6%), Ireland (5%), Italy (3%) | Europe (100%) | 2020-03-16 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| **1852** | 146 | 231 | United Kingdom (47%), USA (17%), Czech Republic (4%), Denmark (4%), Portugal (4%) | Europe (70%) | 2020-03-13 to 2020-12-24 | **Active** | Not_VOC (0) | GR |
| **4326** | 96 | 137 | Serbia (22%), Denmark (21%), Hungary (13%), North Macedonia (10%), United Kingdom (10%) | Europe (96%) | 2020-03-24 to 2020-12-28 | **Active** | Not_VOC (0) | GR |
| **6410** | 66 | 80 | USA (79%), India (6%), Sweden (5%), Israel (4%), United Kingdom (1%) | North America (80%) | 2020-03-24 to 2020-12-26 | **Active** | Not_VOC (0) | GH |
| **10221** | 371 | 578 | USA (96%), Mexico (4%), Norway (0%), South Korea (0%) | North America (100%) | 2020-03-23 to 2020-12-28 | **Active** | Not_VOC (0) | G |
| **15298** | 79 | 111 | USA (31%), India (21%), United Kingdom (20%), Australia (15%), Denmark (4%) | North America (34%) | 2020-05-06 to 2021-01-03 | **Active** | Not_VOC (0) | GR |
| **20133** | 140 | 196 | United Arab Emirates (98%), Hong Kong (1%), United Kingdom (1%) | Asia (99%) | 2020-04-24 to 2020-12-23 | **Active** | Not_VOC (0) | GR |
| **21210** | 1077 | 1609 | USA (96%), United Kingdom (1%), Denmark (1%), Australia (1%), Canada (0%) | North America (97%) | 2020-04-11 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| **25468** | 90 | 178 | Australia (53%), USA (46%), Canada (1%) | Oceania (53%) | 2020-05-21 to 2021-01-02 | **Active** | Not_VOC (0) | Not Applicaple |
| **25545** | 440 | 875 | United Kingdom (29%), Denmark (29%), Belgium (19%), Luxembourg (9%), Netherlands (4%) | Europe (99%) | 2020-07-02 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| **26377** | 1529 | 2975 | United Kingdom (57%), Denmark (32%), Spain (3%), Netherlands (2%), Luxembourg (2%) | Europe (100%) | 2020-07-18 to 2020-12-29 | **Active** | Not_VOC (0) | GV |
| **26477** | 1482 | 2384 | United Kingdom (57%), India (12%), Denmark (6%), Saudi Arabia (5%), Canada (4%) | Europe (69%) | 2020-02-16 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| **26754** | 962 | 1660 | United Kingdom (63%), Denmark (11%), Netherlands (5%), Spain (4%), Norway (4%) | Europe (100%) | 2020-06-20 to 2020-12-28 | **Active** | Not_VOC (0) | GV |
| **27324** | 86 | 148 | USA (57%), Denmark (32%), United Kingdom (8%), Netherlands (1%), Switzerland (1%) | North America (57%) | 2020-06-28 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| **27456** | 1333 | 2817 | Denmark (42%), France (15%), United Kingdom (15%), Luxembourg (15%), Netherlands (4%) | Europe (99%) | 2020-07-09 to 2020-12-29 | **Active** | Not_VOC (0) | GH |
| **27465** | 93 | 152 | Sweden (44%), Denmark (41%), Norway (7%), United Kingdom (4%), Latvia (4%) | Europe (100%) | 2020-07-06 to 2020-12-23 | **Active** | Not_VOC (0) | GR |
| **27693** | 1608 | 3705 | United Kingdom (98%), Denmark (1%), Ireland (0%), Spain (0%), Germany (0%) | Europe (100%) | 2020-03-21 to 2020-12-27 | **Active** | Not_VOC (0) | GV |
| **28179** | 64 | 197 | United Kingdom (100%) | Europe (100%) | 2020-06-11 to 2020-12-23 | **Active** | Not_VOC (0) | GR |
| **29259** | 403 | 736 | United Kingdom (54%), Denmark (12%), Netherlands (12%), Luxembourg (7%), Italy (4%) | Europe (100%) | 2020-08-05 to 2020-12-28 | **Active** | Not_VOC (0) | GV |
| **29310** | 181 | 400 | United Kingdom (95%), Ireland (5%), Sweden (0%) | Europe (100%) | 2020-08-17 to 2020-12-25 | **Active** | Not_VOC (0) | GV |
| **29368** | 63 | 81 | Portugal (68%), United Kingdom (20%), Netherlands (4%), Luxembourg (4%), Ireland (2%) | Europe (100%) | 2020-08-18 to 2020-12-28 | **Active** | Not_VOC (0) | GV |
| **29374** | 246 | 397 | USA (96%), Australia (3%), Denmark (1%), United Kingdom (1%) | North America (96%) | 2020-08-10 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| **29432** | 210 | 407 | Netherlands (40%), United Kingdom (35%), Denmark (9%), Germany (6%), Belgium (4%) | Europe (100%) | 2020-08-18 to 2020-12-27 | **Active** | Not_VOC (0) | GV |
| **29691** | 34 | 46 | USA (100%) | North America (100%) | 2020-08-21 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| **30018** | 565 | 1365 | Denmark (69%), United Kingdom (16%), Czech Republic (5%), Netherlands (3%), Sweden (2%) | Europe (100%) | 2020-05-19 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| **30071** | 72 | 120 | Luxembourg (35%), France (17%), Denmark (13%), Belgium (11%), United Kingdom (8%) | Europe (99%) | 2020-08-25 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| **30180** | 424 | 703 | Netherlands (53%), Denmark (29%), Luxembourg (7%), United Kingdom (5%), Belgium (2%) | Europe (99%) | 2020-06-11 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| **31179** | 3073 | 6050 | United Kingdom (95%), Denmark (3%), Netherlands (1%), Portugal (0%), Spain (0%) | Europe (100%) | 2020-08-09 to 2020-12-23 | **Active** | Not_VOC (0) | GV |
| **31641** | 275 | 477 | United Kingdom (69%), Denmark (20%), Germany (4%), Norway (3%), Luxembourg (1%) | Europe (99%) | 2020-09-08 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| **31744** | 868 | 2114 | United Kingdom (99%), Denmark (1%), Ireland (0%), USA (0%) | Europe (100%) | 2020-09-08 to 2020-12-24 | **Active** | Not_VOC (0) | GV |
| **32234** | 109 | 145 | USA (51%), United Kingdom (48%), Canada (1%) | North America (52%) | 2020-07-13 to 2020-12-27 | **Active** | Not_VOC (0) | GR |
| **32357** | 37 | 80 | United Kingdom (54%), Luxembourg (29%), Portugal (10%), Belgium (5%), Denmark (2%) | Europe (100%) | 2020-08-24 to 2020-12-29 | **Active** | Not_VOC (0) | G |
| **33331** | 50 | 105 | United Kingdom (99%), Netherlands (1%) | Europe (100%) | 2020-09-21 to 2020-12-25 | **Active** | Not_VOC (0) | GV |
| **33612** | 88 | 180 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-23 | **Active** | Not_VOC (0) | GV |
| **34423** | 78 | 149 | United Kingdom (100%) | Europe (100%) | 2020-09-29 to 2020-12-24 | **Active** | Not_VOC (0) | GV |
| **34933** | 210 | 400 | United Kingdom (100%), Denmark (0%), Sweden (0%) | Europe (100%) | 2020-09-10 to 2020-12-24 | **Active** | Not_VOC (0) | GV |
| **35123** | 1161 | 1796 | USA (55%), United Kingdom (28%), South Africa (4%), Mexico (3%), Denmark (2%) | North America (58%) | 2020-03-10 to 2020-12-27 | **Active** | Not_VOC (0) | G |
| **36691** | 42 | 61 | United Kingdom (34%), Russia (16%), Latvia (10%), Denmark (8%), Oman (7%) | Europe (79%) | 2020-04-10 to 2020-12-25 | **Active** | Not_VOC (0) | GR |
| **40969** | 223 | 432 | USA (100%), United Kingdom (0%) | North America (100%) | 2020-07-23 to 2020-12-29 | **Active** | Not_VOC (0) | G |
| **43400** | 48 | 98 | Malaysia (96%), Singapore (2%), Australia (2%) | Asia (98%) | 2020-09-01 to 2020-12-30 | **Active** | Not_VOC (0) | G |
| **43531** | 90 | 180 | Luxembourg (67%), Belgium (13%), France (11%), United Kingdom (3%), Italy (2%) | Europe (100%) | 2020-09-02 to 2020-12-29 | **Active** | Not_VOC (0) | GH |
| **44057** | 109 | 250 | Luxembourg (73%), Belgium (24%), Netherlands (1%), United Kingdom (1%), Portugal (0%) | Europe (100%) | 2020-09-09 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| **44837** | 82 | 139 | Luxembourg (51%), Belgium (37%), Netherlands (7%), United Kingdom (2%), Malaysia (1%) | Europe (99%) | 2020-08-01 to 2020-12-29 | **Active** | Not_VOC (0) | GV |
| **45545** | 38 | 74 | Belgium (31%), Luxembourg (30%), Netherlands (22%), United Kingdom (5%), Portugal (5%) | Europe (100%) | 2020-09-18 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| **53107** | 23 | 83 | Luxembourg (100%) | Europe (100%) | 2020-10-19 to 2020-12-27 | **Active** | Not_VOC (0) | G |
| **55253** | 53 | 103 | Luxembourg (97%), South Korea (3%) | Europe (97%) | 2020-09-30 to 2020-12-29 | **Active** | Not_VOC (0) | GV |
| **72860** | 71 | 87 | USA (97%), Australia (2%), New Zealand (1%) | North America (97%) | 2020-09-28 to 2020-12-27 | **Active** | Not_VOC (0) | GH |


## Installation
### Dependencies
* [Python3.x](https://www.python.org/downloads/)
* [Blastn](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
* [MAFFT](https://mafft.cbrc.jp/alignment/software/source.html)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [scikit-learn](https://scikit-learn.org/stable/install.html)
### Bioconda (**recommended**)
If you use Conda you can use the Bioconda channel to install it in the conda base:
Make a new environment and install GNUVID in it
```
conda create -n GNUVID -c bioconda gnuvid
conda activate GNUVID
```
The 'conda activate' command is needed to activate the GNUVID environment each time you want to use the tool.<br/>
**If you do not have Miniconda or Anaconda installed already, you can install one of them from:**
1. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. [Anaconda](https://www.anaconda.com/distribution/)

**OR**

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
* Type GNUVID_Predict.py -v and you should see an output like GNUVID.py v2.1.

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

GNUVID v2.1 uses the natural variation in public genomes of SARS-CoV-2 to rank
gene sequences based on the number of observed exact matches (the GNU score)
in all known genomes of SARS-CoV-2. It assigns a sequence type to each genome
based on its profile of unique gene allele sequences. It can type (using whole
genome multilocus sequence typing; wgMLST) your query genome in seconds.
GNUVID_Predict is a speedy algorithm for assigning Clonal Complexes to new
genomes, which uses machine learning Random Forest Classifier, implemented as
of GNUVID v2.1.

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

Sequence ID | GNUVID DB Version | ORF1ab | Surface_glycoprotein | ORF3a | Envelope_protein | Membrane_glycoprotein | ORF6 | ORF7a | ORF8 | Nucleocapsid_phosphoprotein | ORF10 | Exact ST | First Country seen | First date seen | Last country seen | Last date seen | CC | probability | Variant of Concern |
----------- | ----------------- | ------ | -------------------- | ----- | ---------------- | --------------------- | ---- | ----- | ---- | --------------------------- | ----- | -------- | ------------------ | --------------- | ----------------- | -------------- | -- | -----------  | ------------------ |
isolate_x | 10/20/20 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | China | 2019-12-30 | India | 2020-08-12 | 4 | Exact | P.1 |
isolate_y | 10/20/20 | Novel | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Novel | NA | NA | NA | NA | 4 | 0.9 | No |
isolate_z | 10/20/20 | None | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | None | NA | NA | NA | NA | 4 | 0.8 | B.1.1.7 |

* Column 1: Query Sequence name
* Column 2: GNUVID Database version (results will vary as more genomes are added to the DB)
* Columns 3-12: The allele numbers for the 10 ORFs (If None, it means the allele was not seen in the database but has degenerate bases (N) so cannot be called novel)
* Column 13: ST
* Column 14: First Country where the ST was seen (only if exact)
* Column 15: First Date when the ST was seen (only if exact)
* Column 16: Last Country where the ST was seen (only if exact)
* Column 17: Last Date when the ST was seen (only if exact)
* Column 18: Clonal Complex (CC) assigned
* Column 19: Probability of the assignment (if exact, it means this is an exact match to a previous genome in the database)
* Column 20: Variant of Concern will be reported if isolate belongs to P1, B.1.1.7 or B.1.351<br/>

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
Emerging SARS-CoV-2 diversity revealed by rapid whole genome sequence typing<br/>
[Moustafa AM and Planet PJ 2020, bioRxiv;2020.12.28.424582](https://doi.org/10.1101/2020.12.28.424582)<br/>
Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread<br/>
[Moustafa AM and Planet PJ 2020, bioRxiv;2020.06.08.139055](https://doi.org/10.1101/2020.06.08.139055)<br/>
### References
* [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU) 'Moustafa AM and Planet PJ 2020, Genome Biology;21:58'.
* MAFFT version 7 'Katoh and Standley 2013, Molecular Biology and Evolution;30:772-780'.
* pandas 'Reback et  al. 2020, DOI:10.5281/zenodo.3509134'.
* minimap2 'Li H 2018, Bioinformatics; 34:18'.
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

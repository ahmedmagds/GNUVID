[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ahmedmagds/GNUVID.svg?branch=master)](https://travis-ci.org/ahmedmagds/GNUVID)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3927063.svg)](https://doi.org/10.5281/zenodo.3927063)
# GNUVID
**G**ene **N**ovelty **U**nit-based **V**irus **ID**entification for **SARS-CoV-2**
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It was created to type SARS-CoV-2 genomes using a whole genome wgMLST approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assigns allele numbers to each of the ORFs and a Sequence Type (ST) to the genome. It is based on our recent panallelome approach implemented in [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU).<br/>

A pre-print of the paper **Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread** can be found here: https://www.biorxiv.org/content/10.1101/2020.06.08.139055v1

A table of acknowledgements for the 18298 GISAID SARS-CoV-2 sequences used here is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_06_17_00.xls
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_07_21_17.pdf

## Globally circulating clonal complexes as  of 2020-07-17:

- 25594 GISAID sequences have been included in this analysis.

- GNUVID compressed the 255940 ORFs in the 25594 genomes to 15025 unique alleles.

- 13688 Sequence Types (STs) have been assigned in this dataset and were clustered in 59 clonal complexes (CCs).

- 14 new CCs have been assigned.

- 42 CCs have been Inactive (i.e. Last time seen more than 1 month before 2020-07-17).

- 12 CCs have gone Quiet (i.e. Last seen 2-4 weeks before 2020-07-17).

- 5 CCs have been Active (i.e. Last seen within the 2 weeks before 2020-07-17).

- CC70, CC26, CC343, CC927 and CC1434 have now been called CC550, CC750, CC9999, CC1179 and CC2175 respectively.

**Minimum spanning tree of the 13688 STs showing the 59 CCs**

![Image of CCs](https://github.com/ahmedmagds/GNUVID/blob/master/db/MST_07172020.png)

The Five Active CCs are in red and the 12 Quiet CCs are in black. The pie charts show the percentage distribution of genomes from the different geographic regions in each CC.

**The table below shows summary information of the 59 Clonal Complexes (CCs).**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex. Starting from the DB update (07/17/2020), **the nine defining SNPs (C241,C3037,A23403,C8782,G11083,G25563,G26144,T28144,G28882)** for the six GISAID clades are reported for each CC for easier correlation between the two systems.


| Clonal Complex | Number of STs | Number of isolates | Most common 5 countries | Most common Region | Date range | Status | Defining SNPs* | GISAID Clade |
|----------------|---------------|--------------------|-------------------------|--------------------|------------|--------|----------------|--------------|
| 4 | 579 | 1094 | USA (21%), United Kingdom (18%), China (17%), Japan (12%), Netherlands (10%) | Asia (37%) | 2019-12-24 to 2020-05-27 | Inactive | CCACGGGTG | L |
| 16 | 21 | 29 | China (66%), Japan (10%), Thailand (7%), USA (7%), Australia (3%) | Asia (86%) | 2020-01-10 to 2020-04-15 | Inactive | CCATGGGCG | S |
| 67 | 62 | 103 | Kazakhstan (25%), Australia (17%), China (9%), Sweden (8%), Canada (6%) | Asia (54%) | 2020-01-19 to 2020-04-26 | Inactive | CCACTGGTG | Not Applicaple |
| **255** | 1212 | 2285 | United Kingdom (25%), USA (10%), Netherlands (8%), India (6%), Belgium (6%) | Europe (67%) | 2020-01-24 to 2020-07-03 | **Active** | TTGCGGGTG | G |
| 256 | 548 | 1327 | USA (74%), Canada (9%), Japan (5%), China (4%), Australia (3%) | North America (84%) | 2020-01-17 to 2020-06-12 | Inactive | CCATGGGCG | S |
| **258** | 2522 | 5145 | USA (65%), United Kingdom (5%), Denmark (4%), Netherlands (3%), Australia (3%) | North America (68%) | 2020-02-16 to 2020-07-07 | **Active** | TTGCGTGTG | GH |
| 266 | 42 | 64 | Spain (39%), United Kingdom (23%), Portugal (11%), Australia (6%), Mexico (5%) | Europe (77%) | 2020-02-23 to 2020-04-26 | Inactive | CCATGGGCG | S |
| 291 | 35 | 68 | USA (29%), France (19%), United Kingdom (16%), Belgium (12%), Netherlands (6%) | Europe (60%) | 2020-02-26 to 2020-05-15 | Inactive | TTGCGGGTG | G |
| 297 | 59 | 139 | Belgium (23%), United Kingdom (23%), Turkey (8%), Hungary (7%), Austria (6%) | Europe (85%) | 2020-02-26 to 2020-05-30 | Inactive | TTGCGGGTA | GR |
| **300** | 2057 | 3942 | United Kingdom (44%), USA (8%), Portugal (5%), Australia (4%), Russia (4%) | Europe (72%) | 2020-01-24 to 2020-07-07 | **Active** | TTGCGGGTA | GR |
| 301 | 55 | 250 | Spain (24%), United Kingdom (23%), USA (7%), Russia (5%), Chile (5%) | Europe (73%) | 2020-02-26 to 2020-06-22 | Quiet | TTGCGGGTG | G |
| 305 | 35 | 77 | United Kingdom (77%), Australia (5%), USA (5%), Chile (5%), Greece (3%) | Europe (82%) | 2020-02-22 to 2020-05-08 | Inactive | TTGCGGGTG | G |
| 317 | 79 | 238 | Japan (55%), United Kingdom (13%), USA (8%), Spain (5%), Israel (4%) | Asia (64%) | 2020-02-28 to 2020-06-27 | Quiet | TTGCGGGTA | GR |
| 333 | 38 | 166 | USA (67%), Australia (8%), Canada (5%), France (5%), Israel (5%) | North America (73%) | 2020-02-29 to 2020-04-23 | Inactive | TTGCGTGTG | GH |
| 336 | 22 | 28 | Australia (96%), United Arab Emirates (4%) | Oceania (96%) | 2020-02-25 to 2020-04-04 | Inactive | CCACTGGTG | Not Applicaple |
| 338 | 44 | 158 | USA (72%), Canada (8%), Colombia (4%), Israel (3%), Japan (2%) | North America (79%) | 2020-02-29 to 2020-06-03 | Inactive | TTGCGTGTG | GH |
| 348 | 96 | 207 | United Kingdom (21%), Netherlands (15%), Belgium (10%), Iceland (8%), Sweden (7%) | Europe (80%) | 2020-02-22 to 2020-06-30 | Quiet | TTGCGGGTG | G |
| 355 | 80 | 188 | Spain (65%), Kazakhstan (10%), Netherlands (4%), Chile (3%), United Kingdom (3%) | Europe (79%) | 2020-02-25 to 2020-06-03 | Inactive | CCATGGGCG | S |
| 358 | 23 | 88 | Portugal (57%), United Kingdom (19%), New Zealand (10%), Netherlands (8%), Iceland (3%) | Europe (89%) | 2020-02-21 to 2020-05-18 | Inactive | TTGCGGGTG | G |
| 369 | 133 | 328 | Netherlands (29%), Sweden (16%), United Kingdom (15%), Iceland (9%), Belgium (7%) | Europe (93%) | 2020-03-01 to 2020-05-08 | Inactive | TTGCGGGTA | GR |
| 399 | 116 | 251 | United Kingdom (59%), Belgium (10%), Netherlands (5%), Peru (4%), Russia (3%) | Europe (87%) | 2020-03-02 to 2020-07-01 | Quiet | TTGCGGGTA | GR |
| 439 | 30 | 49 | USA (63%), China (14%), South Korea (8%), Vietnam (6%), Canada (4%) | North America (67%) | 2020-01-15 to 2020-05-15 | Inactive | CCATGGGCG | S |
| 454 | 73 | 194 | Belgium (36%), France (14%), Canada (9%), United Kingdom (7%), Switzerland (4%) | Europe (77%) | 2020-03-04 to 2020-06-05 | Inactive | TTGCGGGTG | G |
| **498** | 135 | 294 | United Kingdom (57%), USA (29%), Switzerland (2%), Australia (2%), Spain (2%) | Europe (65%) | 2020-03-05 to 2020-07-07 | **Active** | TTGCGGGTG | G |
| 550 | 515 | 807 | United Kingdom (45%), USA (11%), Iceland (8%), Australia (8%), South Korea (4%) | Europe (68%) | 2020-01-22 to 2020-05-22 | Inactive | CCACTGTTG | V |
| 551 | 24 | 81 | United Kingdom (43%), Netherlands (15%), USA (15%), Belgium (5%), Australia (5%) | Europe (74%) | 2020-03-05 to 2020-05-13 | Inactive | CCACTGTTG | V |
| 623 | 45 | 107 | USA (45%), Australia (34%), Iceland (14%), Canada (3%), Taiwan (3%) | North America (49%) | 2020-03-05 to 2020-04-17 | Inactive | CCATGGGCG | S |
| 645 | 30 | 65 | USA (43%), Australia (42%), United Kingdom (12%), New Zealand (3%) | Oceania (45%) | 2020-03-07 to 2020-04-10 | Inactive | CCATGGGCG | S |
| 681 | 66 | 125 | Netherlands (68%), South Africa (11%), USA (6%), Iceland (3%), Hungary (2%) | Europe (81%) | 2020-03-08 to 2020-05-07 | Inactive | TTGCGGGTG | G |
| 750 | 40 | 63 | China (67%), Singapore (10%), USA (5%), Australia (3%), Netherlands (3%) | Asia (84%) | 2019-12-30 to 2020-04-24 | Inactive | CCACGGGTG | L |
| 768 | 258 | 524 | USA (93%), Canada (5%), Australia (1%), New Zealand (0%), Singapore (0%) | North America (98%) | 2020-03-09 to 2020-06-19 | Quiet | TTGCGTGTG | GH |
| 780 | 67 | 178 | United Kingdom (97%), Iceland (1%), Uganda (1%), Canada (1%) | Europe (98%) | 2020-03-09 to 2020-06-28 | Quiet | TTGCGGGTA | GR |
| 800 | 98 | 200 | Saudi Arabia (46%), India (30%), United Kingdom (6%), Austria (4%), Japan (4%) | Asia (82%) | 2020-02-03 to 2020-06-13 | Inactive | TTGCGTGTG | GH |
| 834 | 26 | 45 | United Kingdom (53%), USA (13%), Jordan (9%), Australia (7%), Canada (7%) | Europe (60%) | 2020-03-10 to 2020-04-24 | Inactive | CCACTGTTG | V |
| 844 | 43 | 140 | USA (83%), Israel (10%), Argentina (3%), Canada (2%), France (1%) | North America (85%) | 2020-03-03 to 2020-05-19 | Inactive | TTGCGTGTG | GH |
| 985 | 115 | 246 | United Kingdom (86%), USA (7%), Australia (2%), Iceland (1%), Canada (1%) | Europe (88%) | 2020-03-06 to 2020-06-02 | Inactive | TTGCGGGTG | G |
| 1063 | 161 | 294 | Finland (48%), Sweden (28%), United Kingdom (18%), USA (1%), Netherlands (1%) | Europe (98%) | 2020-03-08 to 2020-06-04 | Inactive | TTGCGTGTG | GH |
| 1085 | 23 | 42 | Denmark (98%), New Zealand (2%) | Europe (98%) | 2020-03-13 to 2020-04-28 | Inactive | TTGCGTGTG | GH |
| 1102 | 57 | 99 | Brazil (72%), USA (13%), Chile (4%), Australia (4%), Argentina (4%) | South America (80%) | 2020-03-07 to 2020-06-19 | Quiet | TTGCGGGTA | GR |
| 1148 | 44 | 87 | United Kingdom (89%), Canada (5%), USA (5%), China (1%), Germany (1%) | Europe (90%) | 2020-01-23 to 2020-06-23 | Quiet | CCACGGGTG | L |
| 1179 | 173 | 262 | Singapore (37%), India (32%), Australia (11%), USA (4%), Canada (4%) | Asia (78%) | 2020-03-04 to 2020-06-27 | Quiet | CCACTGGTG | Not Applicaple |
| 1208 | 27 | 44 | United Kingdom (86%), Iceland (7%), Canada (2%), Belgium (2%), USA (2%) | Europe (95%) | 2020-03-14 to 2020-05-17 | Inactive | TTGCGGGTA | GR |
| 1508 | 30 | 59 | USA (95%), Taiwan (3%), United Kingdom (2%) | North America (95%) | 2020-01-23 to 2020-05-04 | Inactive | CCATGGGCG | S |
| 1698 | 22 | 35 | United Kingdom (71%), India (14%), USA (6%), Gambia (3%), Australia (3%) | Europe (71%) | 2020-03-17 to 2020-06-17 | Quiet | TTGCGGGTA | GR |
| 2175 | 38 | 116 | Australia (97%), USA (1%), Portugal (1%), New Zealand (1%), United Kingdom (1%) | Oceania (97%) | 2020-03-16 to 2020-04-08 | Inactive | CCATGGGCG | S |
| 2445 | 22 | 47 | United Kingdom (79%), Canada (11%), Belgium (6%), France (2%), Democratic Republic of the Congo (2%) | Europe (87%) | 2020-03-04 to 2020-05-25 | Inactive | TTGCGGGTG | G |
| 2532 | 47 | 60 | India (32%), Saudi Arabia (27%), Nigeria (8%), Bangladesh (7%), Mali (5%) | Asia (65%) | 2020-03-06 to 2020-06-11 | Inactive | CCATGGGCG | S |
| 2566 | 30 | 47 | USA (98%), Canada (2%) | North America (100%) | 2020-03-20 to 2020-05-16 | Inactive | TTGCGTGTG | GH |
| 2574 | 126 | 337 | United Kingdom (98%), Iceland (1%), Switzerland (1%), Taiwan (0%), Denmark (0%) | Europe (100%) | 2020-03-07 to 2020-06-06 | Inactive | TTGCGGGTG | G |
| 3530 | 27 | 72 | USA (47%), New Zealand (46%), India (4%), Taiwan (1%), Costa Rica (1%) | North America (49%) | 2020-03-17 to 2020-06-12 | Inactive | TTGCGTGTG | GH |
| 4669 | 30 | 44 | Russia (32%), USA (32%), United Kingdom (11%), Hungary (7%), Spain (5%) | Europe (64%) | 2020-03-16 to 2020-06-13 | Inactive | TTGCGGGTG | G |
| 4713 | 25 | 40 | Singapore (100%) | Asia (100%) | 2020-04-04 to 2020-06-22 | Quiet | CCACTGGTG | Not Applicaple |
| **5447** | 67 | 91 | India (74%), Saudi Arabia (10%), Turkey (4%), Bangladesh (4%), Oman (3%) | Asia (91%) | 2020-02-16 to 2020-07-06 | **Active** | TTGCGTGTG | GH |
| 9505 | 26 | 76 | United Kingdom (100%) | Europe (100%) | 2020-04-13 to 2020-05-05 | Inactive | TTGCGGGTA | GR |
| 9734 | 55 | 105 | Japan (55%), USA (13%), Mali (7%), Netherlands (5%), India (4%) | Asia (67%) | 2020-01-23 to 2020-06-13 | Inactive | CCATGGGCG | S |
| 9999 | 52 | 108 | Netherlands (35%), Belgium (12%), Luxembourg (10%), Canada (10%), United Kingdom (9%) | Europe (79%) | 2020-02-29 to 2020-05-31 | Inactive | TTGCGTGTG | GH |
| 10221 | 26 | 49 | USA (100%) | North America (100%) | 2020-03-27 to 2020-06-17 | Quiet | TTGCGGGTG | G |
| 12210 | 28 | 76 | USA (100%) | North America (100%) | 2020-04-30 to 2020-06-09 | Inactive | TTGCGTGTG | GH |
| 13202 | 25 | 42 | India (100%) | Asia (100%) | 2020-04-26 to 2020-06-13 | Inactive | TTGCGTGTG | GH |

***The nine defining SNPs in order (C241,C3037,A23403,C8782,G11083,G25563,G26144,T28144,G28882)**

## Installation
### Dependencies
* [Python3.x](https://www.python.org/downloads/)
* [Blastn](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
### Clone the Github repository
GNUVID is a command-line application written in Python3. Simply download and use! **You will have to install BLAST+!**
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
* Type GNUVID.py -h and it should output help screen.
* Type GNUVID.py -v and you should see an output like GNUVID.py 1.3.

## Usage for GNUVID.py
### Input
1. database (precompressed (.txt or .txt.gz) or a folder of individual genomes(.fna) to be compressed).
2. Reference File (MN908947.3_cds.fna).
3. Query CDS or whole genome FASTA file (.fna) or folder of query files.
4. Strains_order.txt: order of the strains by date of collection (**optional with -m but preferred**).
5. country_region.csv: Assigning regions (Europe, Asia..etc) to different countries (**optional with -m but preferred**).

### Create commpressed database (ordered by date of collection)
```
$GNUVID.py -m COVID19_10422_isolates/ -l Isolates_date_order.txt -o GNUVID_db_results -p GNUVID MN908947.3_cds.fna CDS queries_folder/
```
### Create commpressed database (ordered by date of collection and Regions assigned to the countries)
**Preferred**
```
$GNUVID.py -m COVID19_10422_isolates/ -l Isolates_date_order.txt -cc country_region.csv -o GNUVID_db_results -p GNUVID MN908947.3_cds.fna CDS queries_folder/
```
### Use precompressed database (Most of the times)

**Whole Genome Mode (GNUVID will use blastn to identify the 10 ORFs in the WGS)**
```
$GNUVID.py -d GNUVID/db/GNUVID_07172020_comp_db.txt GNUVID/db/MN908947.3_cds.fna WG test_WG_query/
```
**CDS Mode**
```
$GNUVID.py -d GNUVID/db/GNUVID_07172020_comp_db.txt.gz GNUVID/db/MN908947.3_cds.fna CDS test_CDS_query/
```
### Command line options
```
usage: GNUVID.py [-h] [-m MKDATABASE | -d DATABASE] [-l LIST_ORDER] [-cc COUNTRY_CONTINENT] [-o OUTPUT_FOLDER] [--force]
                 [-p PREFIX] [-q] [-v]
                 reference {WG,CDS} query_fna

GNUVID v1.3 utilizes the natural variation in public genomes of SARS-CoV-2 to rank gene sequences based on the number of
observed exact matches (the GNU score) in all known genomes of SARS-CoV-2. It types the genomes based on their unique gene
allele sequences. It types (using a whole genome MLST) your query genome in seconds.

positional arguments:
  reference             full path to the reference (MN908947.3_cds.fna)
  {WG,CDS}              select a mode from 'WG' or 'CDS' for query files
  query_fna             Query Whole Genome or CDS (for the 10 ORFs) Nucleotide FASTA file/s to analyze (.fna)

optional arguments:
  -h, --help            show this help message and exit
  -m MKDATABASE, --mkdatabase MKDATABASE
                        you have to provide path to a folder of multiple fna files for compression
  -d DATABASE, --database DATABASE
                        you have to provide path to your compressed database
  -l LIST_ORDER, --list_order LIST_ORDER
                        you have to provide path to txt file with isolates ordered by collection date
  -cc COUNTRY_CONTINENT, --country_continent COUNTRY_CONTINENT
                        you have to provide path to csv file with a country to continent assignment
                        csv of first three columns from GISAID acknowledgment table
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Database output prefix to be created for results (default: timestamped GNUVID_results in the current
                        directory)
  --force               Force overwriting existing results folder assigned with -o (default: off)
  -p PREFIX, --prefix PREFIX
                        Prefix for output compressed database (default: GNUVID)
  -q, --quiet           No screen output [default OFF]
  -v, --version         print version and exit
```
### Output
#### Always with -m or -d
**query_GNUVID_report.txt** (tab-separated output file)

Query Gene | GNU score | length | Gene | sequence | Ns count | Allele number | First date seen | Last date seen |
---------- | --------- | ------ | ---- | -------- | -------- | ------------- | --------------- | -------------- |
isolate_x_Gene_3 | 2000 | 366 | ORF8 | ATGTAA | 0 | 1 | 2019-12-24 | 2020-05-04 |
isolate_x_Gene_10 | 0 | 117 | ORF10 | ATGTAA | 0 | E1 | 2019-12-24 | 2020-05-04 |

* Column 1: Query Gene name
* Column 2: GNU score (number of exact matches in the database, GNU=0 novel allele never seen before)
* Column 3: Query gene sequence length
* Column 4: Gene function from the database
* Column 5: Gene sequence
* Column 6: Number of Ns and degenerate bases in the query gene sequence
* Column 7: Alelle number from the database (if preceded by E, it means expected allele)
* Column 8: First date this allele was seen
* Column 9: Last date this allele was seen<br/>

Note: This report should have 10 rows for the ORFs.

**Query_isolates_GNUVID_ST_Report** (tab-separated output file)

Isolate | ORF1ab | Surface_glycoprotein | ORF3a | Envelope_protein | Membrane_glycoprotein | ORF6 | ORF7a | ORF8 | Nucleocapsid_phosphoprotein | ORF10 | Allele profile | ST (level of variation) | First Country | First date seen | last date seen |
------- | ------ | -------------------- | ----- | ---------------- | --------------------- | ---- | ----- | ---- | --------------------------- | ----- | -------------- | ----------------------- | ------------- | --------------- | --------------- |
isolate_x | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Exact | 4 | China | 2019-12-30 | 2020-04-04 |
isolate_y | 4 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Expected | 4 (SLV) | China | 2019-12-30 | 2020-04-04 |
isolate_z | 4 | E1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Expected | 4 | China | 2019-12-30 | 2020-04-04 |

* Column 1: Query Isolate name
* Columns 2-11: The allele numbers for the 10 ORFs (If preceded by E, it means expected allele)
* Column 12: Matching Level (Exact if alleles are in the database or Expected if one allele or more are novel)
* Column 13: ST (Level of variation from the expected ST (SLV, DLV or more than DLV))
* Column 14: First Country where the ST was seen
* Column 15: First Date when the ST was seen
* Column 16: Last Date when the ST was seen<br/>

Note: If -cc option is used seven columns will be added to the report showing the percentage distribution of the ST in 7 regions.

**GNUVID_date_time.log** (Log file, e.g. GNUVID_20200607_170457.log)

#### Always with -m
* prefix_comp_db.txt
* prefix_DB_isolates_report.txt

Isolate | Date | Country | Region | ORF1ab | Surface_glycoprotein | ORF3a | Envelope_protein | Membrane_glycoprotein | ORF6 | ORF7a | ORF8 | Nucleocapsid_phosphoprotein | ORF10 | ST |
------- | ---- | ------- | ------ | ------ | -------------------- | ----- | ---------------- | --------------------- | ---- | ----- | ---- | --------------------------- | ----- | -- |
isolate_1 | 2019-12-24 | China | Asia | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 |
isolate_2 | 2019-01-30 | USA | North America | 5 | 1 | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |

## Bugs
Please submit via the GitHub issues page: https://github.com/ahmedmagds/GNUVID/issues
## Software Licence
GPLv3: https://github.com/ahmedmagds/GNUVID/blob/master/LICENSE
## Source Data
The data used in GNUVID is from GISAID, but sequences were anonymised to fit with guidelines. Appropriate acknowledgements for the labs that provided the original SARS-CoV-2 genome sequences to GISAID are also provided here<br/>
## Citations
### GNUVID
Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread<br/>
[Moustafa AM and Planet PJ 2020, bioRxiv;2020.06.08.139055](https://doi.org/10.1101/2020.06.08.139055)<br/>
### Other tools
* Please cite [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU) 'Moustafa AM and Planet PJ 2020, Genome Biology;21:58'.
* Please also cite BLAST+ 'Camacho et al. 2009, BMC Bioinformatics;10:421' if you use WhatsGNU.
* Please also cite GISAID 'Shu Y. and McCauley J. 2017, EuroSurveillance; 22:13'
* Please also cite the reference genome MN908947 'Wu et al. 2020, Nature; 579:265–269'
* Please also cite eBURST 'Feil et al. 2004,  Journal of Bacteriology; 186:1518'
* Please also cite goeBURST 'Francisco et al. 2009, BMC Bioinformatics; 10:152'
* Please also cite PHYLOViZ 2.0 'Nascimento et al. 2017, Bioinformatics; 33:128-129'
## Author
Ahmed M. Moustafa: [ahmedmagds](https://github.com/ahmedmagds)<br/>
Twitter: [Ahmed_Microbes](https://twitter.com/Ahmed_Microbes)

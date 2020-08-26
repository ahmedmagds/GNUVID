[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ahmedmagds/GNUVID.svg?branch=master)](https://travis-ci.org/ahmedmagds/GNUVID)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3927063.svg)](https://doi.org/10.5281/zenodo.3927063)
# GNUVID
**G**ene **N**ovelty **U**nit-based **V**irus **ID**entification for **SARS-CoV-2**
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It was created to type SARS-CoV-2 genomes using a whole genome wgMLST approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assigns allele numbers to each of the ORFs and a Sequence Type (ST) to the genome. It is based on our recent panallelome approach implemented in [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU).<br/>

A pre-print of the paper **Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread** can be found here: https://www.biorxiv.org/content/10.1101/2020.06.08.139055v1

A table of acknowledgements for the 32719 GISAID SARS-CoV-2 sequences used here is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_06_17_00.xls
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_hcov-19_acknowledgement_table_2020_08_22_23.pdf

## Globally circulating clonal complexes as  of 2020-08-17:

- 32719 GISAID sequences have been included in this analysis.

- GNUVID compressed the 327190 ORFs in the 32719 genomes to 19224 unique alleles.

- 17615 Sequence Types (STs) have been assigned in this dataset and were clustered in 70 clonal complexes (CCs).

- 11 new CCs have been assigned.

- 54 CCs have been Inactive (i.e. Last time seen more than 1 month before 2020-08-17).

- 12 CCs have gone Quiet (i.e. Last seen 2-4 weeks before 2020-08-17).

- 4 CCs have been Active (i.e. Last seen within the 2 weeks before 2020-08-17).

- CC70, CC26, CC343, CC927, CC1434 and 13202 have now been called CC550, CC750, CC9999, CC1179, CC2175 and 13208 respectively.

**Minimum spanning tree of the 17615 STs showing the 70 CCs**

![Image of CCs](https://github.com/ahmedmagds/GNUVID/blob/master/db/MST_08172020.png)

The Four Active CCs are in red and the 12 Quiet CCs are in black. The pie charts show the percentage distribution of genomes from the different geographic regions in each CC.

**The table below shows summary information of the 70 Clonal Complexes (CCs).**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex. Starting from the DB update (07/17/2020), **the nine defining SNPs (C241,C3037,A23403,C8782,G11083,G25563,G26144,T28144,G28882)** for the six GISAID clades are reported for each CC for easier correlation between the two systems.


| Clonal Complex | Number of STs | Number of isolates | Most common 5 countries | Most common Region | Date range | Status | Defining SNPs | GISAID Clade |
|----------------|---------------|--------------------|-------------------------|--------------------|------------|--------|---------------|--------------|
| 4 | 608 | 1151 | USA (20%), United Kingdom (19%), China (18%), Japan (11%), Netherlands (9%) | Asia (38%) | 2019-12-24 to 2020-06-17 | Inactive | CCACGGGTG | L |
| 16 | 22 | 30 | China (67%), Japan (10%), Thailand (7%), USA (7%), Australia (3%) | Asia (87%) | 2020-01-10 to 2020-04-15 | Inactive | CCATGGGCG | S |
| 67 | 63 | 105 | Kazakhstan (25%), Australia (18%), China (9%), Sweden (8%), Canada (6%) | Asia (53%) | 2020-01-19 to 2020-04-26 | Inactive | CCACTGGTG | Not Applicaple |
| 255 | 1433 | 2687 | United Kingdom (23%), USA (13%), India (8%), Netherlands (7%), Belgium (5%) | Europe (63%) | 2020-01-24 to 2020-07-20 | Quiet | TTGCGGGTG | G |
| 256 | 584 | 1431 | USA (74%), Canada (8%), China (5%), Japan (4%), Australia (3%) | North America (82%) | 2020-01-17 to 2020-06-19 | Inactive | CCATGGGCG | S |
| 258 | 2892 | 5884 | USA (66%), United Kingdom (5%), Denmark (4%), Australia (3%), Netherlands (3%) | North America (69%) | 2020-02-16 to 2020-07-17 | Quiet | TTGCGTGTG | GH |
| 266 | 43 | 69 | Spain (41%), United Kingdom (22%), Portugal (13%), Australia (6%), Mexico (4%) | Europe (78%) | 2020-02-23 to 2020-04-26 | Inactive | CCATGGGCG | S |
| 291 | 49 | 106 | France (25%), USA (21%), Saudi Arabia (20%), United Kingdom (9%), Belgium (8%) | Europe (54%) | 2020-02-26 to 2020-06-19 | Inactive | TTGCGTGTG | GH |
| 297 | 66 | 159 | Belgium (20%), United Kingdom (19%), USA (7%), Turkey (7%), Hungary (6%) | Europe (81%) | 2020-02-26 to 2020-07-22 | Quiet | TTGCGGGTA | GR |
| **300** | 2810 | 5505 | United Kingdom (35%), USA (17%), Portugal (8%), India (4%), Russia (4%) | Europe (62%) | 2020-01-24 to 2020-08-05 | **Active** | TTGCGGGTA | GR |
| 301 | 73 | 299 | Spain (24%), United Kingdom (22%), USA (8%), Portugal (5%), Russia (5%) | Europe (71%) | 2020-02-26 to 2020-07-13 | Inactive | TTGCGGGTG | G |
| 305 | 41 | 103 | United Kingdom (63%), USA (21%), Australia (5%), Chile (4%), Greece (2%) | Europe (67%) | 2020-02-22 to 2020-05-10 | Inactive | TTGCGGGTG | G |
| 317 | 93 | 279 | Japan (47%), United Kingdom (14%), USA (14%), Spain (4%), Israel (3%) | Asia (56%) | 2020-02-28 to 2020-07-14 | Inactive | TTGCGGGTA | GR |
| 333 | 42 | 173 | USA (66%), Australia (8%), France (5%), Canada (5%), Israel (5%) | North America (72%) | 2020-02-29 to 2020-04-23 | Inactive | TTGCGTGTG | GH |
| 336 | 22 | 28 | Australia (96%), United Arab Emirates (4%) | Oceania (96%) | 2020-02-25 to 2020-04-04 | Inactive | CCACTGGTG | Not Applicaple |
| 338 | 55 | 187 | USA (72%), Canada (6%), Saudi Arabia (3%), Colombia (3%), Israel (3%) | North America (78%) | 2020-02-29 to 2020-06-18 | Inactive | TTGCGTGTG | GH |
| 348 | 112 | 243 | United Kingdom (19%), Netherlands (13%), Belgium (8%), Iceland (7%), Portugal (7%) | Europe (81%) | 2020-02-22 to 2020-07-07 | Inactive | TTGCGGGTG | G |
| 355 | 86 | 202 | Spain (65%), Kazakhstan (9%), Portugal (5%), Netherlands (4%), Chile (2%) | Europe (81%) | 2020-02-25 to 2020-06-03 | Inactive | CCATGGGCG | S |
| 358 | 51 | 181 | Portugal (78%), United Kingdom (10%), New Zealand (5%), Netherlands (4%), Iceland (2%) | Europe (94%) | 2020-02-21 to 2020-05-18 | Inactive | TTGCGGGTG | G |
| 369 | 138 | 342 | Netherlands (27%), United Kingdom (18%), Sweden (15%), Iceland (8%), Belgium (7%) | Europe (92%) | 2020-03-01 to 2020-05-08 | Inactive | TTGCGGGTA | GR |
| 399 | 134 | 310 | United Kingdom (60%), Belgium (8%), Netherlands (4%), Peru (4%), Spain (3%) | Europe (86%) | 2020-03-02 to 2020-07-18 | Quiet | TTGCGGGTA | GR |
| 439 | 31 | 51 | USA (63%), China (14%), South Korea (10%), Vietnam (6%), Canada (4%) | North America (67%) | 2020-01-15 to 2020-05-15 | Inactive | CCATGGGCG | S |
| 454 | 94 | 240 | Belgium (28%), France (18%), United Kingdom (9%), Canada (7%), Switzerland (6%) | Europe (78%) | 2020-03-04 to 2020-06-11 | Inactive | TTGCGGGTG | G |
| 498 | 210 | 435 | USA (47%), United Kingdom (40%), Switzerland (1%), Spain (1%), Portugal (1%) | North America (49%) | 2020-03-05 to 2020-07-23 | Quiet | TTGCGGGTG | G |
| 550 | 597 | 972 | United Kingdom (42%), South Korea (11%), USA (10%), Iceland (7%), Australia (6%) | Europe (64%) | 2020-01-22 to 2020-05-22 | Inactive | CCACTGTTG | V |
| 551 | 26 | 84 | United Kingdom (43%), USA (15%), Netherlands (14%), Belgium (5%), Australia (5%) | Europe (73%) | 2020-03-05 to 2020-05-13 | Inactive | CCACTGTTG | V |
| 623 | 60 | 145 | USA (50%), Australia (33%), Iceland (10%), Canada (2%), Taiwan (2%) | North America (54%) | 2020-03-05 to 2020-04-23 | Inactive | CCATGGGCG | S |
| 645 | 38 | 75 | USA (48%), Australia (37%), United Kingdom (11%), New Zealand (3%), Guatemala (1%) | North America (49%) | 2020-03-07 to 2020-04-10 | Inactive | CCATGGGCG | S |
| 681 | 66 | 125 | Netherlands (68%), South Africa (11%), USA (6%), Iceland (3%), Hungary (2%) | Europe (81%) | 2020-03-08 to 2020-05-07 | Inactive | TTGCGGGTG | G |
| 750 | 39 | 62 | China (66%), Singapore (10%), USA (5%), Australia (3%), Netherlands (3%) | Asia (85%) | 2019-12-30 to 2020-04-24 | Inactive | CCACGGGTG | L |
| 768 | 301 | 593 | USA (94%), Canada (5%), Australia (1%), New Zealand (0%), Singapore (0%) | North America (98%) | 2020-03-09 to 2020-07-11 | Inactive | TTGCGTGTG | GH |
| 780 | 68 | 196 | United Kingdom (97%), Iceland (1%), Uganda (1%), Canada (1%) | Europe (98%) | 2020-03-09 to 2020-07-14 | Inactive | TTGCGGGTA | GR |
| **800** | 200 | 358 | Saudi Arabia (65%), India (21%), United Kingdom (3%), Austria (3%), Japan (2%) | Asia (90%) | 2020-02-03 to 2020-08-04 | **Active** | TTGCGTGTG | GH |
| 834 | 31 | 61 | United Kingdom (59%), USA (11%), Australia (10%), Jordan (7%), Canada (5%) | Europe (64%) | 2020-03-10 to 2020-06-22 | Inactive | CCACTGTTG | V |
| 844 | 46 | 148 | USA (82%), Israel (11%), Argentina (3%), Canada (2%), France (1%) | North America (84%) | 2020-03-03 to 2020-05-19 | Inactive | TTGCGTGTG | GH |
| 985 | 131 | 275 | United Kingdom (79%), USA (11%), Australia (2%), Iceland (1%), Canada (1%) | Europe (82%) | 2020-03-06 to 2020-06-22 | Inactive | TTGCGGGTG | G |
| 1063 | 183 | 323 | Finland (43%), Sweden (30%), United Kingdom (19%), USA (2%), Netherlands (1%) | Europe (97%) | 2020-03-08 to 2020-06-15 | Inactive | TTGCGTGTG | GH |
| 1085 | 23 | 42 | Denmark (98%), New Zealand (2%) | Europe (98%) | 2020-03-13 to 2020-04-28 | Inactive | TTGCGTGTG | GH |
| 1102 | 95 | 161 | Brazil (78%), USA (11%), Australia (3%), Chile (2%), Argentina (2%) | South America (83%) | 2020-03-07 to 2020-06-27 | Inactive | TTGCGGGTA | GR |
| 1148 | 44 | 87 | United Kingdom (89%), Canada (5%), USA (5%), China (1%), Germany (1%) | Europe (90%) | 2020-01-23 to 2020-06-23 | Inactive | CCACGGGTG | L |
| 1179 | 208 | 332 | Singapore (36%), India (29%), Australia (10%), Malaysia (10%), USA (3%) | Asia (81%) | 2020-03-04 to 2020-07-22 | Quiet | CCACTGGTG | Not Applicaple |
| 1208 | 30 | 51 | United Kingdom (86%), Iceland (6%), Canada (2%), Belgium (2%), USA (2%) | Europe (94%) | 2020-03-14 to 2020-06-17 | Inactive | TTGCGGGTA | GR |
| 1508 | 37 | 72 | USA (92%), Taiwan (4%), South Korea (3%), United Kingdom (1%) | North America (92%) | 2020-01-23 to 2020-05-26 | Inactive | CCATGGGCG | S |
| 1540 | 30 | 51 | United Kingdom (82%), Vietnam (4%), USA (2%), Sweden (2%), Canada (2%) | Europe (88%) | 2020-03-17 to 2020-07-19 | Quiet | TTGCGGGTA | GR |
| 1698 | 44 | 67 | United Kingdom (46%), India (46%), USA (3%), Gambia (1%), Australia (1%) | Asia (48%) | 2020-03-17 to 2020-06-17 | Inactive | TTGCGGGTA | GR |
| 1852 | 23 | 39 | United Kingdom (44%), Portugal (21%), USA (15%), India (5%), Australia (3%) | Europe (69%) | 2020-03-13 to 2020-06-07 | Inactive | TTGCGGGTA | GR |
| 2175 | 45 | 151 | Australia (97%), USA (1%), Portugal (1%), New Zealand (1%), United Kingdom (1%) | Oceania (98%) | 2020-03-16 to 2020-04-08 | Inactive | CCATGGGCG | S |
| 2445 | 23 | 48 | United Kingdom (77%), Canada (10%), Belgium (6%), France (4%), Democratic Republic of the Congo (2%) | Europe (88%) | 2020-03-04 to 2020-05-25 | Inactive | TTGCGGGTG | G |
| 2490 | 25 | 48 | United Kingdom (96%), Australia (2%), Oman (2%) | Europe (96%) | 2020-03-18 to 2020-07-25 | Quiet | TTGCGGGTA | GR |
| **2532** | 57 | 76 | India (36%), Saudi Arabia (28%), Nigeria (7%), Bangladesh (5%), Australia (4%) | Asia (68%) | 2020-03-06 to 2020-08-04 | **Active** | CCATGGGCG | S |
| 2566 | 35 | 54 | USA (98%), Canada (2%) | North America (100%) | 2020-03-20 to 2020-06-30 | Inactive | TTGCGTGTG | GH |
| 2574 | 126 | 338 | United Kingdom (98%), Iceland (1%), Switzerland (1%), Taiwan (0%), Denmark (0%) | Europe (100%) | 2020-03-07 to 2020-06-06 | Inactive | TTGCGGGTG | G |
| 3530 | 37 | 88 | USA (56%), New Zealand (38%), India (3%), Taiwan (1%), Costa Rica (1%) | North America (57%) | 2020-03-17 to 2020-07-17 | Quiet | TTGCGTGTG | GH |
| 4669 | 34 | 48 | USA (33%), Russia (29%), United Kingdom (12%), Hungary (6%), Spain (4%) | Europe (60%) | 2020-03-16 to 2020-07-17 | Quiet | TTGCGGGTG | G |
| 4713 | 28 | 43 | Singapore (100%) | Asia (100%) | 2020-04-04 to 2020-06-22 | Inactive | CCACTGGTG | Not Applicaple |
| 5447 | 143 | 176 | India (64%), Saudi Arabia (23%), Bangladesh (3%), Ireland (3%), Oman (2%) | Asia (94%) | 2020-02-16 to 2020-07-27 | Quiet | TTGCGTGTG | GH |
| 8626 | 24 | 42 | India (100%) | Asia (100%) | 2020-04-20 to 2020-06-21 | Inactive | TTGCGGGTA | GR |
| 8902 | 25 | 79 | USA (99%), United Kingdom (1%) | North America (99%) | 2020-04-15 to 2020-06-18 | Inactive | TTGCGGGTA | GR |
| 9505 | 26 | 76 | United Kingdom (100%) | Europe (100%) | 2020-04-13 to 2020-05-05 | Inactive | TTGCGGGTA | GR |
| 9734 | 59 | 109 | Japan (53%), USA (15%), Mali (6%), Netherlands (5%), India (5%) | Asia (65%) | 2020-01-23 to 2020-06-13 | Inactive | CCATGGGCG | S |
| 9999 | 59 | 124 | Netherlands (31%), United Kingdom (11%), Belgium (10%), Luxembourg (9%), Canada (9%) | Europe (81%) | 2020-02-29 to 2020-05-31 | Inactive | TTGCGTGTG | GH |
| 10221 | 54 | 108 | USA (100%) | North America (100%) | 2020-03-23 to 2020-07-14 | Inactive | TTGCGGGTG | G |
| 11290 | 23 | 30 | United Kingdom (90%), USA (7%), Belgium (3%) | Europe (93%) | 2020-04-01 to 2020-06-21 | Inactive | TTGCGGGTA | GR |
| 12210 | 28 | 77 | USA (100%) | North America (100%) | 2020-04-30 to 2020-06-09 | Inactive | TTGCGTGTG | GH |
| 13208 | 35 | 54 | India (100%) | Asia (100%) | 2020-04-26 to 2020-06-25 | Inactive | TTGCGTGTG | GH |
| 13301 | 33 | 80 | USA (100%) | North America (100%) | 2020-04-09 to 2020-07-21 | Quiet | TTGCGGGTG | G |
| **13669** | 32 | 127 | Australia (100%) | Oceania (100%) | 2020-03-19 to 2020-08-05 | **Active** | TTGCGGGTA | GR |
| 15279 | 38 | 130 | South Korea (98%), Belgium (1%), USA (1%) | Asia (98%) | 2020-03-14 to 2020-05-28 | Inactive | TTGCGTGTG | GH |
| 16416 | 21 | 21 | Saudi Arabia (95%), India (5%) | Asia (100%) | 2020-04-18 to 2020-06-19 | Inactive | TTACGTGTG | Not Applicaple |
| 17244 | 34 | 49 | South Africa (100%) | Africa (100%) | 2020-06-14 to 2020-07-16 | Inactive | TTGCGGGTA | GR |

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
* Type GNUVID.py -v and you should see an output like GNUVID.py 1.4.

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

GNUVID v1.4 utilizes the natural variation in public genomes of SARS-CoV-2 to rank gene sequences based on the number of
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

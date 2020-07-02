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

## Globally circulating clonal complexes as  of 2020-06-17:

- 18298 GISAID sequences have been included in this analysis.

- GNUVID compressed the 182980 ORFs in the 18298 genomes to 10686 unique alleles.

- 9676 Sequence Types (STs) have been assigned in this dataset and were clustered in 45 clonal complexes (CCs).

- 21 new CCs have been assigned.

- 33 CCs have been Inactive (i.e. Last time seen more than 1 month before 2020-06-17).

- 5 CCs have gone Quiet (i.e. Last seen 2-4 weeks before 2020-06-17).

- 7 CCs have been Active (i.e. Last seen within the 2 weeks before 2020-06-17).

- CC70 and CC26 have now been called CC550 and CC750, respectively.

- The three Beijing isolates that are from the [recent Beijing’s big new COVID-19 outbreak](https://www.sciencemag.org/news/2020/06/source-beijing-s-big-new-covid-19-outbreak-still-mystery) were assigned three new STs that are all Single Locus Variant (SLV) at ORF1ab of ST300, that is mainly found in Europe and founder of CC300.

  - Beijing/IVDC-01-06/2020|EPI_ISL_469254|2020-06-11 is assigned to ST9646 (CC300)

  - Beijing/IVDC-02-06/2020|EPI_ISL_469255|2020-06-11 is assigned to ST9647 (CC300)

  - Beijing/env/IVDC-03-06/2020|EPI_ISL_469256|2020-06-11 is assigned to ST9648 (CC300)

**Minimum spanning tree of the 9676 STs showing the 45 CCs**

![Image of CCs](https://github.com/ahmedmagds/GNUVID/blob/master/db/MST_06172020.png)

The seven Active CCs are in red and the 5 Quiet CCs are in black. The pie charts show the percentage distribution of genomes from the different geographic regions in each CC.

**The table below shows summary information of the 45 Clonal Complexes (CCs).**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex.


| Clonal Complex            | Number of STs | Number of isolates | Most common 5 countries                             | Most common Region                             | Date range                 |   Status |
|--------------------------|---------------|--------------------|----------------------------------------------------|-----------------------------------------------|---------------------------|---------|
| 4 | 500 | 928 | USA (21%), China (20%), United Kingdom (15%), Netherlands (11%), Japan (7%) | Europe (37%) | 2019-12-24 to 2020-05-11 | Inactive |
| 16 | 22 | 30 | China (67%), Japan (10%), Thailand (7%), Australia (3%), United Arab Emirates (3%) | Asia (87%) | 2020-01-10 to 2020-03-26 | Inactive |
| 67 | 54 | 87 | Kazakhstan (30%), Australia (21%), China (10%), Canada (7%), India (6%) | Asia (56%) | 2020-01-19 to 2020-04-26 | Inactive |
| **255** | 1010 | 2015 | United Kingdom (19%), Netherlands (9%), USA (9%), Australia (6%), Belgium (6%) | Europe (65%) | 2020-01-24 to 2020-06-08 | **Active** |
| 256 | 483 | 1150 | USA (78%), Canada (8%), China (5%), Australia (3%), Thailand (2%) | North America (86%) | 2020-01-17 to 2020-05-06 | Inactive |
| **258** | 1971 | 4002 | USA (65%), Denmark (6%), Netherlands (4%), Australia (4%), United Kingdom (3%) | North America (68%) | 2020-02-21 to 2020-06-08 | **Active** |
| 266 | 35 | 55 | Spain (42%), United Kingdom (18%), Portugal (13%), Australia (7%), Mexico (5%) | Europe (76%) | 2020-02-23 to 2020-04-26 | Inactive |
| 291 | 25 | 50 | USA (32%), France (26%), Belgium (12%), Netherlands (8%), Canada (4%) | Europe (58%) | 2020-02-26 to 2020-05-15 | Inactive |
| 297 | 40 | 89 | Belgium (27%), United Kingdom (25%), Netherlands (8%), USA (8%), Switzerland (7%) | Europe (75%) | 2020-02-26 to 2020-05-30 | Quiet |
| **300** | 1335 | 2584 | United Kingdom (39%), USA (8%), Portugal (7%), Russia (5%), Belgium (4%) | Europe (75%) | 2020-02-16 to 2020-06-11 | **Active** |
| 301 | 46 | 197 | Spain (30%), United Kingdom (20%), Russia (7%), Chile (6%), USA (5%) | Europe (76%) | 2020-02-26 to 2020-05-30 | Quiet |
| 305 | 26 | 63 | United Kingdom (73%), Australia (6%), USA (6%), Chile (6%), Greece (3%) | Europe (79%) | 2020-02-22 to 2020-05-08 | Inactive |
| 317 | 35 | 86 | United Kingdom (23%), USA (21%), Spain (14%), Japan (8%), Israel (7%) | Europe (50%) | 2020-02-28 to 2020-04-27 | Inactive |
| 333 | 35 | 158 | USA (69%), Australia (9%), Canada (6%), France (5%), Israel (4%) | North America (75%) | 2020-02-29 to 2020-04-23 | Inactive |
| 336 | 22 | 28 | Australia (96%), United Arab Emirates (4%) | Oceania (96%) | 2020-02-25 to 2020-04-04 | Inactive |
| 338 | 38 | 130 | USA (70%), Canada (8%), Colombia (5%), Japan (2%), Taiwan (2%) | North America (78%) | 2020-02-29 to 2020-04-30 | Inactive |
| 343 | 48 | 92 | Netherlands (41%), Belgium (13%), France (12%), Luxembourg (12%), USA (5%) | Europe (89%) | 2020-02-29 to 2020-05-01 | Inactive |
| 348 | 79 | 166 | United Kingdom (22%), Netherlands (19%), Belgium (12%), Iceland (10%), Sweden (7%) | Europe (88%) | 2020-02-22 to 2020-05-22 | Quiet |
| 355 | 76 | 185 | Spain (65%), Kazakhstan (10%), United Kingdom (5%), Netherlands (4%), Chile (3%) | Europe (81%) | 2020-02-25 to 2020-05-14 | Inactive |
| 369 | 104 | 281 | Netherlands (33%), Sweden (16%), Iceland (10%), United Kingdom (9%), Belgium (9%) | Europe (94%) | 2020-03-01 to 2020-05-08 | Inactive |
| 399 | 71 | 152 | United Kingdom (49%), Belgium (12%), Netherlands (8%), Iceland (5%), Russia (5%) | Europe (90%) | 2020-03-02 to 2020-05-12 | Inactive |
| 439 | 27 | 68 | USA (75%), China (10%), Vietnam (4%), South Korea (4%), Hong Kong (1%) | North America (76%) | 2020-01-15 to 2020-04-10 | Inactive |
| **454** | 67 | 166 | Belgium (36%), France (16%), Canada (9%), United Kingdom (5%), Switzerland (4%) | Europe (80%) | 2020-03-04 to 2020-06-05 | **Active** |
| 498 | 75 | 185 | United Kingdom (63%), USA (17%), Australia (3%), Spain (3%), Canada (3%) | Europe (74%) | 2020-03-05 to 2020-05-22 | Quiet |
| 550 | 416 | 687 | United Kingdom (39%), USA (11%), Iceland (10%), Australia (8%), Netherlands (7%) | Europe (68%) | 2020-01-22 to 2020-05-13 | Inactive |
| 623 | 38 | 92 | USA (41%), Australia (30%), Iceland (16%), Canada (3%), Taiwan (3%) | North America (46%) | 2020-03-05 to 2020-04-17 | Inactive |
| 645 | 29 | 61 | Australia (44%), USA (43%), United Kingdom (10%), New Zealand (3%) | Oceania (48%) | 2020-03-07 to 2020-04-10 | Inactive |
| 681 | 58 | 113 | Netherlands (75%), South Africa (12%), Iceland (4%), United Kingdom (2%), Belgium (2%) | Europe (84%) | 2020-03-08 to 2020-05-07 | Inactive |
| 750 | 40 | 62 | China (68%), Singapore (8%), USA (5%), Australia (3%), Netherlands (3%) | Asia (84%) | 2019-12-30 to 2020-04-24 | Inactive |
| 768 | 196 | 411 | USA (92%), Canada (6%), Australia (1%), New Zealand (0%), Singapore (0%) | North America (98%) | 2020-03-09 to 2020-05-11 | Inactive |
| **800** | 61 | 141 | Saudi Arabia (55%), India (25%), United Kingdom (5%), Austria (4%), Finland (3%) | Asia (83%) | 2020-03-10 to 2020-06-08 | **Active** |
| 844 | 38 | 119 | USA (91%), Canada (3%), Israel (3%), France (2%), Argentina (2%) | North America (93%) | 2020-03-03 to 2020-05-13 | Inactive |
| 927 | 132 | 212 | India (37%), Singapore (29%), Australia (14%), USA (5%), Canada (4%) | Asia (75%) | 2020-03-04 to 2020-05-28 | Quiet |
| 985 | 79 | 154 | United Kingdom (82%), USA (10%), Australia (3%), Iceland (2%), Hungary (1%) | Europe (86%) | 2020-03-11 to 2020-05-14 | Inactive |
| 1063 | 56 | 101 | Sweden (43%), United Kingdom (42%), Netherlands (4%), USA (3%), Iceland (3%) | Europe (96%) | 2020-03-08 to 2020-05-13 | Inactive |
| 1085 | 23 | 42 | Denmark (98%), New Zealand (2%) | Europe (98%) | 2020-03-13 to 2020-04-28 | Inactive |
| 1102 | 52 | 91 | Brazil (76%), USA (11%), Chile (4%), Australia (3%), Argentina (2%) | South America (82%) | 2020-03-07 to 2020-04-28 | Inactive |
| 1148 | 34 | 54 | United Kingdom (81%), Canada (7%), USA (7%), China (2%), Germany (2%) | Europe (83%) | 2020-01-23 to 2020-05-12 | Inactive |
| 1434 | 32 | 80 | Australia (96%), USA (1%), Portugal (1%), New Zealand (1%) | Oceania (98%) | 2020-03-16 to 2020-04-07 | Inactive |
| 2445 | 21 | 44 | United Kingdom (77%), Canada (11%), Belgium (7%), France (2%), Democratic Republic of the Congo (2%) | Europe (86%) | 2020-03-04 to 2020-05-01 | Inactive |
| **2532** | 53 | 77 | India (23%), Saudi Arabia (22%), USA (10%), Australia (9%), China (6%) | Asia (61%) | 2020-01-23 to 2020-06-08 | **Active** |
| 2566 | 21 | 30 | USA (97%), Canada (3%) | North America (100%) | 2020-03-20 to 2020-05-08 | Inactive |
| 2574 | 46 | 107 | United Kingdom (93%), Iceland (3%), Switzerland (2%), Taiwan (1%), Denmark (1%) | Europe (99%) | 2020-03-07 to 2020-05-12 | Inactive |
| 3530 | 25 | 68 | USA (50%), New Zealand (49%), Taiwan (1%) | North America (50%) | 2020-03-17 to 2020-04-20 | Inactive |
| **5447** | 46 | 62 | India (81%), Saudi Arabia (13%), Turkey (5%), Netherlands (2%) | Asia (94%) | 2020-03-15 to 2020-06-08 | **Active** |

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
* Type GNUVID.py -v and you should see an output like GNUVID.py 1.2.

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
$GNUVID.py -d GNUVID/db/GNUVID_06172020_comp_db.txt GNUVID/db/MN908947.3_cds.fna WG test_WG_query/
```
**CDS Mode**
```
$GNUVID.py -d GNUVID/db/GNUVID_06172020_comp_db.txt.gz GNUVID/db/MN908947.3_cds.fna CDS test_CDS_query/
```
### Command line options
```
usage: GNUVID.py [-h] [-m MKDATABASE | -d DATABASE] [-l LIST_ORDER] [-cc COUNTRY_CONTINENT] [-o OUTPUT_FOLDER] [--force]
                 [-p PREFIX] [-q] [-v]
                 reference {WG,CDS} query_fna

GNUVID v1.2 utilizes the natural variation in public genomes of SARS-CoV-2 to rank gene sequences based on the number of
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

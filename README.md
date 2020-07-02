[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ahmedmagds/GNUVID.svg?branch=master)](https://travis-ci.org/ahmedmagds/GNUVID)
# GNUVID
**G**ene **N**ovelty **U**nit-based **V**irus **ID**entification for **SARS-CoV-2**
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It was created to type SARS-CoV-2 genomes using a whole genome wgMLST approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assigns allele numbers to each of the ORFs and a Sequence Type (ST) to the genome. It is based on our recent panallelome approach [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU).<br/>

A pre-print of the paper **Rapid whole genome sequence typing reveals multiple waves of SARS-CoV-2 spread** can be found here: https://www.biorxiv.org/content/10.1101/2020.06.08.139055v1

A table of acknowledgements for the 10422 GISAID SARS-CoV-2 sequences used here is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/Supp_Table_1_gisaid_hcov-19_acknowledgement_table_2020_05_17_00.xls

## First Release of the globally circulating clonal complexes as of 2020-05-17:

- 10422 sequences have been included in this analysis.

- 5510 Sequence Types (STs) have been assigned in this dataset and were clustered in 24 clonal complexes (CCs).

- 3 CCs have been inactive (i.e. Last time seen more than 1 month before the release).

- 16 CCs have been silent (i.e. Last seen 2-4 weeks before the release).

- 5 CCs have been active (i.e. Last seen within the 2 weeks before the release).

![Image of CCs](https://github.com/ahmedmagds/GNUVID/blob/master/db/MST_05172020.png "Minimum spanning tree of the 5510 STs showing the 24 CCs")

The largest six CCs are red and the other 18 CCs are in black. The pie charts show the percentage distribution of genomes from the different geographic regions in each CC. The letter A and G next to the pie charts represent the Spike ORF nucleotide at position 23403 in MN908947.3. The ancestral nucleotide is A and the mutation is G resulting in D614G amino acid change.

**The table below shows summary information of the 24 Clonal Complexes (CCs).**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex.


| Clonal Complex            | Number of STs | Number of isolates | Most common 5 countries                             | Most common Region                             | Date range                 |   Status |
|--------------------------|---------------|--------------------|----------------------------------------------------|-----------------------------------------------|---------------------------|---------|
| 4 | 362 | 694 | USA (26%), United Kingdom (17%), China (15%), Netherlands (10%), Japan (9%) | Europe (38%) | 2019-12-24 to 2020-05-01 | Silent |
| 67 | 52 | 69 | Australia (45%), China (12%), Canada (9%), India (7%), United Arab Emirates (6%) | Oceania (45%) | 2020-01-19 to 2020-04-04 | Inactive |
| 70 | 315 | 517 | United Kingdom (39%), Iceland (13%), Australia (11%), USA (10%), Netherlands (7%) | Europe (69%) | 2020-01-22 to 2020-04-22 | Silent |
| **255** | 585 | 1122 | United Kingdom (22%), USA (12%), Iceland (9%), Netherlands (9%), Belgium (7%) | Europe (73%) | 2020-01-24 to 2020-05-03 | **Active** |
| 256 | 380 | 894 | USA (84%), China (4%), Canada (3%), Australia (3%), Thailand (2%) | North America (88%) | 2020-01-17 to 2020-04-29 | Silent |
| **258** | 1280 | 2556 | USA (66%), Denmark (8%), Australia (4%), France (4%), United Kingdom (3%) | North America (66%) | 2020-02-21 to 2020-05-03 | **Active** |
| **300** | 662 | 1299 | United Kingdom (39%), USA (7%), Belgium (6%), Russia (6%), Australia (6%) | Europe (77%) | 2020-02-25 to 2020-05-02 | **Active** |
| 301 | 34 | 134 | United Kingdom (28%), Spain (25%), Russia (10%), Chile (7%), USA (6%) | Europe (81%) | 2020-02-27 to 2020-05-01 | Silent |
| 317 | 24 | 56 | USA (23%), United Kingdom (21%), Spain (11%), Australia (7%), Brazil (5%) | Europe (50%) | 2020-02-28 to 2020-04-19 | Silent |
| 348 | 44 | 94 | United Kingdom (31%), Iceland (18%), Belgium (14%), Australia (6%), Russia (4%) | Europe (85%) | 2020-02-27 to 2020-04-17 | Silent |
| 355 | 28 | 88 | Spain (48%), Australia (17%), United Kingdom (9%), Chile (5%), Netherlands (5%) | Europe (69%) | 2020-02-25 to 2020-04-21 | Silent |
| 369 | 62 | 179 | Netherlands (32%), Iceland (16%), United Kingdom (12%), Belgium (9%), Germany (7%) | Europe (92%) | 2020-03-01 to 2020-04-08 | Inactive |
| 399 | 41 | 85 | United Kingdom (60%), Iceland (8%), Russia (8%), Belgium (5%), Argentina (4%) | Europe (87%) | 2020-03-02 to 2020-04-19 | Silent |
| 454 | 31 | 98 | France (28%), Belgium (22%), United Kingdom (8%), Luxembourg (7%), Switzerland (6%) | Europe (82%) | 2020-03-04 to 2020-04-26 | Silent |
| **498** | 53 | 125 | United Kingdom (82%), USA (5%), Iceland (3%), Switzerland (3%), Australia (3%) | Europe (92%) | 2020-03-05 to 2020-05-02 | **Active** |
| 623 | 24 | 58 | Australia (38%), USA (28%), Iceland (26%), Canada (5%), Mexico (2%) | Oceania (38%) | 2020-03-05 to 2020-04-17 | Silent |
| 750 | 22 | 42 | China (67%), Singapore (10%), USA (7%), Australia (5%), Nepal (2%) | Asia (81%) | 2019-12-30 to 2020-04-14 | Inactive |
| 768 | 131 | 224 | USA (98%), Australia (2%), Canada (0%) | North America (98%) | 2020-03-09 to 2020-04-25 | Silent |
| **800** | 42 | 110 | Saudi Arabia (71%), India (10%), Turkey (5%), Austria (5%), Finland (4%) | Asia (82%) | 2020-03-10 to 2020-05-03 | **Active** |
| 844 | 26 | 70 | USA (90%), France (3%), Canada (3%), Argentina (3%), Australia (1%) | North America (93%) | 2020-03-03 to 2020-04-30 | Silent |
| 927 | 50 | 73 | Australia (32%), Singapore (27%), USA (7%), Taiwan (5%), India (5%) | Asia (48%) | 2020-03-04 to 2020-04-26 | Silent |
| 985 | 43 | 79 | United Kingdom (87%), Iceland (4%), USA (3%), Australia (3%), Hungary (1%) | Europe (94%) | 2020-03-11 to 2020-04-29 | Silent |
| 1063 | 35 | 66 | United Kingdom (48%), Sweden (35%), Netherlands (6%), Iceland (5%), Denmark (5%) | Europe (98%) | 2020-03-12 to 2020-04-22 | Silent |
| 1148 | 26 | 41 | United Kingdom (80%), Canada (10%), USA (10%) | Europe (80%) | 2020-01-23 to 2020-04-24 | Silent |

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
* Type GNUVID.py -v and you should see an output like GNUVID.py 1.0.

## Usage for GNUVID.py
### Input
1. database (precompressed (.txt) or a folder of individual genomes(.fna) to be compressed).
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
$GNUVID.py -d db/GNUVID_05172020_comp_db.txt db/MN908947.3_cds.fna WG test_WG_query/
```
**CDS Mode**
```
$GNUVID.py -d db/GNUVID_05172020_comp_db.txt db/MN908947.3_cds.fna CDS test_CDS_query/
```
### Command line options
```
usage: GNUVID.py [-h] [-m MKDATABASE | -d DATABASE] [-l LIST_ORDER] [-cc COUNTRY_CONTINENT] [-o OUTPUT_FOLDER] [--force]
                 [-p PREFIX] [-q] [-v]
                 reference {WG,CDS} query_fna

GNUVID v1.0 utilizes the natural variation in public genomes of SARS-CoV-2 to rank gene sequences based on the number of
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

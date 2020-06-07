[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# GNUVID
Gene Novelty Unit-based Virus Identification for SARS-CoV-2
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It is created to type SARS-CoV-2 genomes using a whole genome wgMLST approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assign allele numbers to each of the ORFs and a Sequence Type (ST) to the genome. It is based on our recent panallelome approach of [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU).<br/>

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

### Create commpressed database (ordered by date of collection)
```
$GNUVID.py -m COVID19_11113_strains_individual/ -l Strains_date_order.txt -o GNUVID_db_results -p GNUVID MN908947.3_cds.fna CDS queries_folder/
```
### Create commpressed database (ordered by date of collection and Regions assigned to the countries)
**Preferred**
```
$GNUVID.py -m COVID19_11113_strains_individual/ -l Strains_date_order.txt -cc country_region.csv -o GNUVID_db_results -p GNUVID MN908947.3_cds.fna CDS queries_folder/
```
### Use precompressed database

**Whole Genome Mode (the script will use blastn to identify the 10 ORFs in the WGS)**
```
$GNUVID.py -d GNUVID_comp_db.txt -o GNUVID_output MN908947.3_cds.fna WG test_WG_query/
```
or **CDS Mode**
```
$GNUVID.py -d GNUVID_comp_db.txt -o GNUVID_output MN908947.3_cds.fna CDS test_CDS_query/
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
                        you have to provide path to txt file with strains order of interest for time feed
  -cc COUNTRY_CONTINENT, --country_continent COUNTRY_CONTINENT
                        you have to provide path to csv file with a country to continent assignment
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Database output prefix to be created for results (default: timestamped GNUVID_results in the current
                        directory)
  --force               Force overwriting existing results folder assigned with -o (default: off)
  -p PREFIX, --prefix PREFIX
                        Prefix for output compressed database (default: GNUVID)
  -q, --quiet           No screen output [default OFF]
  -v, --version         print version and exit
```

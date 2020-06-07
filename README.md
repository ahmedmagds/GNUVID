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
1. database (precompressed (.txt) or a folder of individual genomes(.fna)).
2. Query CDS or whole genome FASTA file (.fna) or folder of query files.
3. Reference File.

### Create commpressed database or Use precompressed database
```
$GNUVID.py -m COVID19_11113_strains_individual/ -l Strains_date_order.txt -o GNUVID_db_results -p GNUVID -cc country_continent.csv test_queries/
or
$GNUVID.py -d GNUVID_results/GNUVID_comp_db.txt -o GNUVID_output WG test_WG_query/
or
$GNUVID.py -d GNUVID_results/GNUVID_comp_db.txt -o GNUVID_output CDS test_CDS_query/
```
### Use precompressed databases with more features

### Use all features together
```
```
### Command line options

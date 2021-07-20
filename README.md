[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/ahmedmagds/GNUVID.svg?branch=master)](https://travis-ci.org/ahmedmagds/GNUVID)
[![Anaconda_cloud](https://anaconda.org/bioconda/gnuvid/badges/version.svg)](https://anaconda.org/bioconda/gnuvid)
[![Anaconda_install](https://anaconda.org/bioconda/gnuvid/badges/installer/conda.svg)](https://anaconda.org/bioconda/gnuvid)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3927063.svg)](https://doi.org/10.5281/zenodo.4313855)
# GNUVID
**G**ene **N**ovelty **U**nit-based **V**irus **ID**entification for **SARS-CoV-2**
## Introduction
GNUVID (GNU-based Virus IDentification) is a Python3 program. It ranks CDS nucleotide sequences in a genome fna file based on the number of observed exact CDS nucleotide matches in a public or private database. It was created to type SARS-CoV-2 genomes using a whole genome multilocus sequence typing (wgMLST) approach. The 10 ORFs (ORF1ab, S, ORF3a, E, M, ORF6, ORF7a, ORF8, N, ORF10) in SARS-CoV-2 are used for typing. It automatically assigns allele numbers to each of the 10 ORFs and a Sequence Type (ST) to each genome, based on its profile of unique gene allele sequences. It is based on our recent panallelome approach implemented in [WhatsGNU](https://github.com/ahmedmagds/WhatsGNU). It can type your query genome in seconds. As of GNUVID v2.0, GNUVID_Predict.py is a speedy algorithm for assigning Clonal Complexes to new genomes, which uses a Machine Learning Random Forest Classifier.<br/>

A pre-print of the paper **Emerging SARS-CoV-2 diversity revealed by rapid whole genome sequence typing** can be found here: https://www.biorxiv.org/content/10.1101/2020.12.28.424582v1

A table of acknowledgements for the GISAID SARS-CoV-2 sequences used here is available from:
https://github.com/ahmedmagds/GNUVID/blob/master/GISAID_acknowledgement_table_2021_01_06-merged_all.pdf

## Install and use as simple as
Make a new environment and install GNUVID in it
```
conda create -n GNUVID -c bioconda gnuvid
conda activate GNUVID
```

## Globally circulating clonal complexes as  of 2021-06-21:

- 999106 High Quality GISAID sequences have been included in this analysis.

- GNUVID compressed the 9991060 ORFs in the 999106 genomes to 549768 unique alleles.

- 523727 Sequence Types (STs) have been assigned in this dataset and were clustered in 2888 clonal complexes (CCs).

- 2482 new CCs have been assigned (406 CCs in Jan 2021 to 2888 in Jun 2021).

- 1716 CCs have been Inactive (i.e. Last time seen more than 1 month before 2021-06-21).

- 995 CCs have gone Quiet (i.e. Last seen 2-4 weeks before 2021-06-21).

- 177 CCs have been Active (i.e. Last seen within the 2 weeks before 2021-06-21).


## GNUVID now reports the WHO Naming system for VOCs/VOIs (e.g. Alpha, Beta..etc) as per the WHO updated on 07/06/2021:

- 1346 CCs representing the **Alpha** VOC (a.k.a. B.1.1.7).

- 25 CCs representing the **Beta** VOC (a.k.a. B.1.351, B.1.351.2, B.1.351.3).

- 61 CCs representing the **Gamma** VOC (a.k.a. P.1, P.1.1, P.1.2).

- 47 CCs representing the **Delta** VOC (a.k.a. B.1.617.2, AY.1, AY.2).

- 3 CCs representing the **Eta** VOI (a.k.a. B.1.525).

- 80 CCs representing the **Iota** VOI (a.k.a. B.1.526).

- 8 CCs representing the **Kappa** VOI (a.k.a. B.1.617.1).

- 1 CC representing the **Lambda** VOI (a.k.a. C.37).

- 124 CCs representing the 12 lineages (B.1.427/429, P.2, P.3, R.1/R.2, B.1.466.2, B.1.621, AV.1, B.1.1.318, B.1.1.519, AT.1, C.36.3/C.36.3.1, and B.1.214.2) that are currently designated **Alerts** by WHO for Further Monitoring.

- The remaining 1193/2888 CCs are not designatd VOC/VOI/Alert by WHO (07/06/2021).

**A table showing summary information of the 177 Active Clonal Complexes (CCs) can be found [here](https://github.com/ahmedmagds/GNUVID/tree/master/db). A full report for the 2888 CCs can be found [here](https://github.com/ahmedmagds/GNUVID/blob/master/db/GNUVID_06212021_CCs_report.txt)**

## Installation
### Dependencies
* [Python3.x](https://www.python.org/downloads/)
* [Blastn](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
* [MAFFT](https://mafft.cbrc.jp/alignment/software/source.html)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [scikit-learn](https://scikit-learn.org/stable/install.html)
* [minimap2](https://github.com/lh3/minimap2)
* [Gofasta](https://github.com/cov-ert/gofasta)
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
* Type GNUVID_Predict.py -v and you should see an output like GNUVID.py v2.3.

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
usage: GNUVID_Predict.py [-h] [-o OUTPUT_FOLDER] [-m MIN_LEN] [-n N_MAX] [-b BLOCK_PRED] [-e] [-i] [-f] [-q] [-v] query_fna

GNUVID v2.3 uses the natural variation in public genomes of SARS-CoV-2 to rank
gene sequences based on the number of observed exact matches (the GNU score)
in all known genomes of SARS-CoV-2. It assigns a sequence type to each genome
based on its profile of unique gene allele sequences. It can type (using whole
genome multilocus sequence typing; wgMLST) your query genome in seconds.
GNUVID_Predict is a speedy algorithm for assigning Clonal Complexes to new
genomes, which uses machine learning Random Forest Classifier, implemented as
of GNUVID v2.0.

positional arguments:
  query_fna             Query Whole Genome Nucleotide FASTA file to analyze
                        (.fna)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Output folder and prefix to be created for results (default: timestamped GNUVID_results in the current directory)
  -m MIN_LEN, --min_len MIN_LEN
                        minimum sequence length [Default: 15000]
  -n N_MAX, --n_max N_MAX
                        maximum proportion of ambiguity (Ns) allowed [Default: 0.5]
  -b BLOCK_PRED, --block_pred BLOCK_PRED
                        prediction block size, good for limited memory [Default: 1000]
  -e, --exact_matching  turn off exact matching (no allele will be identified for each ORF) and only use machine learning prediction
                        [default: False]
  -i, --individual      Individual Output file for each genome showing the allele sequence and GNU score for each gene allele
  -f, --force           Force overwriting existing results folder assigned with -o (default: off)
  -q, --quiet           No screen output [default OFF]
  -v, --version         print version and exit
```
### Output
#### Always
**GNUVID_results_date_time.csv** (csv file, specify different name using -o option)

Sequence ID | GNUVID DB Version | ORF1ab | Surface_glycoprotein | ORF3a | Envelope_protein | Membrane_glycoprotein | ORF6 | ORF7a | ORF8 | Nucleocapsid_phosphoprotein | ORF10 | Exact ST | First Country seen | First date seen | Last country seen | Last date seen | CC | probability | WHO Naming | Quality Check |
----------- | ----------------- | ------ | -------------------- | ----- | ---------------- | --------------------- | ---- | ----- | ---- | --------------------------- | ----- | -------- | ------------------ | --------------- | ----------------- | -------------- | -- | -----------  | ---------- | ------------- |
isolate_x | 06/21/21 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | China | 2019-12-30 | India | 2020-08-12 | 4 | Exact | NA | passed |
isolate_y | 06/21/21 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | failed (seq_len:4) |
isolate_z | 06/21/21 | None | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | None | NA | NA | NA | NA | 292115 | 0.8 | Delta | passed |

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
* Column 20: WHO Naming will be reported if isolate belongs to VOCs/VOIs/Alerts as designated by WHO
* Column 21: Quality check before prediction (passed or failed (reason))<br/>

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
* gofasta 'https://github.com/cov-ert/gofasta'
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

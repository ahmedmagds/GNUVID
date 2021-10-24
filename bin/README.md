## Usage for GNUVID.py (recommended only for DB compression, use GNUVID_Predict.py for prediction)
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

GNUVID v2.4 utilizes the natural variation in public genomes of SARS-CoV-2 to rank gene sequences based on the number of
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

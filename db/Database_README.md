# Compressed Databases
Authors: **Ahmed M Moustafa and Paul J Planet**

## Rules

Each Compressed Database Release has more genomes analyzed from GISAID, new STs and CCs may be assigned and older CCs may be renamed.


GISAID Sequences inclusion criteria in this analysis.
  - Complete, high coverage genomes (excluding low coverage ) were downloaded from GISAID.
  - Genomes had at least 29,000 bp in length and had less than 1% Ns.
  - Any genome that had any ambiguity (any letter other than A,T,G and C) in the 10 open reading frames (ORF) was excluded.

The STs identified by GNUVID were grouped into larger taxonomic units, clonal complexes (CCs), defined as clusters of >20 STs that were single or double allele variants (SLV or DLV) away from a “founder” as defined in a a minimum spanning tree (MST) using the goeBURST algorithm.

## Limitations

- Because a change in any allele creates a new ST our method may accumulate and count “unnecessary” STs that have been seen only once or may be due to a sequencing error. This is partially ameliorated by the use of the CC definition that allows some variability amongst the members of a group. A large number of STs also may allow more granular approaches to tracking new lineages.

- The status of the CCs (active, silent and inactive) may be a sampling issue.

- Certain regions (US and Europe) clearly sequenced more genomes compared to other regions.

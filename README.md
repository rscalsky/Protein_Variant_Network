# Protein_Variant_Network
Pipeline for generating protein variant networks. Scripts used in: Global Characterization of Diversity and Selective Pressures in Five Plasmodium falciparum Loci Identified by Whole-Genome Sieve Analysis as Putative Antigens

Haplotype Network Guide

Step 1. Remove non-coding DNA from sequences 
  -	This can be done in mesquite for  simple aligned sequences 
    o	Reference sequence on PlasmoDB and manually delete those positions 

Step 2. Identify codons with nonsynonymous mutations and remove all others 
  Script: identify_and_remove_synonymous_codons.py
  Op tions:
	  -r = reference .fasta file of CDS
	  -i = multi-sequence fasta file of samples (CDS only)
	  Generated through GATK reconstruction pipeline
	  -o = output .fasta file 

Step 3. Generate haplotype data file in DNAsp
  1.	Load in multi-sequence alignment file with only nonsynonymous mutation containing codons (product of previous script) 
  2.	Generate  haplotype data file 
    a.	Change to include invariable positions 

Step 4. Generate haplotype frequency input (-f) 
  1.	Copy haplotype frequencies and sequence number from DNAsp haplotype data file to a .txt file
  2.	Run script
    Script: Haplotype_frequency_input_maker.py
    -t = .txt block copied from DNAsp output 
    -o = output.csv  this will produce a .csv that looks like the image below





Step 4a. Filtering out haplotypes by frequency 
(only if you want to filter out sequences belonging to haplotypes of a specific frequency)
Note: This script will use the -f file created for step 4
Script: filter_nonsynonymous_multi_alignment_by_frequency.py
Inputs:
-f = haplotype frequency input (same as step 4) 
-s = multi-sequence alignment of nonsynonymous positions only (product of step 2) 
-c = cutoff frequency 
-o = output  multi-sequence alignment removing sequences under filter and printing in alphabetical order of headers

At this point you will need to generate a DNAsp haplotype data file with the new reduced alignment then proceed. 
  -	Put multi-sequence alignment into DNAsp and regenerate (step 3) 
You will also need to generate a haplotype frequency input for this new alignment
  -	Repeat step 4a with the new filtered multi-sequence alignment

Step 4b. Generate trait file for PopArt 
Script: haplotype_location_counter_v3.py
  -f = haplotype frequency input .csv (created in step 4)
  -s = sequence location input (.txt)
  -o = output trait file .csv
  Note: save this as a .txt for import into PopArt it’s easiest 


1.	Generate sequence location input (-s) – Create a two column .csv that contains the sequence position (row number) and geographic locations 
 
Note these are custom made based on the order of samples in the trimmed multi-alignment  this may be different from the original multi-alignment if you’ve selected for haplotype of a given frequency (see step 4a) 
Pull your filtered multi-sequence alignment into mesquite and manually create this file.

2.	Save this .csv as a .txt b/c popart can’t handle .csv inputs correctly 

Step 5. Generate haplotype network in PopArt
  a)	Import Haplotype Data File from DNAsp 
  b)	Import trait file into PopArt – import a .txt version


Getting Descriptives on your Haplotypes 
This guide will show you how to run scripts which will take the -f haplotype frequency output produced by DNAsp and the Haplotype_frequency_input_maker.py script and produce an output that shows for each haplotype the counts for each country and the proportion of that haplotype they consist of.

Run script: Haplotype_frequency_proportion_counter_by_country_v4.py
  -f = haplotype frequency file .csv created in step 4 
  -s = sequence location input .csv  same as previously shown in 4b
  -o = output.csv 

Note: There is something wrong with the way these .csv output is created where it is not encoding correctly so it may cause errors when fed into other scripts. To bypass this, simply download the file, save as a .csv and reupload for use




This is a README for identify_and_remove_synonymous_codons.py 

This script requires 3 user options
-r = reference_CDS.fasta
-i = multi-sequence_alignment.fasta 
-o = output .fasta file 

This script:

1. Initialize a python dictionary called genetic_codon_dict, for all three letter genetic codons and their corresponding 1 
letter amino acid code.

2. Initialize an array titled codon array where rows represent samples and columns represent codon position. 

3. read through the -r reference sequence and split the sequence into sets of three characters. 
Row 1 should be titled the name of the -r file without the extension. Each set of three should be added to the following columns in the 
codon array until the entire sequence is processed. 

4.Read through the -i multi-sequence alignment and for each sequence, identified by the >header, the sequence will be split into groups 
of three characters and these added to the codon array in the next available row. The first column will instead contain the header information 
from that sample. This will be looped until all samples are added to the codon array. 

5. The next function will have three conditions assessed by comparing the first row’s values to all other values in a pairwise fashion
	1)	if all pairwise comparisons are the same at that column position the script will move to the next column. 
	2)	If a pairwise comparison of codons is different from the reference then the script will input the reference codon to the 
	dictionary and extract the one letter amino acid code, it will also take the comparator codon, input it into the dictionary and 
	extract the one letter amino acid code  if these are different then this entire column will be copied to the nonsynonymous array, 
	if these are the same it will move on to the next pairwise comparison repeating this until all rows have been examined. 
	If no single letter amino acid codes differ the row will be skipped

6. The nonsynonymous array will be the first column containing the reference and all sample IDs and any of the columns that were copied 
given the conditions in step 5. 

7. The -o output file will be a multi-sequence fasta file where the headers will be the column 1 values and the following sequence will be all 
the codons concatenated for that row. 


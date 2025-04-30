This is a README for filter_nonsynonymous_multi_alignment_by_frequency.py

This script takes the numeric [Hap#  Freq. Sequences] block from a  DNAsp haplotype data file converted into a .csv and uses this, a user
provided cutoff value and a multi-sequence alignment (same one used to make the haplotype data file) and eliminates any samples from the 
multi-sequence alignment which are below the cutoff value. The output is a new frequency filtered multi-sequence alignment file. 

This script takes 4 user command line inputs:

-s = multi-sequence alignment of nonsynonymous positions only 

-f = haplotype frequency input

-c = frequency cutoff value 

-o = frequency filtered multi-sequence alignment fasta 

----------------------------------------------------------------------------------------

script that accepts 4 user command line inputs
-s = multi-sequence alignment of nonsynonymous positions only 
-f = haplotype frequency input 
-c = cutoff value (absolute number) 
-o = output frequency filtered multi-sequence alignment fasta 

1. This script should open the multi-sequence alignment file and create a dictionary where the keys are 1 to n and the values are 
each header and following sequence in the -s multi-sequence alignment file. These will be denoted by starting with a > symbol.
For example if the -s file is 
>sample1
ATGCGAGT
>sample2
ATGCCACT

Then the dictionary will be 
1: “””>sample1
ATGCGAGT”””
2:”””>sample2
ATGCCACT”””
The new line structure should be preserved in the dictionary. 

2. This script will then take the user provided -c value and read through the -f input.csv, specifically the Freq. column if the value 
in the Freq. column is less than the -c value it will remove that row. This will continue until all rows are assessed.

3. The script will then examine the remaining rows in the modified -f array, starting at the second row (skip the header), the script 
will examine the values in the third column, it will put this value into the python dictionary and print the key to the -o output 
multi-sequence .fasta file. It will continue then to the fourth column and repeat until it encounters a column with no value at which point 
it will move on to the next row. Note that the values in these columns may have a ] after the value. This can be ignored. This will continue 
until all rows have been assessed

--------------------------------------------------------------------------------------------

Version notes 

v2 = updated to print sequences in alphabetical order by header

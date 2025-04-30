This is a README for Haplotype_frequency_input_maker.py

This script takes two user inputs

-t = frequency_input from DNAsp output
-o = output.csv file 

The -t input is the 

[Hap#  Freq. Sequences]
[Hap_1:  400    1 3 4 6 9 ...
[Hap_2:  413    2-5 ...

block from a DNAsp haplotype data file copied to a .txt file

This script will take the -t input and will create a .csv output in the correct haplotype frequency file format for the haplotype network 
and haplotype frequency by country pipelines 

----------------------------

Previously I was importing the .txt into .csv using space and - as delimiters. This did not work because values ranges greater than 2 values 
would get ignored for example 2-3 would become 2,3 in the csv but 2-4 would become 2,4 skipping the 3 value. 

This script separates all ranges into their constituent parts and keeps all the appropriate values 


NOTE The .csv produced fromt his script seem to have some sort of encoding issue. To resolve this, download them, save them and then reupload
microsoft excel will save them with the correct formatting

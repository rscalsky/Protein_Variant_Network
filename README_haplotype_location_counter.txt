This is a README for haplotype_location_counter.py

This script has three user inputs 

-f = haplotype frequency .csv (generated from haplotype data output from DNAsp using script identify_and_remove_synonymous_codons.py

-s = sequence location .csv (user generated)

-o = output .csv file


Explanation of input formats:
-f = copied from DNAsp haplotype data file output showing Hap#, Freq., Sequences] 
This can be produced with identify_and_remove_synonymous_codons.py

-s = custom .csv that shows, based on the order of your multi-alignment used to generate your haplotype data file 
Sequence_start_range, Sequence_stop_range, Location
1,1,3D7
2,74,Cambodia, Ratanakiri

Rembember this must match their row # in the multi-sequence fasta


--------------------------------------------------------------------------------------


The script does the following: -h = haplotype frequency .csv 
-s = sequence location .csv 
-o = output trait file .csv 

This script should: 
1. Open the -s .csv and from this create a python dictionary where the keys are digits between the Sequence_start_range and 
Sequence_stop_range for each row and the values are the Location value. 

	a.For example: if the Sequence_start_range is 2 and the Sequence_stop_range is 74 and the Location is Cambodia then there should be 
	keys 2,3,4,5,6,7…74 and each should have the same value which is equal to the Location value for that row, in this case Cambodia
	
Note that if a Sequence_start_range and Sequence_stop_range are the same value then that value will be the only key for that Location value. 

2. It will initialize an output array in .csv format with the name given in the -o option. It will copy the [Hap# column from the -h file 
into the first column of the -o array. It will then create one column for every Location listed in the -s file.  The script will 
then, starting at the second row in the -h .csv, beginning in the third Sequences] column take the value of that Sequence column and 
match it to the python dictionary. It will then add +1 count to that location column of the corresponding [Hap# row, that matches the 
returned value in the -o output array. The script will continue until it comes across the first empty column in that row and then move to the 
next row. 

Note that the final value in each row can contain a ] after the number. This can be stripped and ignored. 

For example if the -s array is 
Sequence_start_range, Sequence_stop_range, Location 
2, 5, Cambodia 

The -h array is 
[Hap#, Freq., Sequences]
[Hap_1:, 4, 2, 3, 4, 5
Then the output array will be 
[Hap#, Cambodia
[Hap_1, 4


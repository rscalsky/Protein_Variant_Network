This is a README for _Haplotype_frequency_proportion_counter_by_country.py

The purpose of this script is to calculate the counts and proportions of each haplotype by country --> these values are derived from a DNAsp
haplotype data file which has been processed to follow the -f frequency file format. The -s files are made by hand given the mesquite
multi-sequence alignment that was used to generate the haplotype data file. 

This script should have three user inputs 
-f = haplotype frequency file 
-s = sequence location input 
-o = output .csv 

-f frequency file format:

[Hap#, Freq., Sequences], , , , 
[Hap_1, 240, 1, 28, 49, 54
[Hap_2, 413, 2, 5, 8, 11, , , 

-s sequence location input format:

Sequence_start_range, Sequence_stop_range, Location 
1, 1, Refrence
2, 74, Cambodia
75, 129, Laos

Note these values represent the rows which contain samples from these locations in mesquite 

This script will:

Pseudo Code

We will first initialize the output array and once we can see the output array has been generated correctly we will address the 
counts and proportions part of the script. I want a script that does the following: This script should have three user inputs -f = haplotype 
frequency file -s = sequence location input -o = output .csv

The script will first initialize a -o output array where the first column is Country, the second column will be Total_freq. The following 
columns will be based on the [Hap# column in the -f input. The [Hap# column in the -f input contains n number of rows each with a haplotype 
name. The script will read the first haplotype name in the [Hap# column and create a corresponding column in the -o output, it will also 
create a second column which is the save string with _proportion added to it. It will continue to create these column pairs until it reaches 
the first empty row in the [Hap# column of the -f input.
For example if the -f file is 
[Hap#, Freq., Sequence] 
[Hap_1, 240, 1 
[Hap_2, 413, 2 

Then the -o array will be initialized as 
Location, Total_freq, [Hap_1, [Hap_1_proportion, [Hap_2, [Hap_2_proportion 

We now have an output array that contains the header Location, Total_Freq, [Hap_1, [Hap1_proportion, [Hap_2, [Hap_2_proportion, 
etc... The locations have been correctly copied from the -s input as well. Now we will want to begin filling in the [Hap_1, [Hap_2, etc. 
columns in the -o output. We will address the Total_freq and _proportions column after this.
For this portion we will begin in the second row of the -f input. The first column value will indicate which column of the -o output we will 
begin counting in. The script will look at the third column of the second row and extract the value which we will call the sample_value, 
it will then determine which range this sample_value fits within. The ranges are described by the Sequence_start_range and Sequence_stop_range 
values in the -s input. The ranges start at the Sequence_start_range value and end at the Sequence_stop_range value. Once it determines which 
range this fits within it will pull the corresponding Location from the -s file which contained the Sequence_start_range and 
Sequence_stop_range values containing our sample_value and find that Location row in the -o output. Once determined it will add +1 to the 
corresponding Location row for the matching [Hap column. This will continue until the first empty column appears in the -f input. 
It will then move to the next row of the -f output and repeat this until the first empty row is encountered.  
Note that the final sample_values may have a ] symbol after the numeric value. These can be ignored. only numeric values should be considered. 

Now for the last step, for each [Hap_ column we will summate the entire column then divide that rows value by the summation and 
paste this into the _proportion row For example if we have Location, Total_Freq, Hap_1, Hap_1_proportion, Hap_2, Hap_2_proportion Cambodia, 
NaN, 3, NaN, 5, NaN Laos, NaN, 2, NaN, 5, NaN The step will produce Location, Total_Freq, Hap_1, Hap_1_proportion, Hap_2, Hap_2_proportion 
Cambodia, NaN, 3, 0.6, 5, 0.5 Laos, NaN, 2, 0.4, 5, 0.5 Because Hap_1_proportion for Cambodia is = Hap_1_cambodia/sum[all rows(Hap_1) --> 3 
/ 3 + 2 = 0.6
Hap_2_proportion for Cambodia is = Hap_2_cambodia/sum[all rows(Hap_2) --> 5 / 5 + 5 = 0.5

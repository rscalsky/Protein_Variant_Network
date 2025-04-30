README for Reference_based_reconstruction_parser_create_country_fasta_from_all_samples.py

This script takes three user inputs 

-f = all_samples multi-sequence .fasta
-i = PF3D7_ID in the header
-o = output directory 

This script reads through the headers in a multi-sequence .fasta file and identifies the information found as follows:

PF3D7_ID_xxxxx_all_samples... 

Anything between the designated PF3D7_ID_ and the _all_samples will be extracted and printed to an output that reflects the PF3D7_ID_XXX.fasta

Usually the information between those points is the country in the header. 

---------------------------------------------------------------------

For example if we have a -f file with and -i = PF3D7_0711200
>PF3D7_0711200_Cambodia_all_samples1
ATGATG
>PF3D7_0711200_Cambodia_all_samples2
ATGTTG
>PF3D7_0711200_Brazil_all_samples1
ATGTTG
>PF3D7_0711200_Brazil_all_samples1
ATGGGT

These should be copied to two .fasta outputs as follows output1, file name = PF3D7_0711200_Cambodia.fasta
>PF3D7_0711200_Cambodia_all_samples1
ATGATG
>PF3D7_0711200_Cambodia_all_samples2
ATGTTG output2, file name = PF3D7_Brazil.fasta
>PF3D7_0711200_Brazil_all_samples1
ATGTTG
>PF3D7_0711200_Brazil_all_samples1
ATGGGT

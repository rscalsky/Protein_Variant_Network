import argparse
from Bio import SeqIO
import numpy as np
import os

# Dictionary for genetic codons and corresponding amino acid codes
genetic_codon_dict = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate synonymous codon alignment.")
    parser.add_argument('-r', '--reference', required=True, help="Reference sequence file (.fas or .fasta)")
    parser.add_argument('-i', '--input', required=True, help="Input multi-sequence alignment file (.fas or .fasta)")
    parser.add_argument('-o', '--output', required=True, help="Output multi-sequence alignment file")
    return parser.parse_args()

def create_codon_array(reference_file, input_file):
    # Load reference sequence
    ref_record = SeqIO.read(reference_file, 'fasta')
    ref_seq = str(ref_record.seq)
    ref_name = os.path.splitext(os.path.basename(reference_file))[0]

    # Create codon array
    num_codons = len(ref_seq) // 3
    codon_array = [[ref_name] + [ref_seq[i:i+3] for i in range(0, len(ref_seq), 3)]]

    # Add input sequences
    with open(input_file, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            codons = [str(record.seq[i:i+3]) for i in range(0, len(record.seq), 3)]
            codon_array.append([record.id] + codons)

    return np.array(codon_array)

def create_synonymous_array(codon_array):
    reference_codons = codon_array[0, 1:]
    synonymous_array = [codon_array[:, 0]]  # Start with sample IDs

    for col_idx in range(1, codon_array.shape[1]):
        ref_codon = reference_codons[col_idx - 1]
        ref_aa = genetic_codon_dict.get(ref_codon, '?')
        col_to_add = [codon_array[0, col_idx]]  # Reference sample ID
        synonymous_flag = False  # Track synonymous changes

        for row in range(1, codon_array.shape[0]):
            sample_codon = codon_array[row, col_idx]
            sample_aa = genetic_codon_dict.get(sample_codon, '?')
            col_to_add.append(sample_codon)

            if sample_aa == ref_aa and sample_codon != ref_codon:
                synonymous_flag = True

        if synonymous_flag:
            synonymous_array.append(col_to_add)

    return np.array(synonymous_array).T

def write_output_file(synonymous_array, output_file):
    with open(output_file, 'w') as file:
        for row in synonymous_array:
            header = f">{row[0]}"
            sequence = ''.join(row[1:])
            file.write(f"{header}\n{sequence}\n")

def main():
    args = parse_arguments()

    # Step 3 & 4: Create codon array from reference and input sequences
    codon_array = create_codon_array(args.reference, args.input)

    # Step 5 & 6: Generate synonymous codon array
    synonymous_array = create_synonymous_array(codon_array)

    # Step 7: Write synonymous array to output file in FASTA format
    write_output_file(synonymous_array, args.output)

if __name__ == "__main__":
    main()


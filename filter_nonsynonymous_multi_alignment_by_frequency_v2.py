import csv
import argparse

def parse_fasta(file):
    """Parse a FASTA file and return a dictionary with sequence data."""
    fasta_dict = {}
    with open(file, 'r') as f:
        key = 1
        current_sequence = ""
        for line in f:
            if line.startswith('>'):
                if current_sequence:
                    fasta_dict[key] = current_sequence.strip()
                    key += 1
                current_sequence = line
            else:
                current_sequence += line
        if current_sequence:  # Add the last sequence
            fasta_dict[key] = current_sequence.strip()
    return fasta_dict

def filter_frequencies(frequency_file, cutoff):
    """Filter the frequency file based on the cutoff value and return relevant haplotypes."""
    filtered_haplotypes = []
    with open(frequency_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header
        freq_index = headers.index('Freq.')
        
        for row in reader:
            if row[freq_index].isdigit() and int(row[freq_index]) >= cutoff:
                filtered_haplotypes.append(row[2:])  # Skip to haplotype columns starting from 3rd column
    return filtered_haplotypes

def write_filtered_fasta(fasta_dict, haplotypes, output_file):
    """Write the filtered fasta sequences to an output file, sorted alphabetically by headers."""
    filtered_sequences = []
    for haplotype_row in haplotypes:
        for haplotype in haplotype_row:
            hap_id = haplotype.split(']')[0].strip()  # Remove any trailing "]"
            if hap_id.isdigit():  # Ensure it's a valid key
                key = int(hap_id)
                if key in fasta_dict:
                    filtered_sequences.append(fasta_dict[key])

    # Sort sequences alphabetically by the header line
    sorted_sequences = sorted(filtered_sequences, key=lambda x: x.split('\n')[0])

    # Write sorted sequences to the output file
    with open(output_file, 'w') as out_f:
        for sequence in sorted_sequences:
            out_f.write(f"{sequence}\n")

def main():
    parser = argparse.ArgumentParser(description="Filter a multi-sequence alignment FASTA based on haplotype frequencies.")
    parser.add_argument('-s', required=True, help="Input multi-sequence alignment FASTA file")
    parser.add_argument('-f', required=True, help="Input haplotype frequency CSV file")
    parser.add_argument('-c', type=int, required=True, help="Frequency cutoff value")
    parser.add_argument('-o', required=True, help="Output filtered multi-sequence alignment FASTA file")

    args = parser.parse_args()

    # Step 1: Parse the multi-sequence alignment file into a dictionary
    fasta_dict = parse_fasta(args.s)

    # Step 2: Filter the frequency file based on the cutoff
    filtered_haplotypes = filter_frequencies(args.f, args.c)

    # Step 3: Write the filtered sequences to the output file, sorted by headers
    write_filtered_fasta(fasta_dict, filtered_haplotypes, args.o)

if __name__ == "__main__":
    main()


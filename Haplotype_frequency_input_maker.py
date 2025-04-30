import csv
import argparse

def process_haplotype_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = infile.readlines()
        writer = csv.writer(outfile)

        # Write header (first line from the input file, split by spaces)
        writer.writerow(reader[0].strip().split())

        # Process each line of the haplotype data (excluding header)
        for line in reader[1:]:
            line = line.strip()
            if line:  # Ensure it's not an empty line
                # Remove unwanted characters (e.g., ']') from the sequence part
                line = line.replace(']', '')

                # Split the line into its components (space-separated)
                parts = line.split()

                haplotype = parts[0]
                freq = parts[1]
                sequences = parts[2:]

                # Expand sequences with ranges
                expanded_sequences = []
                for seq in sequences:
                    if '-' in seq:
                        # If there's a range, split and expand the range
                        start, end = map(int, seq.split('-'))
                        expanded_sequences.extend(range(start, end + 1))
                    else:
                        # Otherwise, add the single value
                        expanded_sequences.append(int(seq))

                # Write the processed row to the output CSV
                writer.writerow([haplotype, freq] + expanded_sequences)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process haplotype frequency data into CSV format")
    parser.add_argument('-t', '--input_file', required=True, help="Input .txt file with haplotype data")
    parser.add_argument('-o', '--output_file', required=True, help="Output .csv file")

    args = parser.parse_args()

    process_haplotype_file(args.input_file, args.output_file)


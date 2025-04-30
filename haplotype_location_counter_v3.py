import csv
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process haplotype frequency and sequence location data.")
    parser.add_argument("-f", "--haplotype_file", required=True, help="Path to the haplotype frequency CSV file")
    parser.add_argument("-s", "--sequence_file", required=True, help="Path to the sequence location CSV file")
    parser.add_argument("-o", "--output_file", required=True, help="Path to the output trait file CSV")
    return parser.parse_args()

def create_location_dict(sequence_file):
    location_dict = {}
    with open(sequence_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start = int(row["Sequence_start_range"])
            stop = int(row["Sequence_stop_range"])
            location = row["Location"]
            for key in range(start, stop + 1):
                location_dict[key] = location
    return location_dict

def process_haplotype_file(haplotype_file, location_dict, output_file):
    with open(haplotype_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        haplotypes = [row[0].replace("[", "").replace(":", "") for row in reader]  # Clean up haplotype names
        # Initialize location columns
        location_counts = {hap: {loc: 0 for loc in set(location_dict.values())} for hap in haplotypes}
        
        # Rewind file to read sequences
        csvfile.seek(0)
        next(reader)  # Skip header
        for row in reader:
            haplotype = row[0].replace("[", "").replace(":", "")  # Clean up haplotype names
            # Process each sequence position in row, starting from the third column
            for seq in row[2:]:
                if seq == "":  # End of sequence list
                    break
                seq = seq.rstrip("]")
                try:
                    seq_key = int(seq)
                    location = location_dict.get(seq_key)
                    if location:
                        location_counts[haplotype][location] += 1
                except ValueError:
                    continue  # Ignore non-integer values

    # Write output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        locations = sorted(set(location_dict.values()))
        # Write header with blank first cell and location headers
        writer.writerow([""] + locations)
        for haplotype in haplotypes:
            row = [haplotype] + [location_counts[haplotype][loc] for loc in locations]
            writer.writerow(row)

def main():
    args = parse_arguments()
    location_dict = create_location_dict(args.sequence_file)
    process_haplotype_file(args.haplotype_file, location_dict, args.output_file)

if __name__ == "__main__":
    main()


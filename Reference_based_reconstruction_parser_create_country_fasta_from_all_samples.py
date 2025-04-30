import argparse
from pathlib import Path
from collections import defaultdict

def parse_fasta(input_fasta, pf3d7_id):
    """
    Parses a multi-sequence FASTA file and groups sequences by country based on the header.
    """
    sequences_by_country = defaultdict(list)
    
    with open(input_fasta, 'r') as fasta_file:
        current_header = None
        current_sequence = []
        
        for line in fasta_file:
            if line.startswith(">"):  # Header line
                # Save the current sequence to the appropriate group
                if current_header and current_sequence:
                    country = extract_country(current_header, pf3d7_id)
                    if country:
                        sequences_by_country[country].append((current_header, ''.join(current_sequence)))
                
                # Start a new sequence
                current_header = line.strip()
                current_sequence = []
            else:  # Sequence line
                current_sequence.append(line.strip())
        
        # Don't forget the last sequence
        if current_header and current_sequence:
            country = extract_country(current_header, pf3d7_id)
            if country:
                sequences_by_country[country].append((current_header, ''.join(current_sequence)))
    
    return sequences_by_country

def extract_country(header, pf3d7_id):
    """
    Extracts the country from the header based on the provided PF3D7_ID.
    """
    if pf3d7_id in header:
        try:
            # Extract the substring between PF3D7_ID and "_all_samples"
            start_idx = header.index(pf3d7_id) + len(pf3d7_id) + 1
            end_idx = header.index("_all_samples", start_idx)
            return header[start_idx:end_idx]
        except ValueError:
            pass
    return None

def write_fasta(output_dir, pf3d7_id, sequences_by_country):
    """
    Writes grouped sequences to separate FASTA files in the output directory.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for country, sequences in sequences_by_country.items():
        output_file = output_dir / f"{pf3d7_id}_{country}.fasta"
        with open(output_file, 'w') as fasta_out:
            for header, sequence in sequences:
                fasta_out.write(f"{header}\n{sequence}\n")
        print(f"Written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Parse a multi-sequence FASTA file and group sequences by country.")
    parser.add_argument("-f", "--fasta", required=True, help="Path to the multi-sequence FASTA file.")
    parser.add_argument("-i", "--id", required=True, help="PF3D7_ID to use for grouping sequences.")
    parser.add_argument("-o", "--output", required=True, help="Output directory to store grouped FASTA files.")
    
    args = parser.parse_args()
    sequences_by_country = parse_fasta(args.fasta, args.id)
    write_fasta(args.output, args.id, sequences_by_country)

if __name__ == "__main__":
    main()


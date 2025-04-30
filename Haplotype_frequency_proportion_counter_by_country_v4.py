import argparse
import pandas as pd

def fill_haplotype_counts_and_proportions(freq_file, seq_file, output_file):
    # Load the haplotype frequency file (-f)
    freq_data = pd.read_csv(freq_file, header=None)
    
    # Load the sequence location file (-s)
    seq_data = pd.read_csv(seq_file, header=0)
    
    # Extract haplotypes and initialize output DataFrame
    haplotypes = []
    for hap in freq_data.iloc[:, 0]:  # Assuming the first column is Hap#
        if pd.isna(hap) or hap.strip() == "":
            break
        haplotypes.append(hap.strip(":"))  # Remove trailing colon from haplotype names
    
    # Define the output columns
    output_columns = ["Location", "Total_freq"]
    for hap in haplotypes:
        output_columns.append(hap)
        output_columns.append(f"{hap}_proportion")
    
    # Initialize output DataFrame
    output_df = pd.DataFrame(columns=output_columns)
    output_df["Location"] = seq_data["Location"]  # Copy locations from -s file
    
    # Start processing haplotype counts
    for _, row in freq_data.iterrows():
        hap_col = row.iloc[0]  # Haplotype column (e.g., Hap_1:, Hap_2:, etc.)
        if pd.isna(hap_col) or hap_col.strip() == "":
            break  # Stop at the first empty row
        
        hap_name = hap_col.strip(":")  # Remove trailing colon
        if hap_name not in output_df.columns:
            print(f"Warning: Haplotype {hap_name} not found in output columns.")
            continue
        
        # Iterate through all sequence values in the row (starting from the 3rd column)
        for sample_value_raw in row.iloc[2:]:  # Skip Hap# and Freq.
            if pd.isna(sample_value_raw):
                continue
            
            # Clean sample_value of trailing non-numeric characters and convert to int
            try:
                sample_value = int(float(str(sample_value_raw).strip("[]")))
            except ValueError:
                print(f"Invalid sequence value encountered: {sample_value_raw}")
                continue
            
            # Determine which range the sample_value fits within
            for _, seq_row in seq_data.iterrows():
                start_range = seq_row["Sequence_start_range"]
                stop_range = seq_row["Sequence_stop_range"]
                if start_range <= sample_value <= stop_range:
                    location = seq_row["Location"]
                    # Find the corresponding row in the output DataFrame and increment count
                    output_df.loc[output_df["Location"] == location, hap_name] = (
                        output_df.loc[output_df["Location"] == location, hap_name].fillna(0) + 1
                    )
                    break  # Move to the next sample_value
    
    # Calculate proportions for each haplotype
    for hap in haplotypes:
        hap_total = output_df[hap].sum()
        if hap_total > 0:  # Avoid division by zero
            output_df[f"{hap}_proportion"] = output_df[hap] / hap_total
        else:
            output_df[f"{hap}_proportion"] = 0
    
    # Debugging output: print the final DataFrame
    print("Final Output Array (Counts and Proportions):")
    print(output_df)
    
    # Save the updated DataFrame
    output_df.to_csv(output_file, index=False)
    print(f"Final output array has been saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fill haplotype counts and proportions in the output array based on input files.")
    parser.add_argument("-f", "--freq_file", required=True, help="Haplotype frequency input file")
    parser.add_argument("-s", "--seq_file", required=True, help="Sequence location input file")
    parser.add_argument("-o", "--output_file", required=True, help="Output CSV file")
    
    args = parser.parse_args()
    fill_haplotype_counts_and_proportions(args.freq_file, args.seq_file, args.output_file)


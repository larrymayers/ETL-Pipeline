import os

def remove_non_utf8_and_backslashes(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        for line_bytes in infile:
            # Decode the line as UTF-8, handling errors by replacing them with the "replace" option
            line = line_bytes.decode('utf-8', errors='replace')
            
            # Remove appearance of "\\"
            cleaned_line = line.replace("'", "")
            # cleaned_line = line.replace("'", "")
            
            # Encode the cleaned line back to bytes as UTF-8 and write it to the output file
            outfile.write(cleaned_line.encode('utf-8'))

if __name__ == "__main__":
    input_file = "D:\\Flexbooker\\FlexBooker_Customers_cleaned.csv"  # Replace with the path to your input file
    output_file = "D:\\Flexbooker\\FlexBooker_Customers_repaired.csv"  # Replace with the path to your output file
    
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' not found.")
    else:
        remove_non_utf8_and_backslashes(input_file, output_file)
        print(f"Processing complete. Cleaned data saved to '{output_file}'.")

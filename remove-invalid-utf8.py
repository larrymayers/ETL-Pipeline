import csv
import sys

# Set a custom field size limit
csv.field_size_limit(2147483647)

def remove_invalid_utf8(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        for line in infile:
            line = line.decode('utf-8', errors='replace')
            parts = line.split(':')  # Adjust the delimiter as needed
            cleaned_parts = []
            for part in parts:
                cleaned_part = part.encode('utf-8', 'replace').decode('utf-8')
                cleaned_parts.append(cleaned_part)
            cleaned_line = ':'.join(cleaned_parts)
            outfile.write(cleaned_line.encode('utf-8') + b'\n')

# input_csv_file = f".\\datasets\\EU_Combo\\cleaned\\1.txt"  # Replace with the actual input CSV file path
# output_csv_file = f".\\datasets\\EU_Combo\\1.txt"  # Replace with the desired output CSV file path

# remove_invalid_utf8(input_csv_file, output_csv_file)



for num in range(1,10):
    # Usage example:
    input_csv_file = f".\\datasets\\Dymocks\\chunks\\Dymocks_{num}.csv"  # Replace with the actual input CSV file path
    output_csv_file = f".\\datasets\\Dymocks\\chunks\\cleaned\\Dymocks_{num}_structured.csv"  # Replace with the desired output CSV file path
    
    remove_invalid_utf8(input_csv_file, output_csv_file)

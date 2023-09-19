import argparse
import csv
import os


##parser.add_argument("-o", "--output_directory", default="output", help="Output Directory")
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Please state the name of the file you wish to test for valid CSV formatting.")
args = parser.parse_args()

# Define the expected header
expected_header = ["User ID", "Gender", "Age", "EstimatedSalary", "Purchased"]

# Define input and output file paths
input_file_path = "input.csv"  # Replace with your input CSV file path
valid_output_file_path = "./valid_json.csv"
garbage_output_file_path = "./garbage_json.csv"

# Open the input file in binary read mode and create output files in binary write mode
with open(args.filename, "rb") as infile, \
        open(valid_output_file_path, "wb") as valid_outfile, \
        open(garbage_output_file_path, "wb") as garbage_outfile:

    # Create CSV writers for output files
    valid_writer = csv.writer(valid_outfile)
    garbage_writer = csv.writer(garbage_outfile)

    # Read the header from the input file and write it to both output files as bytes
    header = next(infile)
    valid_outfile.write(header)
    garbage_outfile.write(header)

    # Process each line in the input file
    for line in infile:
        # Check if the line has the expected number of columns
        if len(line.strip().split(b",")) == len(expected_header):
            valid_outfile.write(line)  # Write to the valid output file
        else:
            garbage_outfile.write(line)  # Write to the garbage output file

print("CSV file validation completed. Valid lines saved to 'valid_json.csv', and garbage lines saved to 'garbage_json.csv'.")

import csv
import re
import os

def extract_values(line):
     return line.strip().split(":", 1)[1].strip()  # Use split with maxsplit=1

def process_file(input_file, output_writer):
    with open(input_file, 'r', encoding='utf-8', errors='replace') as file:
        lines = file.readlines()

    url = username = password = None
    data = []
    for line in lines:
        if line.startswith("URL:"):
            url = extract_values(line)
        elif line.startswith("Username:"):
            username = extract_values(line)
        elif line.startswith("Password:"):
            password = extract_values(line)

            if url and username and password:
                data.append([url, username, password])
                url = username = password = None  # Reset values for the next occurrence

    if data:
        output_writer.writerows(data)

def process_files_in_directory(directory_path, output_writer):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".txt"):
                input_file = os.path.join(root, filename)
                process_file(input_file, output_writer)


def main(input_directory, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['URL', 'Username', 'Password'])
        process_files_in_directory(input_directory, csv_writer)

if __name__ == "__main__":
    input_directory = '.\datasets\HPC2023' # Replace with your input folder path
    output_filename = ".\datasets\HPC2023\csv-records\HPC-List-2023.csv"  # Replace with your output CSV file name
    main(input_directory, output_filename)

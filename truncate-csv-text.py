import csv

# Function to truncate a string to a specific length
def truncate_string(text, length):
    if len(text) > length:
        return text[:length]
    return text

# Specify input and output file paths
input_file_path = '.\datasets\HPC2023\csv-records\HPC-List-2023.csv'
output_file_path = '.\datasets\HPC2023\csv-records\Cleaned-HPC-List-2023.csv'

# Open input CSV file
with open(input_file_path, 'r', newline='', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    
    # Open output CSV file
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        
        # Process each row in the input CSV
        for row in reader:
            processed_row = []
            for field in row:
                processed_field = truncate_string(field, 512)
                processed_row.append(processed_field)
            writer.writerow(processed_row)

print("Data processing complete.")

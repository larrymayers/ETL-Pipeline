def extract_username_password(line):
    # Extract username and password from the line
    parts = line.strip().split(' ')
    if len(parts) == 2:
        return parts[0], parts[1]
    return None, None

input_file_path = r'.\datasets\PolishLeaks\Polish Credentials Data Leaked May 2023 - leaks.txt'    # Replace with the path to your input file
output_csv_path = r'.\datasets\PolishLeaks\PCDL_cleaned.csv'   # Replace with the path for the CSV output file
output_other_path = r'.\datasets\PolishLeaks\PCDL_garbage.txt'  # Replace with the path for the other output file

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

csv_lines = []
other_lines = []

for line in lines:
    url, credentials = extract_username_password(line)
    if url is not None and credentials is not None:
        csv_line = f"{url},{credentials.replace(' ', ',').replace(':', ',')}\n"
        csv_lines.append(csv_line)
    else:
        other_lines.append(line)

# Write CSV lines to output CSV file
with open(output_csv_path, 'w', encoding='utf-8') as output_csv_file:
    output_csv_file.writelines(csv_lines)

# Write other lines to output other file
with open(output_other_path, 'w', encoding='utf-8') as output_other_file:
    output_other_file.writelines(other_lines)

print("Processing complete.")

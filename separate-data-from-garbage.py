def process_lines(input_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data_lines = []
        garbage_lines = []

        for line in infile:
            line = line.strip()
            if is_valid_format(line):
                data_lines.append(line)
            else:
                garbage_lines.append(line)

        return data_lines, garbage_lines

def is_valid_format(line):
    # Check if the line matches the format "xxxx@xxx.xx:xxxxx"
    parts = line.split(':')
    if len(parts) == 2:
        email_part, _ = parts
        email_parts = email_part.split('@')
        if len(email_parts) == 2 and '.' in email_parts[1]:
            return True
    return False

def write_lines_to_file(lines, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line + '\n')

# Usage example:
input_file_path = r'.\datasets\EmailPwdCombo\HQSQL.txt'  # Replace with the actual input file path
data_file_path = r'.\datasets\EmailPwdCombo\chunks\HQSQL_Combos\cleaned\HQSQL_cleaned_data.txt'
garbage_file_path = r'.\datasets\EmailPwdCombo\chunks\HQSQL_Combos\garbage\HQSQL_garbage.txt'

data_lines, garbage_lines = process_lines(input_file_path)

write_lines_to_file(data_lines, data_file_path)
write_lines_to_file(garbage_lines, garbage_file_path)

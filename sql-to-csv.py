import re
import csv

def sanitize_string(text):
    # Remove non-ASCII characters
    sanitized = re.sub(r'[^\x00-\x7F]+', '', text)
    return sanitized

def is_email(line):
    # Check if the line starts with an email address
    return re.match(r'^\S+@\S+', line) is not None

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        input_text = infile.read()
    
    lines = input_text.strip().split('\n')
    csv_rows = []

    for line in lines:
        if is_email(line):
            columns = line.split('\t')
            columns = [sanitize_string(col) for col in columns]
            
            if len(columns) >= 15:  # Change to 15 columns (index 0 to 14)
                email, password, name, signup_token, signup_timestamp, signup_ip, user_agent, is_super_admin, birthdate, dev_token, user_ref, status, origin, id, act_sent = columns
                
                # Handle missing or empty name parts
                name_parts = name.split(' ', 2)
                if len(name_parts) == 3:
                    firstname, middlename, lastname = name_parts
                elif len(name_parts) == 2:
                    firstname, lastname = name_parts
                    middlename = ''
                else:
                    firstname, middlename, lastname = '', '', ''
        
                csv_row = [
                    email, password, firstname, middlename, lastname,
                    signup_token, signup_timestamp, signup_ip, user_agent,
                    is_super_admin, birthdate, dev_token, user_ref, status,
                    origin, id, act_sent
                ]
                csv_rows.append(csv_row)
            else:
                print(f"Skipping line: {line}")
    
    # Write to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            'email', 'password', 'firstname', 'middlename', 'lastname',
            'signup_token', 'signup_timestamp', 'signup_ip_address', 'signup_useragent',
            'is_super_admin', 'birthdate', 'dev_token', 'user_ref', 'status',
            'origin', 'id', 'act_sent'
        ])
        csv_writer.writerows(csv_rows)


folder_path = r".\datasets\Aptoide.com\chunks\\"
output_folder = r".\datasets\Aptoide.com\\"

for number in range(100, 137):  # Loop through numbers 32 to 132 (inclusive)
    input_file_path = f"{folder_path}aptoide_00000{number}.txt"
    output_file_path = f"{output_folder}aptoide_{number}.csv"
    convert_to_csv(input_file_path, output_file_path)

# input_file_path = r".\datasets\Aptoide.com\chunks\aptoide_32.txt"    # Replace with the path to your input file
# output_file_path = r".\datasets\Aptoide.com\aptoide_32.csv"  # Replace with the desired output file path

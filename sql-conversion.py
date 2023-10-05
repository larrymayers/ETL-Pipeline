import re

# Define the input file name and output file name
input_file = r'.\datasets\cleaned\Aptoide.com\aptoide_00000001.csv'  # Replace with the actual file name
output_file = r'.\datasets\cleaned\Aptoide.com\aptoide_output.sql'  # Replace with the desired output file name
# Define the pattern for identifying the fields separated by spaces


# Define the pattern for identifying the fields separated by spaces
pattern = r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

# Open the input and output files
with open(input_file, 'rb') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line_bytes in infile:
        # Decode each line using an appropriate encoding
        line = line_bytes.decode('utf-8', errors='replace')  # Use 'replace' for characters that cannot be decoded
        # Use regex to find the pattern in the line
        match = re.match(pattern, line)
        if match:
            data = match.groups()
            # Generate the SQL INSERT statement
            sql_insert = f"INSERT INTO users (email, password, name, signup_token, signup_timestamp, signup_ip_address, signup_useragent, is_super_admin, birthdate, dev_token, user_ref, status, origin, id, act_sent) VALUES "
            values = f"('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}', '{data[7]}', '{data[8]}', '{data[9]}', '{data[10]}', '{data[11]}', '{data[12]}', '{data[13]}', '{data[14]}', '{data[15]}');"
            sql_insert += values + "\n"
            # Write the SQL INSERT statement to the output file
            outfile.write(sql_insert)

# Print a message indicating the process is complete
print("SQL INSERT statements generated successfully!")

# Close the output file
outfile.close()
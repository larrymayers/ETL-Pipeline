def postgres_copy_to_mysql_insert(postgres_copy_line):
    # Extract the table name from the PostgreSQL COPY statement
    table_name = postgres_copy_line.split('(')[0].split()[-1]

    # Extract the column names from the PostgreSQL COPY statement
    columns = [col.strip() for col in postgres_copy_line.split('(')[1].split(')')[0].split(',')]

    # Generate the MySQL INSERT statement
    mysql_insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n"
    return mysql_insert_statement

# Input and output file paths
input_file_path = r'.\datasets\Turkiye.gov\split\Turk1\turkiye_00000001.csv'
output_file_path = 'Turk_1.sql'

# Open input and output files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    is_first_line = True  # To handle the first line differently

    for line in input_file:
        if is_first_line:
            # Convert PostgreSQL COPY to MySQL INSERT
            mysql_insert = postgres_copy_to_mysql_insert(line)
            output_file.write(mysql_insert)
            is_first_line = False
        else:
            # Convert tab-separated values to comma-separated and remove empty lines
            line = line.strip()
            if line:
                line = line.replace('\t', ',')
                output_file.write(line + '\n')

print(f"Conversion complete. Output saved to {output_file_path}")

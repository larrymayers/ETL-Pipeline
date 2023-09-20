
# Define the SQL table name
table_name = "turk_citizen"


for num in range(1, 10):
    # Open the input file for reading
    # Define the input TSV file path
    input_file = f".\\split2\\txt\\split_file_0000000{num}.txt"
    # Define the output SQL file path
    output_file = f".\split2\sql\Turk_{num}.sql"

    # Open the input file for reading
    with open(input_file, 'r') as infile:
        # Read each line from the file
        lines = infile.readlines()

    # Define an empty list to store SQL INSERT statements
    insert_statements = []

    # Loop through each line and generate SQL INSERT statements
    for line in lines:
        # Split the line into values using tab ('\t') as the delimiter
        values = line.strip().split('\t')
        
        # Check if the line has the correct number of values
        if len(values) == 17:
            uid, national_identifier, first_name, last_name, mother_first, father_first, gender, birth_city, date_of_birth, \
            id_registration_city, id_registration_district, address_city, address_district, address_neighborhood, \
            street_address, door_or_entrance_number, misc = values
            
            # Create the SQL INSERT statement
            insert_statement = (
                f"INSERT INTO {table_name} (uid, national_identifier, first_name, last_name, mother_first, father_first, "
                f"gender, birth_city, date_of_birth, id_registration_city, id_registration_district, address_city, "
                f"address_district, address_neighborhood, street_address, door_or_entrance_number, misc) "
                f"VALUES ({uid}, '{national_identifier}', '{first_name}', '{last_name}', '{mother_first}', '{father_first}', "
                f"'{gender}', '{birth_city}', '{date_of_birth}', '{id_registration_city}', '{id_registration_district}', "
                f"'{address_city}', '{address_district}', '{address_neighborhood}', '{street_address}', "
                f"'{door_or_entrance_number}', '{misc}');"
            )
            
            # Append the INSERT statement to the list
            insert_statements.append(insert_statement)

    # Write the SQL INSERT statements to the output file
    with open(output_file, 'w') as outfile:
        for statement in insert_statements:
            outfile.write(statement + '\n')

    print(f'SQL INSERT statements written to {output_file}')
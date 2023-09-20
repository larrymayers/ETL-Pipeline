
# Define the SQL table name
table_name = "turk_citizen"



for num in range(10, 100):
    # Open the input file for reading
    # Define the input TSV file path
    input_file = f".\split\split_file_000000{num}.txt"
    # Define the output SQL file path
    output_file = f".\split\Turk_{num}.sql"


    with open(input_file, 'r') as infile:
        # Read each line from the file
        lines = infile.readlines()

    # Define an empty list to store values
    values_list = []

    # Loop through each line and gather values
    for line in lines:
        # Split the line into values using tab ('\t') as the delimiter
        values = line.strip().split('\t')
        
        # Check if the line has the correct number of values
        if len(values) == 17:
            values_list.append(values)

    # Open the output SQL file for writing
    with open(output_file, 'w') as outfile:
        # Write the SQL INSERT statement header
        outfile.write(f"INSERT INTO {table_name} (uid, national_identifier, first_name, last_name, mother_first, father_first, "
                    f"gender, birth_city, date_of_birth, id_registration_city, id_registration_district, address_city, "
                    f"address_district, address_neighborhood, street_address, door_or_entrance_number, misc) VALUES\n")

        # Write the values using the batch insert format
        for values in values_list:
            uid, national_identifier, first_name, last_name, mother_first, father_first, gender, birth_city, date_of_birth, \
            id_registration_city, id_registration_district, address_city, address_district, address_neighborhood, \
            street_address, door_or_entrance_number, misc = values

            outfile.write(
                f"({uid}, '{national_identifier}', '{first_name}', '{last_name}', '{mother_first}', '{father_first}', "
                f"'{gender}', '{birth_city}', '{date_of_birth}', '{id_registration_city}', '{id_registration_district}', "
                f"'{address_city}', '{address_district}', '{address_neighborhood}', '{street_address}', "
                f"'{door_or_entrance_number}', '{misc}'),\n")

        # Remove the trailing comma and newline character from the last line
        outfile.seek(outfile.tell() - 2, 0)
        outfile.truncate()

    # Close the output file
    print(f'SQL INSERT statements written to {output_file}')

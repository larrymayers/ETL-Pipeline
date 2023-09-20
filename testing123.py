# Define the input file path
input_file = "Unique_Social_Network_Ads.csv"
output_file = "Social_ads.sql"

# Define the SQL table name
table_name = "social_network_ads"

# Open the input file for reading
with open(input_file, mode="r") as infile, open(output_file, 'w') as outfile:
    # Read each line from the file
    lines = infile.readlines()

# Define an empty list to store SQL INSERT statements
insert_statements = []

# Loop through each line and generate SQL INSERT statements
for line in lines:
    # Split the line into values
    values = line.strip().split(',')
    
    # Check if the line has the correct number of values
    if len(values) == 5:
        id, gender, age, estimated_salary, purchased = values
        
        # Create the SQL INSERT statement
        insert_statement = f"INSERT INTO {table_name} (Id, gender, age, estimated_salary, purchased) VALUES ({id}, '{gender}', {age}, {estimated_salary}, {purchased});"
        
        # Append the INSERT statement to the list
        insert_statements.append(insert_statement)
        
        
with open(output_file, 'w') as outfile:
    for statement in insert_statements:
        outfile.write(f"{statement}\n")


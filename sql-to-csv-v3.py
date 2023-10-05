import csv

for num in range (6, 8):
    # Input and output file paths
    input_file_path = f'.\\datasets\\Turkiye.gov\\split\\turkiye_{num}.csv'
    output_file_path = f'.\\datasets\\Turkiye.gov\\split\\Turk{num}\\CSV\\turkiye_{num}.csv'

    # Open input and output files
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        # Define the delimiter (either space or tab)
        delimiter = None

        # Read the first line to determine the delimiter
        first_line = input_file.readline()
        if '\t' in first_line:
            delimiter = '\t'
        elif ' ' in first_line:
            delimiter = ' '
        else:
            raise ValueError("Delimiter not found in the first line.")

        # Set the CSV writer with the determined delimiter
        csv_writer = csv.writer(output_file, delimiter=',')

        # Split the first line into column headers
        column_headers = first_line.strip().split(delimiter)

        # Write the column headers to the CSV file
        csv_writer.writerow(column_headers)

        # Process the remaining lines
        for line in input_file:
            # Split the line using the determined delimiter
            data = line.strip().split(delimiter)

            # Write the data to the CSV file
            csv_writer.writerow(data)

    print(f"Conversion complete. Output saved to {output_file_path}")

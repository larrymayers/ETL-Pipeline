import json
import csv


for num in range(1,27):
    # Define the input JSON file path on your local filesystem
    input_json_file_path = f'.\\datasets\\Verifications.io\\data\\processing\\chunks\\16\\chunk_{num}.json'
    # Define the output CSV file path
    output_csv_file_path = f'.\\datasets\\Verifications.io\\data\\processing\\chunks\\16\\chunk_{num}.csv'


    # Read JSON data from the input file
    with open(input_json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Extract fieldnames from JSON data
    fieldnames = set()
    for record in data:
        fieldnames.update(record.keys())

    # Flatten the JSON data
    flattened_data = []
    for record in data:
        flattened_record = {}
        for key, value in record.items():
            if isinstance(value, dict) and "$oid" in value:
                flattened_record[key] = value["$oid"]
            elif isinstance(value, dict) and "$date" in value:
                flattened_record[key] = value["$date"]
            elif isinstance(value, dict) and "$numberLong" in value:
                flattened_record[key] = value["$numberLong"]
            else:
                flattened_record[key] = value
        flattened_data.append(flattened_record)

    # Write the flattened data to a CSV file with 'replace' option for encoding
    with open(output_csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for record in flattened_data:
            writer.writerow(record)

    print(f"Data has been flattened and saved to {output_csv_file_path}")

import json

# Define the input file path and output file path
input_file_path = r'.\datasets\Verifications.io\data\processing\chunks\chunk_1.json'  # Replace with your input file path
output_file_path = r'.\datasets\Verifications.io\data\processing\chunks\vJ_chunk_1.json'  # Replace with your desired output JSON file path
garbage_file_path = r'.\datasets\Verifications.io\data\processing\chunks\garbage\gJ_chunk.json'  # Path for lines that can't be decoded as JSON

# Create lists to store valid JSON objects and garbage lines
json_data = []
garbage_lines = []

# Read the input file line by line with explicit encoding specification (utf-8)
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            # Parse each line as a JSON object
            record = json.loads(line)
            json_data.append(record)
        except json.JSONDecodeError as e:
           # print(f"Error parsing JSON on line: {line.strip()}")
            garbage_lines.append(line)

# Save the collected JSON data to the output file
with open(output_file_path, 'w') as output_file:
    json.dump(json_data, output_file, indent=2)

# Save garbage lines to the garbage file
with open(garbage_file_path, 'w') as garbage_file:
    garbage_file.writelines(garbage_lines)

print(f"Data has been formatted into valid JSON and saved to {output_file_path}")
print(f"Garbage lines have been saved to {garbage_file_path}")

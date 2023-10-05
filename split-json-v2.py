import os
import json
import codecs

# Define the input JSON file path
input_file_path = r'.\datasets\Verifications.io\data\processing\chunks\chunk_6.json'  # Replace with the path to your input JSON file

# Define the output directory where the chunks will be saved
output_directory = r'.\datasets\Verifications.io\data\processing\chunks\6'  # Replace with the directory where you want to save the chunks
# Define the path for the "garbage.json" file
garbage_file_path = r'.\datasets\Verifications.io\data\processing\chunks\garbage\6\garbage.json'  # Replace with the directory where you want to save the chunks

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Initialize variables
current_chunk_size = 0
current_chunk_number = 1

# Open the input JSON file for reading in binary mode
with open(input_file_path, 'rb') as input_file:
    current_output_file = None
    
    # Open the garbage file for binary write mode for lines that aren't valid JSON
    with open(garbage_file_path, 'wb') as garbage_file:
        for line in input_file:
            # Attempt to write the line to the current output file
            if current_output_file is None:
                current_output_file = open(os.path.join(output_directory, f'chunk_{current_chunk_number}.json'), 'wb')
            
            try:
                current_output_file.write(line)
                current_chunk_size += len(line)
                
                # Check if the current chunk size exceeds the desired size (10GB)
             #   if current_chunk_size >= (10 * 1024 * 1024 * 1024):
                if current_chunk_size >= (200 * 1024 * 1024):
                    current_output_file.close()
                    current_output_file = None
                    current_chunk_size = 0
                    current_chunk_number += 1
            except Exception as e:
                # Line is not valid JSON; write it to the garbage file
                garbage_file.write(line)

# Close the last output file
if current_output_file is not None:
    current_output_file.close()

print("File splitting completed. Invalid JSON lines saved in 'garbage.json'.")
import json
import os

# 47,244,640,256

# Calculate an estimated size of 1 GB in bytes
ONE_GB = 1024 * 1024 * 1024
# ONE_HUNDRED_AND_FIFTY_FOUR_GB = 157696 * 1024 * 1024
SEVENTY_SEVEN_GB = 78848 * 1024 * 1024

def estimate_record_size(data):
    # Serialize a single record to JSON and get its size
    sample_record = json.dumps(data[0], ensure_ascii=False).encode('utf-8')
    return len(sample_record)

def replace_non_ascii(text):
    # Replace non-ASCII characters with a placeholder
    return ''.join(char if ord(char) < 128 else '?' for char in text)

def chunk_json(input_file, output_dir, target_size):
    with open(input_file, "rb") as input_json:
        chunk_number = 1
        current_chunk_size = 0
        current_chunk_data = []

        for line in input_json:
            record = json.loads(line.decode('utf-8'))

            # Replace non-ASCII characters in each record
            for key, value in record.items():
                if isinstance(value, str):
                    record[key] = replace_non_ascii(value)

            current_chunk_data.append(record)
            current_chunk_size += estimate_record_size(current_chunk_data)

            if current_chunk_size >= target_size:
                chunk_filename = os.path.join(output_dir, f"chunk_{chunk_number}.json")
                with open(chunk_filename, "wb") as chunk_json:
                    chunk_json.write(json.dumps(current_chunk_data, ensure_ascii=False, indent=4).encode('utf-8'))
                print(f"Chunk {chunk_number} saved to {chunk_filename}")

                # Reset for the next chunk
                chunk_number += 1
                current_chunk_size = 0
                current_chunk_data = []

        # Save any remaining records as the last chunk
        if current_chunk_data:
            chunk_filename = os.path.join(output_directory, f"emailrecords_{chunk_number}.json") # Each CHUNK
            with open(chunk_filename, "wb") as chunk_json:
                chunk_json.write(json.dumps(current_chunk_data, ensure_ascii=False, indent=4).encode('utf-8'))
            print(f"Chunk {chunk_number} saved to {chunk_filename}")

if __name__ == "__main__":
    input_file_path = r'.\datasets\Verifications.io\data\processing\emailrecords.bson.json'  # Replace with the path to your input JSON file
    output_directory = r'.\datasets\Verifications.io\data\processing\chunks'  # Replace with the directory where you want to save the chunks
    target_chunk_size = SEVENTY_SEVEN_GB  # 1 GB (adjust as needed)
    # target_chunk_size = ONE_GB  # 1 GB (adjust as needed)

    os.makedirs(output_directory, exist_ok=True)

    chunk_json(input_file_path, output_directory, target_chunk_size)

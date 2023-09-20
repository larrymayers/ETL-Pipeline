import json
import csv
import os

def flatten_json(data):
    flattened_data = []
    for record in data:
        flattened_record = {}
        for key, value in record.items():
            if isinstance(value, dict):
                flattened_record[key] = json.dumps(value, ensure_ascii=False)
            else:
                flattened_record[key] = value
        flattened_data.append(flattened_record)
    return flattened_data

def process_chunk(input_json_file_path, output_csv_file_path):
    try:
        with open(input_json_file_path, "r") as json_file:
            lines = json_file.readlines()
        
        fieldnames = set()
        flattened_data = []
        
        for line in lines:
            record = json.loads(line.strip())
            fieldnames.update(record.keys())
            flattened_data.append(record)
        
        flattened_data = flatten_json(flattened_data)
        
        with open(output_csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore', quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for record in flattened_data:
                writer.writerow(record)

        print(f"Data has been flattened and saved to {output_csv_file_path}")
    
    except FileNotFoundError:
        print(f"Input file not found: {input_json_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_dir = '.\\datasets\\Verifications.io\\data\\processing\\chunks\\10\\'
    output_dir = '.\\datasets\\Verifications.io\\data\\processing\\chunks_csv\\'
    
    os.makedirs(output_dir, exist_ok=True)

    for num in range(1, 53):
        input_json_file_path = f'{input_dir}chunk_{num}.json'
        output_csv_file_path = f'{output_dir}chunk_{num}.csv'
        
        process_chunk(input_json_file_path, output_csv_file_path)

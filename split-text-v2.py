import argparse
import os

# folder_path = './datasets/Turkiye.gov/Split'  # Replace with the desired folder path

 

# # Check if the folder doesn't exist, then create it

# if not os.path.exists(folder_path):

#     os.makedirs(folder_path)

#     print(f'Folder "{folder_path}" created successfully.')

# else:

#     print(f'Folder "{folder_path}" already exists.')

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input binary file path")
parser.add_argument("-c", "--chunk_size", type=int, default=50, help="Chunk Size : default as 200 MB per file")
parser.add_argument("-o", "--output_directory", default="output", help="Output Directory")
args = parser.parse_args()

def split_file(file_path, chunk_size, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    
    with open(file_path, 'rb') as file:
        file_count = 0
        current_size = 0
        output_file = None
        
        for line in file:
            if output_file is None or current_size >= chunk_size * 1024 * 1024:
                if output_file:
                    output_file.close()
                file_count += 1
                current_size = 0
                file_name = f'turkiye__{str(file_count).zfill(8)}.csv'
                current_file_path = os.path.join(output_directory, file_name)
                output_file = open(current_file_path, 'w', encoding='utf-8')

            try:
                decoded_line = line.decode('utf-8')  # Try decoding with UTF-8
            except UnicodeDecodeError:
                decoded_line = line.decode('latin-1')  # If that fails, try decoding with Latin-1
            
            output_file.write(decoded_line)
            current_size += len(line)

        if output_file:
            output_file.close()

    print(f'Splitting complete. Total files created: {file_count}')

# Usage
split_file(args.filename, args.chunk_size, args.output_directory)

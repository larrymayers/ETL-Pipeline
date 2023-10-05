import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input text file path")
parser.add_argument("-c", "--chunk_size", type=int, default=50, help="Chunk Size : default as 100 MB per file")
parser.add_argument("-o", "--output_directory", default="output", help="Output Directory")
parser.add_argument("-e", "--encoding", default="UTF-8", help="Encoding default as latin-1")
args = parser.parse_args()

def split_file(file_path, chunk_size, output_directory, encoding_r):
    os.makedirs(output_directory, exist_ok=True)
    with open(file_path, 'r', encoding=encoding_r) as file:
        file_count = 1
        current_size = 0
        file_name = f'aptoide_{str(file_count).zfill(8)}.txt'
        current_file_path = os.path.join(output_directory, file_name)
        output_file = open(current_file_path, 'w', encoding='UTF-8')

        for line in file:
            output_file.write(line)
            current_size += len(line.encode())

            if current_size >= chunk_size * 1024 * 1024:
                output_file.close()
                file_count += 1
                current_size = 0
                file_name = f'aptoide_{str(file_count).zfill(8)}.txt'
                current_file_path = os.path.join(output_directory, file_name)
                output_file = open(current_file_path, 'w', encoding='UTF-8')

        output_file.close()

    print(f'Splitting complete. Total files created: {file_count}')

# Usage
split_file(args.filename, args.chunk_size, args.output_directory, args.encoding)
import os
import codecs
import cchardet as chardet
import argparse
#!pip install faust-cchardet

parser = argparse.ArgumentParser()
parser.add_argument("input_directory", help="Input directory, stores source files")
parser.add_argument("output_directory", help="Ouput directory, stores proccessed files")
parser.add_argument("--overwrite", help="Overwrite existing files")
args = parser.parse_args()

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

def process_line(line):
    parts = line.strip().split(':')

    # Extract email and password parts
    if len(parts) >= 2:
        for part in parts:
            if "@" in part: # if line have more than 2 : then pick the one have @ as email
                email = part[:255] # email and truncate it if its length exceeds 256
                password = parts[-1][:500]  # Pick the last part as password and truncate it if its length exceeds 500 
                return f"{email}:{password}\n"
    else:
        if "@" in line: # if line have more than 2 : then pick the one have @ as email
            email=line.strip()[:255]  # whole line as email and truncate it if its length exceeds 256
            return f"{email}:\n"
    return None

def process_file(input_file_path, output_file_path, encoding='latin-1', buffer_size=5000):
    print(f'\n{input_file_path} encoding: {encoding} buffer: {buffer_size}', flush=True )    
    with codecs.open(input_file_path, 'r', encoding=encoding) as input_file, codecs.open(output_file_path, 'w', encoding='utf-8') as output_file:
        lines_buffer = []
        line_count = 0

        for line in input_file:
            lines_buffer.append(line)
            line_count += 1

            if line_count % buffer_size == 0:
                print('.', end=" ", flush= True)
                process_buffer(lines_buffer, output_file)
                lines_buffer = []

        if lines_buffer:
            process_buffer(lines_buffer, output_file)

def process_buffer(lines_buffer, output_file):
    for line in lines_buffer:
        processed_line = process_line(line)
        if processed_line:
            output_file.write(processed_line)

# Example usage
input_file_path = args.input_directory #'d:/Downloads/dehashedv2/raw/+4.5K MULTIPLE DEHASHED DATABASES [7.38 GB]/'
output_file_path = args.output_directory #'d:/Downloads/dehashedv2/processed'

for file in os.listdir(input_file_path):
    file_name = os.path.join(input_file_path, file)
    file_out_name = os.path.join(output_file_path, file)
    if os.path.isfile(file_name):
        if args.overwrite or (not os.path.exists(file_out_name)):
            encoding = detect_encoding(file_name)
            if not encoding:
                encoding = 'latin-1'
            try:
                process_file(file_name, file_out_name, encoding)
            except Exception  as e:
                #WHEN Encoding fallback to latin-1 whenever there is Exception
                print(e)
                process_file(file_name, file_out_name)
        else:
            print(f'{file_out_name} already exist, skip.')

print('\nDone!')

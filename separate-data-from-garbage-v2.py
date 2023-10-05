def process_bytes(input_file):
    data_bytes = bytearray()
    garbage_bytes = bytearray()
    current_line = bytearray()

    with open(input_file, 'rb') as infile:
        while True:
            byte = infile.read(1)
            if not byte:
                break  # End of file

            if byte == b'\n':  # Newline character indicates the end of a line
                line = current_line.decode('utf-8', errors='ignore')
                if is_valid_format(line):
                    data_bytes.extend(current_line)
                else:
                    garbage_bytes.extend(current_line)
                current_line.clear()
            else:
                current_line.extend(byte)

    return data_bytes, garbage_bytes

def is_valid_format(line):
    # Check if the line matches the format "xxxx@xxx.xx:xxxxx"
    parts = line.split(':')
    if len(parts) == 2:
        email_part, _ = parts
        email_parts = email_part.split('@')
        if len(email_parts) == 2 and '.' in email_parts[1]:
            return True
    return False

def write_bytes_to_file(data_bytes, garbage_bytes, data_file, garbage_file):
    with open(data_file, 'wb') as data_outfile:
        data_outfile.write(data_bytes)
    
    with open(garbage_file, 'wb') as garbage_outfile:
        garbage_outfile.write(garbage_bytes)

# input_file_path = r'.\datasets\EU_Combo\1.txt'
# data_file_path = r'.\datasets\EU_Combo\cleaned\1_structured.txt'
# garbage_file_path = r'.\datasets\EU_Combo\garbage\1_garbage.txt'

# data_bytes, garbage_bytes = process_bytes(input_file_path)

# write_bytes_to_file(data_bytes, garbage_bytes, data_file_path, garbage_file_path)

for num in range(3,20):
    # Usage example:
    input_file_path = f'.\datasets\EU_Combo\{num}.txt'
    data_file_path = f'.\datasets\EU_Combo\cleaned\{num}_structured.txt'
    garbage_file_path = f'.\datasets\EU_Combo\garbage\{num}_garbage.txt'

    data_bytes, garbage_bytes = process_bytes(input_file_path)

    write_bytes_to_file(data_bytes, garbage_bytes, data_file_path, garbage_file_path)

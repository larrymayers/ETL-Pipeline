input_file_path = './datasets/PolishLeaks/chunks/polish_data_00000001.txt'       # Path to the input file
output_file_path = './datasets/PolishLeaks/chunks/polish_data_1A.txt'     # Path to the output file
file_encoding = 'utf-8'             # Specify the file encoding

# Open input file for reading the move every line containing the string "USER::"
with open(input_file_path, 'r', encoding=file_encoding) as input_file:
    lines_with_user = [line for line in input_file if 'USER::' in line]

# Write filtered lines to output file
with open(output_file_path, 'w', encoding=file_encoding) as output_file:
    for line in lines_with_user:
        output_file.write(line)

print("Lines containing 'USER::' have been extracted to the output file.")

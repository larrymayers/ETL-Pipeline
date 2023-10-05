def split_text_to_lines(input_file_path, output_file_path):
    # Read the content of the input file
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # Split the text by spaces and join with newline character
    lines = content.split()  # Split by spaces (default behavior of split)
    formatted_content = '\n'.join(lines)  # Join with newline character

    # Write the formatted content to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(formatted_content)

# Usage example:
input_file_path = '.\datasets\emailPWD\chunks\million_74_00000001.txt'  # Replace with the actual input file path
output_file_path = '.\datasets\emailPWD\chunks\cleaned_million_74_1.txt'  # Replace with the desired output file path
split_text_to_lines(input_file_path, output_file_path)

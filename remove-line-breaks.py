def remove_line_breaks(input_file_path):
    # Read the content of the input file
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # Remove line breaks by replacing them with spaces
    content_without_line_breaks = content.replace('\n', ' ').replace('\r', '')

    # Write the modified content back to the input file
    with open(input_file_path, 'w', encoding='utf-8') as input_file:
        input_file.write(content_without_line_breaks)

# Usage example:
input_file_path = '.\datasets\zerooqcom\chunks\zerooqcom_00000001.csv'  # Replace with the actual file path
remove_line_breaks(input_file_path)

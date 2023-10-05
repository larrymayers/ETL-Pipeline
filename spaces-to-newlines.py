def convert_spaces_to_newlines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified_content = content.replace(' ', '\n')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print("Conversion successful!")
    except Exception as e:
        print("An error occurred:", e)

input_filename = '.\datasets\zerooqcom\chunks\zerooqcom_00000001.csv'  # Change this to your input file's name
output_filename = '.\datasets\zerooqcom\chunks\zerooqcom_1_structured.csv'  # Change this to the desired output file's name

convert_spaces_to_newlines(input_filename, output_filename)
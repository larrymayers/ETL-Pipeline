def add_colon_to_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified_lines = [line.strip() + (":null" if ":" not in line else "") for line in lines]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(modified_lines))
        
        print("Colon added to lines successfully!")
    except Exception as e:
        print("An error occurred:", e)

input_filename = '.\datasets\emailPWD\chunks\million_74_1A_structured.txt'  # Change this to your input file's name
output_filename = '.\datasets\emailPWD\chunks\million_74_1A_cleaned.txt'  # Change this to the desired output file's name

add_colon_to_lines(input_filename, output_filename)

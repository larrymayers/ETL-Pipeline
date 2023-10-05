def remove_empty_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified_lines = [line.strip() for line in lines if line.strip()]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(modified_lines))
        
        print("Empty lines removed successfully!")
    except Exception as e:
        print("An error occurred:", e)

for num in range(1,17):
    #input_filename = f'.\datasets\emailProject\chunks\geniusu_{num:08}.csv'  # Change this to your input file's name
    input_filename = f'.\\datasets\\Turkiye.gov\\split\\Turk7\\CSV\\output\\turkiye__{num:08}.csv'  # Change this to your input file's name
    #output_filename = f'.\datasets\emailProject\chunks\structured\geniusu_{num}_structured.csv'  # Change this to the desired output file's name
    output_filename = f'.\\datasets\\Turkiye.gov\\split\\Turk7\\CSV\\output\\turkiye_{num}_cleaned.csv'  # Change this to the desired output file's name

    remove_empty_lines(input_filename, output_filename)

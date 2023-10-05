# folder_path = r'.\datasets\EU_Combo\chunks\converted\custom_records'
folder_path = r'.\\datasets\\JD Group\\chunks'

for num in range(1, 4):  # Loop through numbers 32 to 132 (inclusive)

    input_file_path = f"{folder_path}\\JD_{num}_cleaned.csv"
    #input_file_path = f'.\\datasets\\Turkiye.gov\\split\\Turk{num}\\CSV\\turkiye_{num}.csv'
        # Read lines, remove quotation marks, and update the original file
    with open(input_file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        # Remove single quotation marks from each line
        # cleaned_lines = [line.replace(' ', '') for line in lines]
        # cleaned_lines = [line.replace('"', '') for line in lines]
        cleaned_lines = [line.replace("\\", "") for line in lines]
        # cleaned_lines = [line.replace('zz', '') for line in lines]

        # Move the file pointer to the beginning and truncate the file
        file.seek(0)
        file.truncate()

        # Write the cleaned lines back to the file
        file.writelines(cleaned_lines)

    print("Quotation marks removed from the file.")

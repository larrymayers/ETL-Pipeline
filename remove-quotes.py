# folder_path = r'.\datasets\EU_Combo\chunks\converted\custom_records'
<<<<<<< HEAD
folder_path = r'.\\datasets\\JD Group\\chunks'

for num in range(1, 4):  # Loop through numbers 32 to 132 (inclusive)

    input_file_path = f"{folder_path}\\JD_{num}_cleaned.csv"
    #input_file_path = f'.\\datasets\\Turkiye.gov\\split\\Turk{num}\\CSV\\turkiye_{num}.csv'
=======
folder_path = r'.\datasets\Turkiye.gov\split\Turk1\CSV'


for num in range(7, 8):  # Loop through numbers 32 to 132 (inclusive)

    #input_file_path = f"{folder_path}\\aptoide_{number}.csv"
    input_file_path = f'.\\datasets\\Turkiye.gov\\split\\Turk{num}\\CSV\\turkiye_{num}.csv'
>>>>>>> 5cd0d343e009506e65658a1f0c75b40f3ca44d96
        # Read lines, remove quotation marks, and update the original file
    with open(input_file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        # Remove single quotation marks from each line
<<<<<<< HEAD
        # cleaned_lines = [line.replace(' ', '') for line in lines]
        # cleaned_lines = [line.replace('"', '') for line in lines]
        cleaned_lines = [line.replace("\\", "") for line in lines]
=======
        cleaned_lines = [line.replace(' ', '') for line in lines]
        # cleaned_lines = [line.replace("'", "") for line in lines]
        # cleaned_lines = [line.replace("\\", "") for line in lines]
>>>>>>> 5cd0d343e009506e65658a1f0c75b40f3ca44d96
        # cleaned_lines = [line.replace('zz', '') for line in lines]

        # Move the file pointer to the beginning and truncate the file
        file.seek(0)
        file.truncate()

        # Write the cleaned lines back to the file
        file.writelines(cleaned_lines)

    print("Quotation marks removed from the file.")

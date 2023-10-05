def remove_non_ascii(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.readlines()  # Read lines into a list

        cleaned_lines = [line for line in content if all(ord(char) < 128 for char in line)]

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(cleaned_lines)

        print("Non-ASCII characters removed and saved to", output_file)
    except FileNotFoundError:
        print("Input file not found:", input_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    
    # input_file_path = f".\\datasets\\EU_Combo\\cleaned\\1_structured.txt"  # Replace with the desired output CSV file path
    # output_file_path = f".\\datasets\\EU_Combo\\cleaned\\1.txt"  # Replace with the desired output CSV file path
    # remove_non_ascii(input_file_path, output_file_path)
    
    for num in range(1,10):
    # Usage example:
        input_file_path = f".\\datasets\\Dymocks\\chunks\\cleaned\\Dymocks_{num}_structured.csv"  # Replace with the desired output CSV file path
        output_file_path = f".\\datasets\\Dymocks\\chunks\\Dymocks_{num}_structured.csv"  # Replace with the desired output CSV file path

        remove_non_ascii(input_file_path, output_file_path)
        print("Non-ASCII characters removed and saved to", output_file_path)

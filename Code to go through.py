import os

class Dataset:
    count = 0
    maximum_ingestable_size = 10

    def __init__(self, name, format, delimiter, location, size=0):
        self.name = name
        self.format = format
        self.delimiter = delimiter
        self.location = location
        self.size = size
        Dataset.count += 1

def create_dataset_from_file(file_path):
    try:
        # Get file name from the file path
        file_name = file_path.split("\\")[-1]

        # Get file size in bytes
        
        size = os.path.getsize(file_path)

        # Determine file format based on file extension
        file_extension = file_name.split(".")[-1].lower()
        
        if file_extension == 'txt':
            file_format = 'Text'
        elif file_extension == 'csv':
            file_format = 'CSV'
        elif file_extension == 'xlsx':
            file_format = 'Excel'
        else:
            file_format = 'Unknown'

       

        # Create a Dataset object
        dataset = Dataset(name=file_name, format=file_format, delimiter='null', location=file_path, size=size)

        return dataset

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None

#def get_user_input():
 #   delimiter = input("Enter the delimiter for the file (e.g., ',' for CSV, '\\t' for TSV): ")
  #  return delimiter

# Example usage:
file_path = r"C:\Users\JayshreeGreenidge\Documents\Pull\Identify Duplicates.txt"
#user_delimiter = get_user_input()
dataset = create_dataset_from_file(file_path)
if dataset:
    print(f"Name: {dataset.name}")
    print(f"Format: {dataset.format}")
   #print(f"Delimiter: {dataset.delimiter}")
    print(f"Location: {dataset.location}")
    print(f"Size: {dataset.size} bytes")
    print(f"Total datasets created: {Dataset.count}")

class Dataset:
    # Core OBJECT designed to manage all data ingestion - Needs some work though

    type = 'Dataset'
    count = 0
    maximum_ingestable_size = 10

    def __init__(self,name,format,delimeter,location,size=0):
        self.name = name        
        self.format = format
        self.delimeter = delimeter
        self.location = location
        self.size = size
        Dataset.count +=1

      
    def display(self):
        print(f'Welcome to {self.name}.This file is currenltly {self.size} of hefty data.')
        print(f'this file is located in {self.location}.')
        print(f'{self.name} has a format of {self.format} with a delimeter of {self.delimeter}.')
        print("")
        print("what would you like to do?")

one = Dataset()
one.display()

        


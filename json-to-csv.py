import pandas as pd
import json

json_file_path = r'.\datasets\Verifications.io\data\processing\json_records.json'
csv_file_path = r'\datasets\Verifications.io\data\processing\json_records.csv'

# Load JSON data into a DataFrame
data = []
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    for line in json_file:
        data.append(json.loads(line))
        # _id, phone
#df = pd.json_normalize(data, record_path='_id', 'phone')
df = pd.json_normalize(data)

# Write DataFrame to CSV
df.to_csv(csv_file_path, index=False)

print("JSON data has been converted to CSV format using pandas.")

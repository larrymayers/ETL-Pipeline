import csv
import sys

def repair_csv(input_file, output_file, headings):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the headers to the output file
        writer.writerow(headings)
        
        for row in reader:
            # Ensure that the row has the same number of columns as the headers
            if len(row) != len(headings):
                # If there are missing values, fill them with empty strings
                if len(row) < len(headings):
                    row += [''] * (len(headings) - len(row))
                # If there are extraneous values, truncate the row
                elif len(row) > len(headings):
                    row = row[:len(headings)]
                
                # Write the cleaned row to the output file
                writer.writerow(row)
            else:
                writer.writerow(row)

if __name__ == "__main__":
    input_file = "D:\\Flexbooker\\FlexBooker_Customers_cleaned.csv"  # Replace with the path to your input CSV file
    output_file = "D:\\Flexbooker\\FlexBooker_Customers_repaired.csv"  # Replace with the path for the repaired CSV file
    # headings = [
    #     "CUSTOMER_ID", "EMAIL", "DATE_REGISTERED", "PARTNER_CODE", "USERNAME", "PASSWORD", 
    #     "CLUE", "HINT", "FIRST_NAME", "LAST_NAME", "DISPLAY_NAME", "FIRM_NAME", 
    #     "ADDRESS_LINE_1", "ADDRESS_LINE_2", "CITY", "STATE_PROVINCE", "POST_CODE", 
    #     "COUNTRY", "DAY_PHONE", "DAY_PHONE_EXT", "EVENING_PHONE", "FAX", "SMS_NBR", 
    #     "ADDRESS_TYPE_ID", "ADDRESS_ID", "SMS_OPT_IN_DATE", "SMS_OPT_OUT_DATE"
    # ]
    
    headings = [
       "ID","Name","Email","Group","Phone","ZIP","Country","State/Province","Customer Since","Billing Address","Shipping Address","Date of Birth","Tax VAT Number","Gender","Street Address",City,"Billing Firstname","Billing Lastname","Account Lock","Rewards Balance"
    ]
    try:
        repair_csv(input_file, output_file, headings)
        print(f"CSV file repaired and saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

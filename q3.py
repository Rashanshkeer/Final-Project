import pandas as pd

# Open the Excel file
file_path = 'rehospitalization.xlsx'

# Read all the sheets in the file
excel_data = pd.read_excel(file_path, sheet_name=None)

# Create a dictionary where the key is the sheet name and the value is the corresponding DataFrame
dataframes = {sheet: pd.DataFrame(data) for sheet, data in excel_data.items()}

# Print the names of the sheets to verify
print("Loaded sheets:")
for sheet in dataframes.keys():
    print(sheet)

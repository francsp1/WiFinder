import pandas as pd

# Read the CSV file, skipping lines with inconsistent field counts
data = pd.read_csv('airodump-01.csv', error_bad_lines=False)

# Modify the Manufacturer column to include the entire string within commas as one field
data['Manufacturer'] = data['Manufacturer'].apply(lambda x: ''.join(x.split(',')))

# Save the data to an Excel file
data.to_excel('output.xlsx', index=False)

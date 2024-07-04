import pandas as pd
import os

# Path to your Excel file
file_path = '/Users/bin/Desktop/Book1.xlsx'

# Load the Excel file
data = pd.read_excel(file_path)

# Set the first row as the header
data.columns = data.iloc[0]
data = data.drop(data.index[0])

# Convert 'Description' and 'Text (must exist)' columns to string
data['Description'] = data['Description'].astype(str)
data['Text (must exist)'] = data['Text (must exist)'].astype(str)

# Directory to save the output files
output_dir = '/Users/bin/Desktop/generate'
os.makedirs(output_dir, exist_ok=True)

# Iterate over each row in the DataFrame to create text files
for index, row in data.iterrows():
    filename = f"{row['Id']}_{row['Description'].replace(' ', '_').replace('/', '_')}.txt"
    file_path = os.path.join(output_dir, filename)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(row['Text (must exist)'])

print("Files have been created successfully.")

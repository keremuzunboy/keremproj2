import pandas as pd

# Specify the path to the CSV file
csv_file_path = '../veri/buyuk_veri_dosyasi.csv'

# Read the CSV file into a DataFrame
veri_df = pd.read_csv(csv_file_path)

# Print the first few rows of the DataFrame
print(veri_df.head())
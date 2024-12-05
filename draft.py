import pandas as pd

# Specify the filename (assumes the file is in the same directory)
parquet_file_name = '0000.parquet'  # Change this to your actual file name if needed

# Read the Parquet file into a DataFrame
try:
    df = pd.read_parquet(parquet_file_name)
    
    # Display the size of the dataset (rows and columns)
    print(f"Dataset size: {df.shape[0]} rows and {df.shape[1]} columns")
    
    # Display the number of NaN values in each column
    print("\nNaN values per column:")
    print(df.isna().sum())
    
    # Optionally display the first few rows of the DataFrame
    print("\nFirst few rows of the dataset:")
    print(df.head())

except Exception as e:
    print(f"Error reading Parquet file: {e}")

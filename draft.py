##This was used for exploring data 
import pandas as pd

parquet_file_name = '0000.parquet'  

try:
    df = pd.read_parquet(parquet_file_name)
    
    print(f"Dataset size: {df.shape[0]} rows and {df.shape[1]} columns")
    
    print("\nNaN values per column:")
    print(df.isna().sum())
    
    print("\nFirst few rows of the dataset:")
    print(df.head())

except Exception as e:
    print(f"Error reading Parquet file: {e}")

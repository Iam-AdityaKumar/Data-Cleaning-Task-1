import pandas as pd

# Use a raw string for the file path
file_path = r"C:\Users\anura\Downloads\Elevate Labs\Mall_Customers Datasets.csv"

# Print the file path to verify
# print("File path:", file_path)

# Load the dataset
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    print(df.head())
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except PermissionError:
    print(f"Error: Permission denied for {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Step 1: Handle missing values
# Check for missing values
print("\nMissing value counts:")
print(df.isnull().sum())

# Option 1: Drop rows with missing values
# Handle missing values (e.g., drop or fill)
# Option 1: Drop rows with missing values
df = df.dropna()

# Option 2: Fill missing values (if applicable)
# df['column_name'] = df['column_name'].fillna(value)
  
  
  # Step 2: Remove duplicate rows
  # Remove duplicate rows
print("\nDuplicate rows removed.")
df = df.drop_duplicates()


# Step 3: Standardize text values
# Standardize text values (e.g., Gender)
df['Gender'] = df['Gender'].str.lower()

# Step 4: Rename column headers
# Rename columns to be clean and uniform
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 5: Fix data types
# Convert 'age' to integer
df['age'] = df['age'].astype(int)

# Convert 'annual_income' to float
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(float)

# Step 6: Save the cleaned dataset
# Save the cleaned dataset
cleaned_file_path = "cleaned_Mall_Customers.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved to: {cleaned_file_path}")

# Step 7: Write a summary
summary = """
Summary of Changes:
- Removed duplicate rows.
- Handled missing values.
- Standardized text values.
- Renamed column headers.
- Fixed data types.
"""
print(summary)

import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())
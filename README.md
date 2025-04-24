# Data-Cleaning-Task-1
Cleaned dataset and Python script for Task 1
# Task 1: Data Cleaning and Preprocessing

## Objective
The objective of this task was to clean and preprocess a raw dataset to prepare it for analysis. The dataset used was **Mall Customer Segmentation Data**, downloaded from Kaggle.

## Steps Taken to Clean the Data
1. **Loaded the Dataset**:
   - Used Python's Pandas library to load the dataset (`pd.read_csv()`).
   - Verified the dataset was loaded successfully using `df.head()`.

2. **Handled Missing Values**:
   - Checked for missing values using `df.isnull().sum()`.
   - Dropped rows with missing values using `df.dropna()`.

3. **Removed Duplicate Rows**:
   - Removed duplicate rows using `df.drop_duplicates()`.

4. **Standardized Text Values**:
   - Converted the `Gender` column to lowercase using `df['Gender'].str.lower()`.

5. **Renamed Column Headers**:
   - Renamed column headers to be clean and uniform (e.g., lowercase, no spaces) using `df.columns.str.lower().str.replace(' ', '_')`.

6. **Fixed Data Types**:
   - Ensured numerical columns had the correct data types:
     - `age` as integer.
     - `annual_income_(k$)` as float.

7. **Saved the Cleaned Dataset**:
   - Saved the cleaned dataset as `cleaned_Mall_Customers.csv` using `df.to_csv()`.

## Summary of Changes Made
- Removed duplicate rows.
- Handled missing values by dropping rows with nulls.
- Standardized text values (e.g., `Gender` to lowercase).
- Renamed column headers for consistency.
- Fixed data types for numerical columns.

## Challenges Faced and Resolutions
1. **File Path Issues**:
   - Initially encountered errors due to incorrect file paths.
   - Resolved by using raw strings (`r"..."`) and verifying the path.

2. **Permission Errors**:
   - Encountered permission issues while accessing the file.
   - Resolved by ensuring proper file permissions and moving the file to a user-accessible directory.

3. **Understanding Pandas Functions**:
   - Initially unsure about how to handle missing values and rename columns.
   - Resolved by referring to Pandas documentation and online tutorials.

## Tools Used
- **Python**: Pandas library for data cleaning.
- **GitHub**: For version control and submission.

## Files Included
- `cleaned_Mall_Customers.csv`: The cleaned dataset after preprocessing.
- `py1.py`: Python script used for cleaning the dataset.

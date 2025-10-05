import pandas as pd
import numpy as np

# 1. Load Data
data = pd.read_csv("your_file.csv")

# Preview data
print(data.shape)         # rows, columns
print(data.dtypes)        # data types
print(data.head())        # first 5 rows

# -----------------------------------------------------
# 2. Missing Values
print("\nMissing Values:\n", data.isnull().sum())
# Example fixes:
# data = data.dropna()  # drop rows with NA
# data['col'] = data['col'].fillna(data['col'].median())  # impute with median

# -----------------------------------------------------
# 3. Duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
data = data.drop_duplicates()

# -----------------------------------------------------
# 4. Fix Data Types
# Example: convert date columns
# data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Example: categorical columns
# data['category'] = data['category'].astype('category')

# -----------------------------------------------------
# 5. Standardize Column Names
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

# -----------------------------------------------------
# 6. Outlier Detection
print("\nSummary Statistics:\n", data.describe())
# Example: remove extreme outliers in a numeric column
# q1 = data['price'].quantile(0.25)
# q3 = data['price'].quantile(0.75)
# iqr = q3 - q1
# lower = q1 - 1.5 * iqr
# upper = q3 + 1.5 * iqr
# data = data[(data['price'] >= lower) & (data['price'] <= upper)]

# -----------------------------------------------------
# 7. Fix Inconsistent Formats
# Example: strip spaces, make lowercase in text columns
# data['city'] = data['city'].str.strip().str.title()

# -----------------------------------------------------
# 8. Feature Engineering Prep
# Example: split or combine columns
# data['full_date'] = pd.to_datetime(data['year'].astype(str) + '-' + data['month'].astype(str) + '-01')

# Example: encode categories
# data = pd.get_dummies(data, columns=['room_type'], drop_first=True)

# -----------------------------------------------------
# 9. Validate Business Rules
# Example: age must be > 0
# data = data[data['age'] > 0]

# Example: rating <= 5
# data = data[data['rating'] <= 5]

# -----------------------------------------------------
# 10. Save Cleaned Data
data.to_csv("cleaned_file.csv", index=False)

print("\n✅ Data cleaning completed. Cleaned file saved as 'cleaned_file.csv'")



import pandas as pd
import numpy as np

# Sample dataset (AI-style dummy data)
data = {
    'Age': [25, np.nan, 30, 22, np.nan],
    'Salary': [50000, 60000, np.nan, 52000, 58000],
    'Experience': [1, 3, 4, np.nan, 2]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 2. Fill missing values (AI preprocessing step)

# Age -> fill with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Salary -> fill with median
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Experience -> fill with mode
df['Experience'].fillna(df['Experience'].mode()[0], inplace=True)

print("\nAfter Handling Missing Values:")
print(df)
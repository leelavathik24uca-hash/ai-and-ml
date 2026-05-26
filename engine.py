import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Sample dataset
data = {
    'Age': [25, 30, 35, None, 40],
    'Salary': [25000, 30000, 35000, 40000, None],
    'City': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -----------------------------
# 1. Handling missing values
# -----------------------------
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# -----------------------------
# 2. Label Encoding (Categorical → Numeric)
# -----------------------------
encoder = LabelEncoder()
df['City'] = encoder.fit_transform(df['City'])

# -----------------------------
# 3. Feature Engineering (New Feature)
# Example: Income per Age
# -----------------------------
df['Income_per_Age'] = df['Salary'] / df['Age']

# -----------------------------
# 4. Feature Scaling
# -----------------------------
scaler = StandardScaler()
df[['Age', 'Salary', 'Income_per_Age']] = scaler.fit_transform(
    df[['Age', 'Salary', 'Income_per_Age']]
)

print("\nProcessed Data (After Feature Engineering):")
print(df)
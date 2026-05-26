# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = {
    'Age': [20, 25, 30, 35, None, 40],
    'Salary': [20000, 25000, 30000, 35000, 40000, None],
    'Purchased': [0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Handle missing values (fill with mean)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

# 2. Split features and target
X = df[['Age', 'Salary']]
y = df['Purchased']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Feature scaling (standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nPreprocessed Training Data:")
print(X_train)

print("\nPreprocessed Test Data:")
print(X_test)
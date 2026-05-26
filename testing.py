from sklearn.model_selection import train_test_split

# Sample dataset (X = input features, y = output labels)
X = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 9]
]

y = [0, 0, 0, 0, 1, 1, 1, 1]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Print results
print("Training Data (X_train):")
print(X_train)

print("\nTesting Data (X_test):")
print(X_test)

print("\nTraining Labels (y_train):")
print(y_train)

print("\nTesting Labels (y_test):")
print(y_test)
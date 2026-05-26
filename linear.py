# Simple Linear Regression AI Program

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import numpy as np

# Sample dataset (X = hours studied, y = marks scored)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Output results
print("Test Data:", X_test.flatten())
print("Actual Values:", y_test)
print("Predicted Values:", y_pred)

# Model performance
error = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", error)

# Predict new value
new_data = np.array([[9]])
prediction = model.predict(new_data)
print("Prediction for 9 hours:", prediction[0])
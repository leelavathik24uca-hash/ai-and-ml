import numpy as np

# Input data (hours studied)
x = np.array([1, 2, 3, 4, 5])

# Output data (marks scored)
y = np.array([20, 40, 60, 80, 100])

# Simple AI model using formula y = wx
w = np.sum(x * y) / np.sum(x * x)

print("Training completed!")
print("Weight value:", w)

# Prediction
new_input = 6
prediction = w * new_input

print("Predicted marks for", new_input, "hours study =", prediction)
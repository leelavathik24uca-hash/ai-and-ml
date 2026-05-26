from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample dataset (AI feature data)
data = np.array([
    [100, 0.001],
    [200, 0.005],
    [300, 0.010],
    [400, 0.020]
])

print("Original Data:")
print(data)

# Create scaler
scaler = MinMaxScaler()

# Fit and transform data
normalized_data = scaler.fit_transform(data)

print("\nNormalized Data (0 to 1):")
print(normalized_data)
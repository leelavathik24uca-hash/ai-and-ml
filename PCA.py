# Simple Clustering Analysis using K-Means

from sklearn.cluster import KMeans
import numpy as np

# Sample data
data = np.array([
    [1, 2],
    [1, 4],
    [2, 3],
    [8, 7],
    [9, 8],
    [8, 9]
])

# Create K-Means model
model = KMeans(n_clusters=2, random_state=0)

# Train the model
model.fit(data)

# Predict cluster labels
labels = model.labels_

# Print results
print("Data Points:")
print(data)

print("\nCluster Labels:")
print(labels)

print("\nCluster Centers:")
print(model.cluster_centers_)
from sklearn import tree

# Sample dataset (features: [age, income])
# Label: 0 = No Buy, 1 = Buy

X = [
    [22, 25000],
    [25, 30000],
    [47, 60000],
    [52, 65000],
    [46, 70000],
    [23, 20000]
]

y = [0, 0, 1, 1, 1, 0]

# Create Decision Tree Classifier
model = tree.DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict new data
prediction = model.predict([[30, 40000]])

if prediction[0] == 1:
    print("Customer will BUY")
else:
    print("Customer will NOT BUY")
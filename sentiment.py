from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
texts = [
    "I love this movie",
    "This is amazing",
    "I feel very happy",
    "What a great experience",
    "I hate this",
    "This is bad",
    "I feel sad",
    "Terrible experience"
]

# Labels: 1 = Positive, 0 = Negative
labels = [1, 1, 1, 1, 0, 0, 0, 0]

# Convert text into numerical data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test data
test_text = [
    "I love this product",
    "This is very bad",
    "What an amazing day",
    "I feel terrible"
]

# Transform test data
X_test = vectorizer.transform(test_text)

# Predict sentiment
predictions = model.predict(X_test)

# Output results
for text, pred in zip(test_text, predictions):
    sentiment = "Positive 😊" if pred == 1 else "Negative 😡"
    print(f"{text} ---> {sentiment}")
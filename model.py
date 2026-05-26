from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Sample dataset (text + label)
texts = [
    "Free money offer just for you",
    "Win a lottery now",
    "Hello how are you",
    "Let's meet tomorrow",
    "Congratulations you won a prize",
    "Are you coming to class today",
    "Click here to claim reward",
    "Good morning have a nice day"
]

labels = [
    "spam",
    "spam",
    "not spam",
    "not spam",
    "spam",
    "not spam",
    "spam",
    "not spam"
]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=42
)

# Create pipeline (vectorizer + model)
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Test prediction
test_messages = [
    "Win free cash now",
    "Are we meeting today?"
]

predictions = model.predict(test_messages)

# Output results
for msg, label in zip(test_messages, predictions):
    print(f"Message: {msg}")
    print(f"Prediction: {label}")
    print("-" * 40)
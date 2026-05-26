from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample dataset (you can expand this)
messages = [
    "Win money now", "Hello how are you", "Free prize claim now",
    "Are we meeting today?", "Congratulations you won a lottery",
    "Let's have lunch", "Click this link to get cash", "Good morning",
    "Urgent offer just for you", "See you tomorrow"
]

labels = [
    "spam", "ham", "spam",
    "ham", "spam",
    "ham", "spam", "ham",
    "spam", "ham"
]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    messages, labels, test_size=0.3, random_state=42
)

# Build AI model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Test predictions
test_messages = [
    "Win a free cash prize now",
    "Are you coming to college?",
    "Claim your free offer"
]

predictions = model.predict(test_messages)

# Output results
for msg, label in zip(test_messages, predictions):
    print(f"{msg} ---> {label}")
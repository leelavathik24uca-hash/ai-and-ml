# Simple AI Program for Text Preprocessing

# Sample text
text = "Hello! Welcome to AI and Machine Learning. AI is powerful."

# Step 1: Convert to lowercase
text = text.lower()

# Step 2: Remove punctuation
import string

for p in string.punctuation:
    text = text.replace(p, "")

# Step 3: Tokenization (split words)
words = text.split()

# Step 4: Remove stopwords
stopwords = ["is", "to", "and", "the", "a"]

filtered_words = []

for word in words:
    if word not in stopwords:
        filtered_words.append(word)

# Step 5: Display output
print("Original Text:")
print("Hello! Welcome to AI and Machine Learning. AI is powerful.")

print("\nPreprocessed Text:")
print(filtered_words)
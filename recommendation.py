# Simple Recommendation System using Python

# Sample movie data
movies = {
    "Action": ["KGF", "Leo", "Vikram"],
    "Comedy": ["Boss Engira Bhaskaran", "Doctor", "Jailer"],
    "Drama": ["96", "Master", "Soorarai Pottru"]
}

# Ask user interest
print("Movie Categories: Action, Comedy, Drama")
choice = input("Enter your favorite category: ")

# Recommend movies
if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print(movie)
else:
    print("Category not found")
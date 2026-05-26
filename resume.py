from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Job description
job_description = """
We are looking for a Python developer with knowledge of machine learning,
data analysis, pandas, numpy, and scikit-learn. Experience in AI projects is required.
"""

# Sample resumes
resumes = [
    """Python developer with experience in machine learning, pandas, numpy and AI projects.""",
    
    """Web developer with HTML, CSS, JavaScript and React experience.""",
    
    """Data scientist skilled in Python, scikit-learn, machine learning and data analysis.""",
    
    """Java developer with Spring Boot and backend development experience."""
]

# Combine job description and resumes
documents = [job_description] + resumes

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Compute similarity between job description and resumes
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Rank resumes
ranked_resumes = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True)

print("🔍 Resume Ranking Based on Job Match:\n")

for idx, score in ranked_resumes:
    print(f"Resume {idx+1}: Score = {score:.2f}")
    print(resumes[idx])
    print("-" * 60)
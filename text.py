from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
textfile=["good", "apple", "was","good"]
word_count = cv.fit_transform(textfile)
similarity_score = cosine_similarity(word_count)
print(similarity_score)
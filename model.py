from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jobs = {
    "AI Engineer": "Python Machine Learning Deep Learning AI",
    "Data Analyst": "Python SQL Excel Statistics Analytics",
    "UI UX Designer": "Design Creativity Figma User Experience",
    "Product Manager": "Communication Planning Business Leadership"
}

def predict_jobs(user_skills):
    user_text = " ".join(user_skills)

    all_texts = [user_text] + list(jobs.values())

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    results = sorted(
        zip(jobs.keys(), similarity),
        key=lambda x: x[1],
        reverse=True
    )

    return results[:3]
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from questions import questions

# model load
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Simple AI Mock Interview\n") 

for q, expected in questions.items():

    print("Question:", q)
    user_answer = input("Your answer: ")

    # embeddings
    user_vec = model.encode([user_answer])
    expected_vec = model.encode([expected])

    # similarity
    score = cosine_similarity(user_vec, expected_vec)[0][0]

    print("Similarity score:", round(score, 2))

    if score > 0.7:
        print("Result: Answer looks correct\n")
    elif score > 0.4:
        print("Result: Partially correct\n")
    else:
        print("Result: Not correct\n")
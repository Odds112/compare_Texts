from sentence_transformers import SentenceTransformer, util

def compare_texts(text1, text2):
    # Загрузка предварительно обученной модели SentenceTransformer
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(embeddings1, embeddings2)

    similarity_score = cosine_similarity[0][0].item()

    return similarity_score

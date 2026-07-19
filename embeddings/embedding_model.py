from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingModel:
    """
    Generate embeddings and calculate semantic similarity.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def encode(self, text: str):
        return self.model.encode(text)

    def similarity(self, text1: str, text2: str):

        embedding1 = self.encode(text1)
        embedding2 = self.encode(text2)

        score = cosine_similarity(
            [embedding1],
            [embedding2]
        )[0][0]

        return round(score * 100, 2)
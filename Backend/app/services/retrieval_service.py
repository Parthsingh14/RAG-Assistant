from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorestore.pinecone_store import PineconeStore


class RetrievalService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.pinecone_store = PineconeStore()

    def retrieve(self, question: str, top_k: int = 3):

        query_vector = self.embedding_service.embed_query(question)

        results = self.pinecone_store.search(
            query_vector=query_vector,
            top_k=top_k
        )

        return results
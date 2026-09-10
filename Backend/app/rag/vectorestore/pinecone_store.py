import os

from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

class PineconeStore:

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("PINECONE_API_KEY")

        if not api_key:
            raise ValueError("PINECONE_API_KEY environment variable is not set.")

        self.client = Pinecone(api_key=api_key)
        self.index_name = "rag-knowledge-assistant"
        self.index = self.client.Index(self.index_name)

    def upsert_vectors(self, vectors):
        self.index.upsert(vectors = vectors)

    def search(self, query_vector: list[float], top_k: int = 3):
        results = self.index.query(
            vector = query_vector,
            top_k = top_k,
            include_metadata = True
        )

        return [
            {
                "id": match.id,
                "score": match.score,
                "document_id": match.metadata.get("document_id"),
                "filename": match.metadata.get("filename"),
                "page_number": match.metadata.get("page_number"),
                "chunk_index": match.metadata.get("chunk_index"),
                "text": match.metadata.get("text")
            } for match in results.matches
        ]

    def delete_all(self):
        self.index.delete(delete_all=True)
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
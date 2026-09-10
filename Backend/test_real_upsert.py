from dotenv import load_dotenv
load_dotenv()
from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorestore.pinecone_store import PineconeStore

embedding_service = EmbeddingService()
pinecone_store = PineconeStore()

text = "Employees receive 20 days of annual leave."
embedded_vector = embedding_service.embed_query(text)

test_vector = {
    "id": "test_chunk_001",
    "values": embedded_vector,
    "metadata": {
        "document_id": "test_document",
        "filename": "test.txt",
        "chunk_id": 0,
        "text": text
    }
}

pinecone_store.upsert_vectors([test_vector])
stats = pinecone_store.index.describe_index_stats()
print("Index stats:")
print(stats)
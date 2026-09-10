from app.rag.vectorestore.pinecone_store import PineconeStore

pinecone_store = PineconeStore()

test_vector = {
    "id": "test_chunk_001",
    "values": [0.1] * 3072,
    "metadata": {
        "document_id": "test_document",
        "filename": "test.txt",
        "chunk_id": 0,
        "text": "This is a test chunk."
    }
}

pinecone_store.upsert_vectors([test_vector])

print("Vector upserted successfully.")

stats = pinecone_store.index.describe_index_stats()

print("Index stats:")
print(stats)
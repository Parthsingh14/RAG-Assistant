from app.rag.vectorestore.pinecone_store import PineconeStore


pinecone_store = PineconeStore()

print("PineconeStore initialized successfully.")
print("Index name:", pinecone_store.index_name)

print("Index stats:")
print(pinecone_store.index.describe_index_stats())
from dotenv import load_dotenv

from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorestore.pinecone_store import PineconeStore

load_dotenv()

embedding_service = EmbeddingService()
pinecone_store = PineconeStore()

query = "What subjects are included in the GATE 2027 Computer Science syllabus?"

query_vector = embedding_service.embed_query(query)
results = pinecone_store.search(query_vector=query_vector, top_k=5)
for result in results:
    print("\n--- Result ---")
    print("ID:", result["id"])
    print("Score:", result["score"])
    print("Filename:", result["filename"])
    print("Page:", result["page_number"])
    print("Chunk:", result["chunk_index"])
    print("Text:", result["text"])
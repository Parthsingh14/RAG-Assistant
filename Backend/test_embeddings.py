from dotenv import load_dotenv

load_dotenv()

from app.rag.embeddings.embedding_service import EmbeddingService


embedding_service = EmbeddingService()

texts = [
    "Employees receive 20 days of annual leave.",
    "The company provides health insurance.",
    "Employees may work remotely three days per week.",
]

vectors = embedding_service.embed_documents(texts)

print("Number of vectors:", len(vectors))

for index, vector in enumerate(vectors):
    print(f"Vector {index + 1} dimensions:", len(vector))
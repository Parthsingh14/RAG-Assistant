from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from app.rag.embeddings.embedding_service import EmbeddingService


embedding_service = EmbeddingService()

text = "Employees receive 20 days of annual leave."

vector = embedding_service.embed_query(text)

print("Vector type:", type(vector))
print("Vector dimensions:", len(vector))
print("First 5 values:", vector[:5])
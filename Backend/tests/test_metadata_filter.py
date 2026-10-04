from dotenv import load_dotenv
load_dotenv()
from app.services.retrieval_service import RetrievalService


retrieval_service = RetrievalService()

question = "What is my GATE score?"

filter = {
    "filename": {
        "$eq": "Main Resume.pdf"
    }
}

results = retrieval_service.retrieve(
    question=question,
    top_k=5,
    filter=filter
)

print("=" * 50)
print(f"Question: {question}")
print("Filter: Main Resume.pdf")
print("=" * 50)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print(f"Score: {result['score']}")
    print(f"File: {result['filename']}")
    print(f"Page: {result['page_number']}")
    print(f"Chunk: {result['chunk_index']}")
    print(f"Text: {result['text']}")
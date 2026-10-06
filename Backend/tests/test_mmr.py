from dotenv import load_dotenv
load_dotenv()
from app.services.retrieval_service import RetrievalService



retrieval_service = RetrievalService()

question = "What is the syllabus of GATE?"

results = retrieval_service.retrieve_mmr(
    question=question,
    k=3,
    fetch_k=8,
    lambda_mult=0.5
)

print("=" * 70)
print(f"Question: {question}")
print("Strategy: MMR")
print("=" * 70)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print(f"Score: {result['score']}")
    print(f"File: {result['filename']}")
    print(f"Chunk: {result['chunk_index']}")
    print(f"Text: {result['text']}")
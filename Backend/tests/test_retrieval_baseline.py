from dotenv import load_dotenv
load_dotenv()
from app.services.retrieval_service import RetrievalService
retrieval_service = RetrievalService()

questions = [
    "What is my GATE score?",
    # "Give me the full syllabus of GATE.",
    # "Who is the PM of Pakistan?",
]

for question in questions:
    print("=" * 50)
    print(f"Question: {question}")
    print("=" * 50)

    results = retrieval_service.retrieve(question, top_k=5)

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}")
        print(f"Score: {result['score']}")
        print(f"File: {result['filename']}")
        print(f"Page: {result['page_number']}")
        print(f"Chunk: {result['chunk_index']}")
        print(f"Text: {result['text']}")
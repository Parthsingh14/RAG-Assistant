from dotenv import load_dotenv
load_dotenv()

from app.services.retrieval_service import RetrievalService


retrieval_service = RetrievalService()

questions = [
    "What is my GATE score?",
    "What is the syllabus of GATE?",
    "Who is the PM of Pakistan?",
]

top_k_values = [1, 3, 5, 8]

for question in questions:

    print("\n" + "=" * 70)
    print(f"QUESTION: {question}")
    print("=" * 70)

    for top_k in top_k_values:

        print(f"\n--- TOP K = {top_k} ---")

        results = retrieval_service.retrieve(
            question=question,
            top_k=top_k
        )

        for i, result in enumerate(results, start=1):
            print(
                f"{i}. "
                f"Score={result['score']:.4f} | "
                f"File={result['filename']} | "
                f"Chunk={result['chunk_index']}"
            )
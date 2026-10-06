from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorestore.pinecone_store import PineconeStore
import numpy as np


class RetrievalService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.pinecone_store = PineconeStore()

    def retrieve(self, question: str, top_k: int = 3, filter: dict | None = None):

        query_vector = self.embedding_service.embed_query(question)

        results = self.pinecone_store.search(
            query_vector=query_vector,
            top_k=top_k,
            filter = filter
        )

        return results


    def retrieve_mmr(
        self,
        question: str,
        k: int = 3,
        fetch_k: int = 8,
        lambda_mult: float = 0.5,
        filter: dict | None = None
    ):
        query_vector = self.embedding_service.embed_query(question)

        candidates = self.pinecone_store.search(
            query_vector=query_vector,
            top_k=fetch_k,
            filter=filter,
            include_values=True
        )

        if not candidates:
            return []

        selected = []
        remaining = candidates.copy()

        # First result: most relevant to the query
        first = max(remaining, key=lambda result: result["score"])
        selected.append(first)
        remaining.remove(first)

        while remaining and len(selected) < k:
            best_candidate = None
            best_score = float("-inf")

            selected_vectors = [
                np.array(result["values"])
                for result in selected
            ]

            for candidate in remaining:
                candidate_vector = np.array(candidate["values"])

                query_similarity = candidate["score"]

                diversity_similarity = max(
                    np.dot(candidate_vector, selected_vector)
                    / (
                        np.linalg.norm(candidate_vector)
                        * np.linalg.norm(selected_vector)
                    )
                    for selected_vector in selected_vectors
                )

                mmr_score = (
                    lambda_mult * query_similarity
                    - (1 - lambda_mult) * diversity_similarity
                )

                if mmr_score > best_score:
                    best_score = mmr_score
                    best_candidate = candidate

            selected.append(best_candidate)
            remaining.remove(best_candidate)

        for result in selected:
            result.pop("values", None)

        return selected
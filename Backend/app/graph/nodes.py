from app.graph.state import GraphState
from app.services.retrieval_service import RetrievalService


def create_retrieval_node(retrieval_service: RetrievalService):

    def retrieve_documents(state: GraphState) -> dict:
        question = state.get("rewritten_question") or state["question"]

        results = retrieval_service.retrieve(question)

        return {
            "documents": results
        }

    return retrieve_documents



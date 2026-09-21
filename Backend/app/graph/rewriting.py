from app.graph.state import GraphState
from app.rag.llm.llm_service import LLMService

def create_rewriting_node(llm_service: LLMService):

    def rewrite_question(state: GraphState) -> dict:
        question = state["question"]
        documents = state["documents"]
        retry_count = state["retry_count"]

        context = ""
        for index, document in enumerate(documents, start=1):
            context = context + f"Chunk_{index} -> {document['text']}" + "\n\n"

        prompt = f"""
            You are a rewriting question agent. 
            The retrieved content is not relevant enough for the user question.
            You have to rewrite the question for better retrieval.

            User_original_question: {question},
            Retrieved_context: {context}

            Only return the re-written question.
        """

        response = llm_service.generate(prompt)
        rewritten_question = response.content.strip()

        return {
            "rewritten_question": rewritten_question,
            "retry_count": retry_count+1
        }
    return rewrite_question
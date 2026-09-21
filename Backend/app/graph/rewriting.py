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
                You are a query rewriting agent in a RAG system.

                The initial retrieval did not provide sufficiently relevant documents.
                Rewrite the user's question to improve semantic retrieval.

                Rules:
                1. Preserve the original user's intent.
                2. Do not change, replace, or invent important entities, names, exams,
                subjects, products, people, or other key terms from the original question.
                3. Do not make the question about a different topic just because the
                retrieved context contains information about that topic.
                4. Make the query clearer, more specific, and easier for a semantic
                search system to retrieve.
                5. Use the retrieved context only to identify possible missing terminology
                or clarify what information may be needed.
                6. Return only the rewritten question. Do not provide an explanation.

                Original user question:
                {question}

                Retrieved context:
                {context}

                Rewritten question:
            """

        response = llm_service.generate(prompt)
        rewritten_question = response.content.strip()

        return {
            "rewritten_question": rewritten_question,
            "retry_count": retry_count+1
        }
    return rewrite_question
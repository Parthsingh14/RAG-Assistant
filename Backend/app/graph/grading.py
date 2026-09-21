from app.graph.state import GraphState
from app.rag.llm.llm_service import LLMService


def create_grading_node(llm_service: LLMService):

    def grade_documents(state: GraphState) -> dict:
        question = state["question"]
        documents = state["documents"]

        # Build the retrieved context here
        context = ""
        for index , doc in enumerate(documents, start=1):
            retrieved_context = f"Chunk_{index} -> {doc.get('text')}"
            context = context + retrieved_context + "\n\n"

        # Build the grading prompt here
        prompt = f"""You are a document relevance grader.

            Determine whether the retrieved context contains information relevant to answering the user's question.

            Reply with exactly one word:
            - Yes — if the retrieved context is relevant.
            - No — if the retrieved context is not relevant.

            Question:
            {question}

            Retrieved context:
            {context}
        """


        # Call the LLM here
        response = llm_service.generate(prompt=prompt)
        answer = response.content.strip().lower()
        
        # Convert the response to True / False
        if answer == "yes":
            documents_relevant = True
        elif answer == "no":
            documents_relevant = False
        else:
            raise ValueError("Unexpected grading response")



        # Return the state update
        return {
            "documents_relevant": documents_relevant
        }

    return grade_documents
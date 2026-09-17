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
            context = context + retrieved_context

        # Build the grading prompt here
        prompt = f"""You are a grading node. Your job is to return the answer in only 'Yes' or 'No' in the terms of relevant. I am providing the user question and the retrived content. If the retrieved chunks are relevant then reply 'Yes' then 'No'. 
        Question - {question}
        retrieved_context - {context}
        'Yes' or 'No'."""


        # Call the LLM here
        result = llm_service.generate(prompt=prompt)
        
        # Convert the response to True / False
        ans = True
        if result is 'No':
            ans = False



        # Return the state update
        return {
            
        }

    return grade_documents
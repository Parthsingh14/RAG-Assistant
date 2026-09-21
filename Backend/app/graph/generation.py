from app.graph.state import GraphState
from app.rag.llm.llm_service import LLMService
from app.rag.prompts.rag_prompt import RAG_PROMPT

def create_generation_node(llm_service: LLMService):

    def build_context(results):
        context_parts = []
        sources = []

        for index,result in enumerate(results, start=1):
            text = result.get('text')

            if text:
                context_parts.append(f"--- Document Chunk {index} ---\n{text}")

            sources.append({
                "filename": result.get('filename'),
                "page_number": result.get('page_number')
            })


        context = "\n\n".join(context_parts)
        return context, sources

    def generation_node(state: GraphState) -> dict:
        question = state['question']
        documents = state['documents']

        context , sources = build_context(documents)
        prompt = RAG_PROMPT.invoke({
            "context": context,
            "question": question
        })

        response = llm_service.generate(prompt)
        answer = response.content.strip()

        return {
            "answer": answer,
            "sources": sources
        }


    return generation_node
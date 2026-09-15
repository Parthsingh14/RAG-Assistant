from app.services.retrieval_service import RetrievalService
from app.rag.llm.llm_service import LLMService
from app.rag.prompts.rag_prompt import RAG_PROMPT


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

class ChatService:
    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.llm_service = LLMService()

    def get_answer(self,question:str):

        results = self.retrieval_service.retrieve(question=question, top_k=3)
        context, sources = build_context(results)

        prompt = RAG_PROMPT.invoke({
            "context": context,
            "question": question
        })

        response = self.llm_service.generate(prompt)

        return {
            "answer": response.content,
            "sources": sources
        }
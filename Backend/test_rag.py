from dotenv import load_dotenv

from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorestore.pinecone_store import PineconeStore
from app.rag.prompts.rag_prompt import RAG_PROMPT
from app.rag.llm.llm_service import LLMService

load_dotenv()

def build_context(results):
    context_parts = []
    sources = []

    for index, result in enumerate(results, start=1):
        text = result.get("text")

        if text:
            context_parts.append(
                f"--- Document Chunk {index} ---\n{text}"
            )

        sources.append(
            {
                "filename": result.get("filename"),
                "page_number": result.get("page_number")
            }
        )

    context = "\n\n".join(context_parts)

    return context, sources


question = "What is the syllabus of NEET exam?"

embedding_service = EmbeddingService()
pinecone_store = PineconeStore()
llm_service = LLMService()

query_vector = embedding_service.embed_query(question)

results = pinecone_store.search(query_vector=query_vector, top_k=3)

context , sources = build_context(results)

prompt = RAG_PROMPT.invoke({
    "context": context,
    "question": question
})

response = llm_service.generate(prompt)

print("\n===== QUESTION =====")
print(question)

print("\n===== ANSWER =====")
print(response.content)

print("\n===== SOURCES =====")
print(sources)
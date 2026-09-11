from app.rag.prompts.rag_prompt import RAG_PROMPT

print(RAG_PROMPT.invoke({"context": "Heey swatty", "question": "Date pe chalog kta"}))
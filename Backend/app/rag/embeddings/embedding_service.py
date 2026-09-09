from langchain_google_genai import GoogleGenerativeAIEmbeddings


class EmbeddingService:

    def __init__(self):
        self.embedding_model =  GoogleGenerativeAIEmbeddings(
            model = "gemini-embedding-2"
        )

    def embed_query(self, text: str) -> list[float]:
        return self.embedding_model.embed_query(text)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.embedding_model.embed_documents(texts)
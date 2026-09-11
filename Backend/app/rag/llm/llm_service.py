from langchain_google_genai import ChatGoogleGenerativeAI

class LLMService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
        )

    def generate(self,prompt:str):
        return self.llm.invoke(prompt)
        
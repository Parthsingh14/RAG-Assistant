from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]

class Source(BaseModel):
    filename: str | None
    page_number: int | None
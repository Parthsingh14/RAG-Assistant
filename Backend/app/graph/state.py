from typing import TypedDict

class RetrievedDocument(TypedDict):
    id: str
    score: float
    document_id: str | None
    filename: str | None
    page_number: int | None
    chunk_index: int | None
    text: str | None


class GraphState(TypedDict, total=False):
    question: str
    documents: list[RetrievedDocument]
    documents_relevant: bool
    rewritten_question: str
    answer: str
    sources: list[dict]
    retry_count: int
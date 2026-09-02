from pathlib import Path

from app.rag.loaders.pdf_loader import load_pdf
from app.rag.loaders.docx_loader import load_docx
from app.rag.loaders.txt_loader import load_txt
from app.rag.splitters.text_splitter import split_documents

def ingest_documents(file_path: str):

    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".pdf":
        documents = load_pdf(file_path)
    elif file_extension == ".docx":
        documents = load_docx(file_path)
    elif file_extension == ".txt":
        documents = load_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    chunks = split_documents(documents)
    return chunks

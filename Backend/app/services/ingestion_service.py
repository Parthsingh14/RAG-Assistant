from pathlib import Path
import uuid

from app.rag.loaders.pdf_loader import load_pdf
from app.rag.loaders.docx_loader import load_docx
from app.rag.loaders.txt_loader import load_txt
from app.rag.splitters.text_splitter import split_documents
from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorestore.pinecone_store import PineconeStore

def ingest_documents(file_path: str):

    filename = Path(file_path).name
    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".pdf":
        documents = load_pdf(file_path)
    elif file_extension == ".docx":
        documents = load_docx(file_path)
    elif file_extension == ".txt":
        documents = load_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    document_id = str(uuid.uuid4())

    for document in documents:
        document.metadata["document_id"] = document_id
        document.metadata["filename"] = filename

    chunks = split_documents(documents)

    texts = [chunk.page_content for chunk in chunks]

    embedding_service = EmbeddingService()
    pinecone_store = PineconeStore()

    embeddings = embedding_service.embed_documents(texts)
    vectors = []

    for i, chunk in enumerate(chunks):
        vector = {
            "id": f"{chunk.metadata['document_id']}_chunk_{i}",
            "values": embeddings[i],
            "metadata": {
                "document_id": chunk.metadata["document_id"],
                "filename": chunk.metadata["filename"],
                "page_number": chunk.metadata.get("page"),
                "chunk_index": i,
                "text": chunk.page_content
            }

        }
        vectors.append(vector)

    pinecone_store.upsert_vectors(vectors)


    return {
        "document_id": document_id,
        "filename": filename,
        "chunks_created": len(chunks),
        "vectors_stored": len(vectors)
    }
        

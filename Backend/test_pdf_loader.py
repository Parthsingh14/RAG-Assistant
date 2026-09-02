from app.rag.loaders.pdf_loader import load_pdf
from app.rag.splitters.text_splitter import split_documents

file_path = "test_data/syllabus.pdf"

documents = load_pdf(file_path)

chunks = split_documents(documents)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks[:5]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk.page_content)
    print("Metadata:", chunk.metadata)
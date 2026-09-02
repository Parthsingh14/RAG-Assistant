from app.rag.loaders.pdf_loader import load_pdf

file_path = "test_data/syllabus.pdf"

documents = load_pdf(file_path)

print(f"Number of documents: {len(documents)}")

for document in documents:
    print("\n --- Documents ---")
    print(document)
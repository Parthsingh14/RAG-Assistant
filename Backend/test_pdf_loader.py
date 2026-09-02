from app.services.ingestion_service import ingest_documents

file_path = "test_data/syllabus.pdf"
chunks = ingest_documents(file_path)
print("Number of chunks:", len(chunks))
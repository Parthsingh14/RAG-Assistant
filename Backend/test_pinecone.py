import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")

if not api_key:
    raise ValueError("PINECONE_API_KEY environment variable is not set.")

pc = Pinecone(api_key=api_key)

index_name = "rag-knowledge-assistant"
dimension = 3072

existing_indexes = [index.name for index in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name = index_name,
        dimension = dimension,
        metric = "cosine",
        spec = ServerlessSpec(
            cloud = "aws",
            region = "us-east-1",
        )
    )

    print(f"Created index:  {index_name}")
else:
    print(f"Index '{index_name}' already exists.")
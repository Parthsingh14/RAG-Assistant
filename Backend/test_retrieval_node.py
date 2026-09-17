from dotenv import load_dotenv
load_dotenv()
from app.graph.nodes import create_retrieval_node
from app.services.retrieval_service import RetrievalService

# Create your existing RetrievalService here
retrieval_service = RetrievalService()

# Create the actual graph node
retrieval_node = create_retrieval_node(retrieval_service)

# Initial graph state
state = {
    "question": "What is the GATE CS syllabus?",
    "retry_count": 0
}

# Execute the node
result = retrieval_node(state)

print(result)
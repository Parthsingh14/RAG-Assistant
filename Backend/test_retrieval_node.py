from dotenv import load_dotenv
load_dotenv()

from app.graph.nodes import create_retrieval_node
from app.services.retrieval_service import RetrievalService
from app.rag.llm.llm_service import LLMService
from app.graph.grading import create_grading_node
from app.graph.rewriting import create_rewriting_node

# Create your existing RetrievalService here
retrieval_service = RetrievalService()
llm_service = LLMService()

# Create the actual graph node
retrieval_node = create_retrieval_node(retrieval_service)
grading_node = create_grading_node(llm_service)
rewriting_node = create_rewriting_node(llm_service)

# Initial graph state
state = {
    "question": "What is the GATE CS syllabus?",
    "retry_count": 0
}

# Execute the retrival node
result = retrieval_node(state)

#Updated the state
state.update(result)


print("State after retrieval:")
print(state)


grade = grading_node(state)

state.update(grade)

print("\nState after grading:")
print(state)

rewritten = rewriting_node(state)
state.update(rewritten)

print("\n\nState after Re-WRITING ")
print(state)
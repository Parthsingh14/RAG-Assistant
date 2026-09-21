from dotenv import load_dotenv
load_dotenv()

from app.graph.graph import create_graph

graph = create_graph()

result = graph.invoke({
    "question": "What is the Neet syllabus?",
    "retry_count": 0
})

print("\nFinal result:")
print(result)
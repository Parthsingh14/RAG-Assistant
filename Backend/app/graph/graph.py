from langgraph.graph import START,END, StateGraph

from app.graph.state import GraphState
from app.graph.nodes import create_retrieval_node
from app.graph.grading import create_grading_node
from app.graph.rewriting import create_rewriting_node
from app.graph.generation import create_generation_node

from app.graph.edges import (
    route_after_grading,
    route_after_rewriting
)

from app.services.retrieval_service import RetrievalService
from app.rag.llm.llm_service import LLMService

def fallback_node(state: GraphState) -> dict:
    return {
        "answer": "I couldn't find enough relevant information in the provided documents to answer this question.",
        "sources": []
    }

def create_graph():
    # Create services
    retrieval_service = RetrievalService()
    llm_service = LLMService()

    # Create nodes
    retrieval_node = create_retrieval_node(retrieval_service)
    grading_node = create_grading_node(llm_service)
    rewriting_node = create_rewriting_node(llm_service)
    generation_node = create_generation_node(llm_service)

    # Create StateGraph
    workflow = StateGraph(GraphState)

    # Register nodes
    workflow.add_node("retrieve", retrieval_node)
    workflow.add_node("grade", grading_node)
    workflow.add_node("rewrite", rewriting_node)
    workflow.add_node("generate", generation_node)
    workflow.add_node("fallback", fallback_node)

    # Add edges
    workflow.add_edge(START,"retrieve")
    workflow.add_edge("retrieve", "grade")
    workflow.add_conditional_edges(
        "grade",
        route_after_grading,
        {
            "generate": "generate",
            "rewrite": "rewrite",
        }
        )
    workflow.add_conditional_edges(
    "rewrite",
    route_after_rewriting,
    {
        "retrieve": "retrieve",
        "fallback": "fallback",
    }
)
    workflow.add_edge("generate", END)
    workflow.add_edge("fallback", END)

    # Compile graph
    graph = workflow.compile()
    
    return graph


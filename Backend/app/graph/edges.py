from app.graph.state import GraphState

def route_after_grading(state: GraphState) -> str:
    if state["documents_relevant"]:
        return "generate"

    return "rewrite"

def route_after_rewriting(state: GraphState) -> str:
    if state["retry_count"] <=1:
        return "retrieve"
    return "fallback"
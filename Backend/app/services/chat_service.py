from app.graph.graph import create_graph


class ChatService:
    def __init__(self):
        self.graph = create_graph()

    def get_answer(self,question:str):

        results = self.graph.invoke({
            "question": question,
            "retry_count": 0
        })


        return {
            "answer": results["answer"],
            "sources": results.get("sources", [])
        }
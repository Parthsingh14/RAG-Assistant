"use client";

import { useEffect, useState } from "react";

export default function Home() {
  
  //health status state
  const [status,setStatus] = useState("");
  const [healthLoading,setHealthLoading] = useState(true);
  const [error,setError] = useState("");

  //chat state
  const [question,setQuestion] = useState("")
  const [answer, setAnswer] = useState("")
  const [sources, setSources] = useState<
              {
                filename: string | null
                page_number: number | null
              }[]
              >([])
  const [chatLoading, setChatLoading] = useState(false)
  const [chatError, setChatError] = useState("")



  const sendMessage  = async (question: string) => {
    try{
      
      if(!question.trim()){
        throw new Error("Input field required")
      }
      setChatLoading(true)
      setChatError("")

      const payload = {
        "question": question.trim()
      }

      const response = await fetch("http://127.0.0.1:8000/chat/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      })
      if(!response.ok){
        throw new Error("Backend request failed");
      }

      const data = await response.json();
      setAnswer(data.answer)
      setSources(data.sources)

    }
    catch(err){
        setChatError("Issue")
    }
    finally{
      setChatLoading(false)
    }
  }



  //Checking backend status
  useEffect(()=>{
    const checkBackend = async () => {
      try{
        const response = await fetch("http://127.0.0.1:8000/health");
        if(!response.ok){
          throw new Error("Backend request failed");
        }

        const data = await response.json();
        setStatus(data.status);
      } catch (err) {
        setError("Could not connect to backend");
      } finally {
        setHealthLoading(false);
      }
    };

    checkBackend();

  },[])


  return (
    <main>
       <h1>RAG Knowledge Assistant</h1>

       {healthLoading && (
        <p>Connecting to backend...</p>
       )}

       {!healthLoading && error && (
        <p>{error}</p>
       )}

       {!healthLoading && !error && (
        <section>
          <p>Backend status: {status}</p>

          <div>
            <input value={question} onChange={(e)=> setQuestion(e.target.value)} placeholder="Ask a question..." />
            <button onClick={()=> sendMessage(question)} disabled={chatLoading}>
              {chatLoading ? "Thinking...": "Send"}
            </button>
          </div>

          {chatError && (
            <p>{chatError}</p>
          )}

          {answer && (
            <div>
              <h2>Answer</h2>
              <p>{answer}</p>
            </div>
          )}

          {sources.length > 0 && (
            <div>
              <h3>Sources</h3>
              {sources.map((source,index)=>(
                <p key={index}>
                  {source.filename} -- Page {source.page_number}
                </p>
              ))}
            </div>
          )}
        </section>
       )}
    </main>
  )
}
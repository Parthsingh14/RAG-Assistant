"use client";

import { useEffect, useState } from "react";

export default function Home() {

  const [status,setStatus] = useState("");
  const [loading,setLoading] = useState(true);
  const [error,setError] = useState("");

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
        setLoading(false);
      }
    };

    checkBackend();

  },[])


  return (
    <main>
      <h1>RAG Knowledge Assistant</h1>
      {loading && <p>Conecting to backend...</p>}
      {!loading && error && <p>{error}</p>}
      {!loading && !error && (
        <p>Backend Status: {status}</p>
      )}
    </main>
  )
}
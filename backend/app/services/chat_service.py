from groq import Groq

from app.config import GROQ_API_KEY
from app.services.faiss_service import search_faiss

client = Groq(api_key=GROQ_API_KEY)


def ask_ai(question: str):

    # Retrieve relevant chunks
    results = search_faiss(question, top_k=5)

    context = "\n\n".join(
        chunk["text"] for chunk in results
    )

    prompt = f"""
You are an AI assistant.

Answer ONLY from the context below.

If the answer is not available, reply:
"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You answer only from the provided context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": results
    }
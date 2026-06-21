import google.generativeai as genai

from config import *

from vector_store import VectorStore
from prompt import SYSTEM_PROMPT


genai.configure(api_key=GEMINI_API_KEY)


def ask_question(question):

    db = VectorStore()

    results = db.search(
        query=question,
        top_k=TOP_K
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = ""
    citations = []

    for doc, meta in zip(documents, metadatas):
        source = meta["source"]
        page = meta["page"]

        citations = list(dict.fromkeys(citations))

        context += (
            f"[Source: {source}, Page: {page}]\n"
            f"{doc}\n\n"
        )

    prompt = f"""
{SYSTEM_PROMPT}

DOCUMENT CONTEXT

{context}

USER QUESTION

{question}

ANSWER
"""

    response = genai.GenerativeModel(
        model_name=LLM_MODEL
    ).generate_content(prompt)

    return {
        "answer": response.text,
        "citations": citations,
        "context": context
    }
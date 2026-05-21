import ollama


def generate_answer(query, retrieved_results):

    context = ""

    for result in retrieved_results:

        retrieved_doc = result[0]

        text = retrieved_doc[0]

        context += text + "\n\n"

    prompt = f"""
You are an enterprise AI assistant.

Answer the user's question ONLY using the retrieved evidence below.

If the evidence is insufficient, say so.

Question:
{query}

Retrieved Evidence:
{context}

Answer:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
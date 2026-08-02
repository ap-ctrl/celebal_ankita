from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(question, context):
    """
    Generate answer using Groq.
    """

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context provided below.

If the answer is not present in the context, reply:

"I could not find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3

    )

    return response.choices[0].message.content
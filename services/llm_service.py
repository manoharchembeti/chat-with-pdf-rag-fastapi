import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it inside your .env file.")

# Create Groq client
client = Groq(api_key=api_key)


def generate_answer_from_chunks(question: str, chunks: list[str]):
    """
    This function takes:
    1. User question
    2. Related PDF chunks

    Then sends both to Groq AI and gets final answer.
    """

    # Convert list of chunks into one context string
    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful PDF assistant.

Answer the user's question using ONLY the PDF context given below.

If the answer is not available in the context, say:
"I could not find this information in the uploaded PDF."

PDF CONTEXT:
{context}

USER QUESTION:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You answer questions based only on uploaded PDF content."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer
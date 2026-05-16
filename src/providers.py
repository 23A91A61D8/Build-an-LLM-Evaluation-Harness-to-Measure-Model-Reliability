import os
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize clients
openai_client = None
groq_client = None

# OpenAI Client
if OPENAI_API_KEY:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Groq Client
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)


def get_openai_response(prompt):
    """
    Generate response using OpenAI model.
    """

    if not openai_client:
        return "OpenAI API key not configured."

    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"OpenAI Error: {str(e)}"


def get_groq_response(prompt):
    """
    Generate response using Groq model.
    """

    if not groq_client:
        return "Groq API key not configured."

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Groq Error: {str(e)}"
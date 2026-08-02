import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.1-8b-instant"

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

TOP_K = 3
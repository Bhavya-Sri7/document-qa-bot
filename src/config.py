import os
from dotenv import load_dotenv

load_dotenv()

# ---------------- API ---------------- #

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------------- Models ---------------- #
EMBEDDING_MODEL = "models/gemini-embedding-001"

LLM_MODEL = "models/gemini-2.5-flash"

# ---------------- Database ---------------- #

DB_PATH = "db"

COLLECTION_NAME = "document_knowledge"

# ---------------- Chunking ---------------- #

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# ---------------- Retrieval ---------------- #

TOP_K = 5

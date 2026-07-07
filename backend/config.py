import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not found."
    )
MODEL_NAME = "gemini-2.5-flash"

TEMPERATURE = 0.3

MAX_HISTORY = 8

TOP_K = 4
VECTOR_DB="vector_db"

DATA_PATH="data/gucci_docs.json"
from dotenv import load_dotenv
import os
from pathlib import Path

# Secrets
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent 
DATA_DIR = PROJECT_ROOT / "data"
PDF_PATH = DATA_DIR / "document.pdf" # Path and name to save the downloaded PDF
EMBEDDINGS_PATH = DATA_DIR / "text_chunks_and_embeddings_df.csv" # Path and name to save the embeddings file

# URLs
PDF_URL = "" # The PDF URL for making the download

# Models (OpenAI models for Embedding and Chat)
EMBED_MODEL = "text-embedding-3-small" # The embedding model
CHAT_MODEL = "gpt-5.2" # The chat model

# Parameters
CHUNK_SIZE = 10 # The sentence number per chunk
OVERLAP = 1 # The sentence overlap per chunk
TOP_K = 5 # The number of chunks retrieved
BATCH_SIZE = 32 # The number of chunks by batch

if CHUNK_SIZE <= 0 or OVERLAP < 0 or OVERLAP >= CHUNK_SIZE:
    raise ValueError("Chunk size must be greater than 0. Chunk overlap must be equal or greater than 0. Chunk size must be greater than Chunk overlap")
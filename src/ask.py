from src.config import CHAT_MODEL, EMBED_MODEL, OPENAI_API_KEY, EMBEDDINGS_PATH, TOP_K
from src.storage import load_embeddings
from src.retrieval import build_embeddings_matrix, retrieve_top_k
from src.generation import generate_response

loaded_embeddings = load_embeddings(EMBEDDINGS_PATH)

embeddings = build_embeddings_matrix(loaded_embeddings)

query = "INSERT_YOUR_QUERY_HERE"

context = retrieve_top_k(query, loaded_embeddings, embeddings, OPENAI_API_KEY, EMBED_MODEL, TOP_K)

response = generate_response(query, context, OPENAI_API_KEY, CHAT_MODEL)

print(response)
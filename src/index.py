from src.config import PDF_PATH, PDF_URL, OVERLAP, CHUNK_SIZE, EMBED_MODEL, OPENAI_API_KEY, EMBEDDINGS_PATH, BATCH_SIZE
from src.io_pdf import open_and_read_file, ensure_pdf_exists
from src.chunking import split_senteces, make_chunks
from src.embeddings import embed_chunks
from src.storage import save_embeddings, load_embeddings

ensure_pdf_exists(PDF_URL, PDF_PATH)

pages_and_text = open_and_read_file(PDF_PATH)

split_senteces(pages_and_text)

pages_and_chunks = make_chunks(pages_and_text, CHUNK_SIZE, OVERLAP)

#Embed Chunk 1 by 1
pages_and_chunks = embed_chunks(pages_and_chunks, OPENAI_API_KEY, EMBED_MODEL)

#Embed Chunk in batches of BATCH_SIZE
#embed_chunks_batched(pages_and_chunks, OPENAI_API_KEY, EMBED_MODEL, BATCH_SIZE)

save_embeddings(pages_and_chunks, EMBEDDINGS_PATH)
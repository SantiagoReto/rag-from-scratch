from openai import OpenAI
from tqdm.auto import tqdm


# Embed chunks 1 by 1
def embed_chunks(pages_and_chunks, api_key, model):
    client = OpenAI(api_key=api_key)
    print("Embedding chunks...")
    for item in tqdm(pages_and_chunks):
        response = client.embeddings.create(
            input = item["sentence_chunk"],
            model=model
        )
        item["embedding"] = response.data[0].embedding
    return pages_and_chunks

# Embed chunks in batches of BATCH_SIZE
def embed_chunks_batched(pages_and_chunks, api_key, model, batch_size=16):
    client = OpenAI(api_key=api_key)
    print("Embedding chunks...")
    for start in tqdm(range(0, len(pages_and_chunks), batch_size)):
        end = min(start + batch_size, len(pages_and_chunks))

        batch_chunks = [item["sentence_chunk"] for item in pages_and_chunks[start:end]]

        response = client.embeddings.create(
            input = batch_chunks,
            model=model
        )

        for j, item in enumerate(pages_and_chunks[start:end]):
            item["embedding"] = response.data[j].embedding
    return pages_and_chunks
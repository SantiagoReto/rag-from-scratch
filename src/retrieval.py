import numpy as np
import torch
from openai import OpenAI

def build_embeddings_matrix(pages_and_chunks):
    # Convert our embeddings into a torch.tensor
    embeddings = torch.tensor(np.stack([item["embedding"] for item in pages_and_chunks]), dtype=torch.float32)
    
    # Normalize embeddings vectors
    embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)

    return embeddings

def retrieve_top_k(query, pages_and_chunks, embeddings, api_key, model, top_k):
    
    # Embed the query
    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(
            input = query,
            model=model
        )

    query_embedding = response.data[0].embedding

    # Convert our query embedding into a torch.tensor
    query_embedding = torch.tensor(query_embedding, dtype=torch.float32)

    # Normalize query_embedding vectors
    query_embedding = torch.nn.functional.normalize(query_embedding, p=2, dim=0)


    # Get similarity scores with dot_product (compared on magnitude and direction. As the vectores were previously normalized it is equal to cosine similarity)
    dot_scores = embeddings @ query_embedding


    # Get the top 5 results
    top_results_dot_product = torch.topk(dot_scores, k=top_k)

    context_text = []

    for idx in top_results_dot_product[1]:
        part = f"Chunk: {pages_and_chunks[idx]['sentence_chunk']} Page: {pages_and_chunks[idx]['page_number']}"
        context_text.append(part)

    context_text = "\n\n".join(context_text)

    return context_text
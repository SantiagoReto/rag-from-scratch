import pandas as pd
import numpy as np
import ast


# Save embedding vectors to a csv file to save_path
def save_embeddings(pages_and_chunks, save_path):
    text_chunks_and_embeddings_df = pd.DataFrame(pages_and_chunks)
    text_chunks_and_embeddings_df.to_csv(save_path, index = False)
    print(f"[INFO] The file has been created as '{save_path.name}' in '{save_path}'")


# Load embedding vectors from a csv file
def load_embeddings(save_path):
    # Import file from save_path
    text_chunks_and_embeddings_df_load = pd.read_csv(save_path)

    # Convert embedding column back to np.array (it got converted to string when it saved to csv)
    text_chunks_and_embeddings_df_load["embedding"] = text_chunks_and_embeddings_df_load["embedding"].apply(lambda s: np.array(ast.literal_eval(s), dtype=np.float32))

    # Convert texts and embedding df to list of dicts
    pages_and_chunks = text_chunks_and_embeddings_df_load.to_dict(orient="records")
    return pages_and_chunks
from spacy.lang.en import English
import re


# Split pages into sentences
def split_senteces(pages_and_text):
    
    nlp = English()

    nlp.add_pipe("sentencizer")

    for item in pages_and_text:
        item["sentences"] = list(nlp(item["text"]).sents)
        
        # Make sure all sentences are strings
        item["sentences"] = [str(sentence) for sentence in item["sentences"]]
        
        # Count the sentences 
        item["page_sentence_count_spacy"] = len(item["sentences"])


# Chunking sentences in groups of CHUNK_SIZE
def make_chunks(pages_and_text, chunk_size, overlap):
    
    def split_list(input_list: list, chunk_size: int, overlap: int) -> list[list[str]]:

        if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
            raise ValueError("Chunk size must be greater than 0. Chunk overlap must be equal or greater than 0. Chunk size must be greater than Chunk overlap")

        step = chunk_size - overlap
        return [input_list[i:i + chunk_size] for i in range(0, len(input_list), step)]

    for item in pages_and_text:
        item["sentence_chunks"] = split_list(input_list=item["sentences"], chunk_size=chunk_size, overlap=overlap)
        item["num_chunks"] = len(item["sentence_chunks"])


    # Split each chunk into its own item
    pages_and_chunks = []
    for item in pages_and_text:
        for sentence_chunk in item["sentence_chunks"]:
            chunk_dict = {}
            chunk_dict["page_number"] = item["page_number"]

            # Join the sentences together into a paragraph like structure, aka join the list of sentences into one paragraph
            joined_sentence_chunk = "".join(sentence_chunk).replace("  ", " ").strip()
            joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sentence_chunk)

            chunk_dict["sentence_chunk"] = joined_sentence_chunk

            chunk_dict["chunk_char_count"] = len(joined_sentence_chunk)
            chunk_dict["chunk_word_count"] = len([word for word in joined_sentence_chunk.split(" ")])
            chunk_dict["chunk_token_count"] = len(joined_sentence_chunk) / 4

            pages_and_chunks.append(chunk_dict)
    
    return pages_and_chunks
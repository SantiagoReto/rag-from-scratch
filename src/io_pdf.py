import fitz
import requests


# Clean the text
def text_formatter(text: str) -> str:
    cleaned_text = text.replace("\n", " ").strip()
    return cleaned_text


# Get text + info per page
def open_and_read_file(dest_path) -> list[dict]:
    doc = fitz.open(str(dest_path))
    pages_and_text = []
    for page_number, page in enumerate(doc):
        text = page.get_text()
        text = text_formatter(text=text)
        pages_and_text.append({"page_number": page_number + 1,
                               "page_char_count": len(text),
                               "page_word_count": len(text.split(" ")),
                               "page_sentence_count_raw": len(text.split(". ")),
                               "page_token_count": len(text) / 4,
                               "text": text})
    return pages_and_text


# Download PDF
def download_pdf(url, dest_path):
    
    # Send a GET request to the URL
    response = requests.get(url, timeout=(10, 60))
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the file and save it
        with dest_path.open("wb") as file:
            file.write(response.content)
        print(f"[INFO] The file has been download and saved as '{dest_path.name}' in '{dest_path}'")
    else:
        print(f"[INFO] Failed to down the file. Status code: {response.status_code}")


# See if PDF already exist, if it doesn't exist download it
def ensure_pdf_exists(url, dest_path):
    if not dest_path.exists():
        print("[INFO] File doesn't exist, downloading...")
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        download_pdf(url, dest_path)

    else:
        print(f"File '{dest_path.name}' already exists.")
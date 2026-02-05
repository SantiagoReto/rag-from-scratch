# PDF-based RAG Pipeline (Python)

This repository contains a **Retrieval-Augmented Generation (RAG)** pipeline built in Python, designed to answer questions based on the contents of a PDF document.

The goal of this project is to **demonstrate a complete RAG workflow** — from document ingestion to context-aware LLM responses.

---

## 🧠 What this project does

The pipeline follows these steps:

1. Reads a PDF document (local or downloaded)
2. Extracts text page by page
3. Splits text into sentences
4. Groups sentences into overlapping chunks
5. Generates embeddings for each chunk
6. Stores embeddings locally
7. Retrieves the most relevant chunks via similarity search
8. Uses an LLM to answer a question using the retrieved context

---

## 🏗️ High-level architecture
```text
PDF
 ↓
Text extraction
 ↓
Sentence splitting
 ↓
Chunking with overlap
 ↓
Embeddings
 ↓
Similarity search
 ↓
LLM response grounded in context
```

## 📁 Project structure
```text
.
├── data/
│   ├── .gitkeep                 # folder placeholder (no data committed)
│   └── document.pdf             # user-provided (ignored by git)
│
├── src/
│   ├── io_pdf.py                # PDF download & reading
│   ├── chunking.py              # sentence splitting & chunking
│   ├── embeddings.py            # embedding generation
│   ├── storage.py               # save/load embeddings
│   ├── retrieval.py             # similarity search (top-k)
│   ├── generation.py            # LLM response generation
│   ├── config.py                # project configuration
│   ├── index.py                 # PDF → embeddings pipeline
│   └── ask.py                   # question → answer pipeline
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
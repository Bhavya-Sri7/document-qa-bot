# 📚 AI Document Q&A Bot using RAG

A Retrieval-Augmented Generation (RAG) application built with Python, Google Gemini, and ChromaDB that allows users to upload PDF/DOCX documents and ask questions based only on their content.

---

## Features

- Upload PDF and DOCX documents
- Extract text from documents
- Chunk text with overlap
- Generate embeddings using Google Gemini
- Store embeddings in ChromaDB
- Semantic search using vector similarity
- Grounded answer generation
- Source citations
- Interactive Streamlit UI
- Persistent vector database

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Google Gemini | LLM & Embeddings |
| ChromaDB | Vector Database |
| PyPDF | PDF Extraction |
| python-docx | DOCX Extraction |
| Streamlit | Web Interface |
| dotenv | API Key Management |

---

## Project Structure

document-qa-bot/

```
data/
db/
src/
    config.py
    document_loader.py
    chunker.py
    vector_store.py
    prompt.py
    ingest.py
    query.py
main.py
requirements.txt
README.md
.env
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/document-qa-bot.git
```

Go to project

```bash
cd document-qa-bot
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create

```
.env
```

Add

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run

Build database

```bash
python -m src.ingest
```

Run Streamlit

```bash
streamlit run main.py
```

---

## Workflow

Upload Documents

↓

Extract Text

↓

Chunk Documents

↓

Generate Embeddings

↓

Store in ChromaDB

↓

User Query

↓

Semantic Search

↓

Gemini

↓

Answer + Citations

---

## Future Improvements

- Chat History
- Multi-user Support
- FAISS Support
- Hybrid Search
- OCR for Scanned PDFs
- Docker Deployment

---

## Author

Your Name

AI Engineering Internship Assignment

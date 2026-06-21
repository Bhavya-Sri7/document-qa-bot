from document_loader import load_documents
from chunker import chunk_pages
from vector_store import VectorStore
from config import *


def ingest_documents(folder="data"):

    pages = load_documents(folder)

    chunks = chunk_pages(
        pages,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    db = VectorStore()

    db.reset_collection()

    db.add_chunks(chunks)

    return len(pages), len(chunks), db.total_documents()


if __name__ == "__main__":

    pages, chunks, total = ingest_documents()

    print(f"Pages : {pages}")

    print(f"Chunks : {chunks}")

    print(f"Database : {total}")

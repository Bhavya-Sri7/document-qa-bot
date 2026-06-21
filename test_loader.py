from src.document_loader import load_documents
from src.chunker import chunk_pages

pages = load_documents("data")

chunks = chunk_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=200
)

print("=" * 60)
print("Total Pages :", len(pages))
print("Total Chunks:", len(chunks))
print("=" * 60)

for chunk in chunks[:5]:

    print(chunk["metadata"])

    print(chunk["text"][:200])

    print("-" * 60)
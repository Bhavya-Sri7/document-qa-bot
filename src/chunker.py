from typing import List, Dict


def chunk_pages(
    pages: List[Dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Dict]:
    """
    Splits extracted pages into overlapping chunks while
    preserving metadata.
    """

    chunks = []

    for page in pages:

        text = page["text"]
        metadata = page["metadata"]

        start = 0
        text_length = len(text)

        while start < text_length:

            end = min(start + chunk_size, text_length)

            chunk_text = text[start:end]

            chunks.append(
                {
                    "text": chunk_text,
                    "metadata": {
                        "source": metadata["source"],
                        "page": metadata["page"],
                        "chunk_start": start,
                        "chunk_end": end
                    }
                }
            )

            if end == text_length:
                break

            start += chunk_size - chunk_overlap

    return chunks
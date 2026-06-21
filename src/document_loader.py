import os
from pathlib import Path
from pypdf import PdfReader
from docx import Document

def clean_text(text: str) -> str:
    """
    Remove extra spaces, tabs and newlines.
    """
    if not text:
        return ""

    return " ".join(text.split())


# ---------------- PDF ---------------- #

def extract_pdf(file_path: str):
    """
    Extract text page-by-page from PDF.
    Returns:
        [
            {
                "text": "...",
                "metadata":{
                    "source":"file.pdf",
                    "page":1
                }
            }
        ]
    """

    pages = []

    file_name = os.path.basename(file_path)

    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        text = clean_text(text)

        if text:

            pages.append(
                {
                    "text": text,
                    "metadata": {
                        "source": file_name,
                        "page": page_number
                    }
                }
            )

    return pages


# ---------------- DOCX ---------------- #

def extract_docx(file_path: str):
    """
    Extract text from Word documents.
    Entire document is treated as page 1.
    """

    file_name = os.path.basename(file_path)

    document = Document(file_path)

    paragraphs = []

    for para in document.paragraphs:

        if para.text.strip():

            paragraphs.append(para.text.strip())

    full_text = "\n".join(paragraphs)

    full_text = clean_text(full_text)

    return [
        {
            "text": full_text,
            "metadata": {
                "source": file_name,
                "page": 1
            }
        }
    ]


# ---------------- Dispatcher ---------------- #

def load_document(file_path: str):
    """
    Automatically detect document type.
    """

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    elif extension == ".docx":
        return extract_docx(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")


# ---------------- Folder Loader ---------------- #

def load_documents(folder_path: str):
    """
    Read every PDF and DOCX from a folder.
    """

    all_pages = []

    supported = [".pdf", ".docx"]

    for file in os.listdir(folder_path):

        path = os.path.join(folder_path, file)

        if Path(path).suffix.lower() in supported:

            print(f"Reading {file}")

            pages = load_document(path)

            all_pages.extend(pages)

    return all_pages

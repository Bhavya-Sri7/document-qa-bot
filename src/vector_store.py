import chromadb

from chromadb.utils.embedding_functions import (
    GoogleGenerativeAiEmbeddingFunction
)

from config import *

import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=DB_PATH
        )

        self.embedding_function = GoogleGenerativeAiEmbeddingFunction(
            api_key=GEMINI_API_KEY,
            model_name=EMBEDDING_MODEL
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_function,
            metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(self, chunks):

        ids = []

        documents = []

        metadatas = []

        existing_ids = set(
            self.collection.get()["ids"]
        )

        for chunk in chunks:

            metadata = chunk["metadata"]

            chunk_id = (
                f"{metadata['source']}_"
                f"{metadata['page']}_"
                f"{metadata['chunk_start']}"
            )

            if chunk_id in existing_ids:
                continue

            ids.append(chunk_id)

            documents.append(chunk["text"])

            metadatas.append(metadata)

        if ids:

            self.collection.add(

                ids=ids,

                documents=documents,

                metadatas=metadatas
            )

            print(f"Indexed {len(ids)} chunks.")

        else:

            print("No new chunks found.")

    def total_documents(self):

        return self.collection.count()

    def reset_collection(self):
        try:
            self.client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_function,
            metadata={"hnsw:space": "cosine"}
        )
    
    def search(self, query, top_k=3):

        results = self.collection.query(

        query_texts=[query],

        n_results=top_k

    )
        return results

import os
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

VECTOR_DIR = "app/vector_store"
os.makedirs(VECTOR_DIR, exist_ok=True)

INDEX_FILE = os.path.join(VECTOR_DIR, "documents.index")
METADATA_FILE = os.path.join(VECTOR_DIR, "metadata.pkl")

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def save_to_faiss(document_id: int,filename: str,chunks: list,embeddings):
    embeddings = np.array(embeddings, dtype="float32")
    dimension = embeddings.shape[1]

    # Load existing index or create a new one
    if os.path.exists(INDEX_FILE):
        index = faiss.read_index(INDEX_FILE)
    else:
        index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)
    faiss.write_index(index, INDEX_FILE)

    # Load existing metadata
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "rb") as f:
            metadata = pickle.load(f)
    else:
        metadata = []

    # Append new chunk metadata
    for chunk in chunks:
        metadata.append(
            {
                "document_id": document_id,
                "document_name": filename,
                "text": chunk
            }
        )

    with open(METADATA_FILE, "wb") as f:
        pickle.dump(metadata, f)


def search_faiss(query: str, k: int = 5):
    if not os.path.exists(INDEX_FILE):
        raise Exception("FAISS index not found.")

    if not os.path.exists(METADATA_FILE):
        raise Exception("Metadata file not found.")

    index = faiss.read_index(INDEX_FILE)

    with open(METADATA_FILE, "rb") as f:
        metadata = pickle.load(f)

    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        if idx != -1:
            results.append(metadata[idx])

    return results
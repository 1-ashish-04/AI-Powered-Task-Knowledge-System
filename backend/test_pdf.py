from app.services.document_service import (
    extract_text,
    chunk_text
)
from app.services.embedding_service import create_embeddings
from app.services.faiss_service import save_to_faiss

text = extract_text(
    "app/uploads/pythonHandBook.pdf"
)

chunks = chunk_text(text)

print(len(chunks))

print(chunks[0])

vectors = create_embeddings(chunks)

print(vectors.shape)

save_to_faiss(
    chunks,
    vectors
)
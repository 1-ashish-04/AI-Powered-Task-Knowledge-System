import os
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.document import Document

from app.services.document_service import (
    extract_text,
    chunk_text
)

from app.services.embedding_service import (
    create_embeddings
)

from app.services.faiss_service import (
    save_to_faiss
)

from app.schemas.search import SearchRequest
from app.services.faiss_service import search_faiss

from app.dependencies import get_current_user
from app.models.user import User

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = [".pdf", ".txt"]

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Validate file extension
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported."
        )

    # Save uploaded file
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save metadata to MySQL
    document = Document(
        title=file.filename,
        filename=file.filename,
        filepath=file_path,
        uploaded_by=current_user.id      # Temporary (replace with current_user.id later)
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # Extract text
    text = extract_text(file_path)

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable text found in the document."
        )

    # Chunk text
    chunks = chunk_text(text)

    # Generate embeddings
    embeddings = create_embeddings(chunks)

    # Store in FAISS
    save_to_faiss(
    document.id,
    file.filename,
    chunks,
    embeddings
)

    return {
        "message": "Document uploaded and indexed successfully.",
        "document_id": document.id,
        "filename": file.filename,
        "chunks": len(chunks)
    }

@router.post("/search")
def semantic_search(request: SearchRequest):

    results = search_faiss(
        query=request.query,
        k=request.top_k
    )

    return {
        "query": request.query,
        "total_results": len(results),
        "results": results
    }
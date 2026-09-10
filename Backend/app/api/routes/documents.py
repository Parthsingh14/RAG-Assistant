from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
import logging

from app.services.ingestion_service import ingest_documents


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    upload_dir = Path("temp_uploads")
    upload_dir.mkdir(exist_ok=True)

    file_path = upload_dir / file.filename
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        stats = ingest_documents(str(file_path))

        return {
            "message": "Document ingested successfully",
            "document_id": stats["document_id"],
            "filename": stats["filename"],
            "chunks_created": stats["chunks_created"],
            "vectors_stored": stats["vectors_stored"]
        }
    finally:
        file_path.unlink(missing_ok=True)  # Clean up the uploaded file after processing
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from services.pdf_service import extract_text_from_pdf
from utils.text_splitter import create_chunks
from vectorstore.chroma_store import add_chunks_to_chroma, search_similar_chunks
from services.llm_service import generate_answer_from_chunks

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    text = await extract_text_from_pdf(file)

    chunks = create_chunks(text)

    add_chunks_to_chroma(chunks)

    return {
        "message": "PDF uploaded successfully. Now you can ask questions.",
        "chunks_count": len(chunks)
    }


@router.post("/ask")
def ask_question(request: QuestionRequest):
    # Step 1: Search related chunks from ChromaDB
    related_chunks = search_similar_chunks(request.question)

    # Step 2: Send question + chunks to Groq AI
    final_answer = generate_answer_from_chunks(
        question=request.question,
        chunks=related_chunks
    )

    # Step 3: Return final AI answer
    return {
        "question": request.question,
        "answer": final_answer,
        "source_chunks": related_chunks
    }
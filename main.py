from fastapi import FastAPI
from routes.pdf_routes import router as pdf_router

app = FastAPI()

app.include_router(pdf_router)


@app.get("/")
def home():
    return {
        "message": "PDF RAG API is running"
    }
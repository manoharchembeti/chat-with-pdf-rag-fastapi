# Chat with PDF - RAG API (FastAPI)

A FastAPI-based application implementing Retrieval-Augmented Generation (RAG) to allow users to upload PDF documents and ask questions based on their content.

## Features

- **PDF Ingestion & Processing**: Extract text from uploaded PDF files and split it into optimized chunks.
- **Vector Search Integration**: Store and query document embeddings efficiently using vector storage.
- **RAG-Powered Q&A**: Combine retrieved document contexts with LLMs to generate accurate responses.
- **RESTful Endpoints**: Built with FastAPI for fast, asynchronous, and auto-documented API interactions.

## Project Structure

```text
.
├── routes/          # FastAPI route handlers & API endpoints
├── services/        # Core business logic (PDF parsing, LLM invocation)
├── utils/           # Utility scripts and helpers
├── vectorstore/     # Vector database setup and retriever logic
├── main.py          # Application entry point
├── requirements.txt # Python dependencies
└── README.md        # Project documentation

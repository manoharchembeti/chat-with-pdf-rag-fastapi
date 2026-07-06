import chromadb
from sentence_transformers import SentenceTransformer

# This model converts text into embeddings/vectors
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB stores vectors locally in this folder
client = chromadb.PersistentClient(path="./vectorstore/db")

# Collection is like a table inside ChromaDB
collection = client.get_or_create_collection(name="pdf_chunks")


def add_chunks_to_chroma(chunks: list[str]):
    """
    This function stores PDF chunks inside ChromaDB.
    Each chunk is converted into an embedding.
    """

    for index, chunk in enumerate(chunks):
        embedding = embedding_model.encode(chunk).tolist()

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk_{index}"]
        )

    return True


def search_similar_chunks(question: str, top_k: int = 3):
    """
    This function searches the most related chunks for the user question.
    """

    question_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    return results["documents"][0]
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text: str):
    """
    This function splits large PDF text into smaller chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )

    chunks = text_splitter.split_text(text)

    return chunks
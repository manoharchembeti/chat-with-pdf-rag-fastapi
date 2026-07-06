from pypdf import PdfReader
import io


async def extract_text_from_pdf(file):
    """
    This function reads uploaded PDF file and extracts text.
    """

    pdf_bytes = await file.read()

    reader = PdfReader(io.BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text
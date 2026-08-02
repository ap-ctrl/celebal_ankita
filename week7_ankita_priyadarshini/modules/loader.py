import fitz  # PyMuPDF


def load_pdf(pdf_path):
    """
    Reads a PDF and returns all text.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text
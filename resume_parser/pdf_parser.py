import fitz  # PyMuPDF


class PDFParser:
    """
    Extract text from PDF resumes.
    """

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        text = ""

        try:
            document = fitz.open(pdf_path)

            for page in document:
                text += page.get_text()

            document.close()

        except Exception as e:
            print(f"PDF Error: {e}")

        return text.strip()
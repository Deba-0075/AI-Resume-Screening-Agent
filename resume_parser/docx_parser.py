from docx import Document


class DOCXParser:
    """
    Extract text from DOCX resumes.
    """

    @staticmethod
    def extract_text(docx_path: str) -> str:

        try:
            document = Document(docx_path)

            paragraphs = [
                para.text
                for para in document.paragraphs
                if para.text.strip()
            ]

            return "\n".join(paragraphs)

        except Exception as e:
            print(f"DOCX Error: {e}")
            return ""
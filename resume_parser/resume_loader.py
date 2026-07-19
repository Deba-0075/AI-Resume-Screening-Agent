from pathlib import Path

from resume_parser.pdf_parser import PDFParser
from resume_parser.docx_parser import DOCXParser
from resume_parser.text_parser import TXTParser


class ResumeParser:

    @staticmethod
    def extract_text(file_path: str):

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return PDFParser.extract_text(file_path)

        elif extension == ".docx":
            return DOCXParser.extract_text(file_path)

        elif extension == ".txt":
            return TXTParser.extract_text(file_path)

        else:
            raise ValueError(f"Unsupported file format: {extension}")
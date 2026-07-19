class TXTParser:
    """
    Extract text from TXT resumes.
    """

    @staticmethod
    def extract_text(txt_path: str) -> str:

        try:
            with open(txt_path, "r", encoding="utf-8") as file:
                return file.read()

        except UnicodeDecodeError:
            with open(txt_path, "r", encoding="latin-1") as file:
                return file.read()

        except Exception as e:
            print(f"TXT Error: {e}")
            return ""
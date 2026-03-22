from pathlib import Path
import pdfplumber
import pytesseract
import pandas as pd
from PIL import Image


def extract_text(file_path: Path) -> str:
    ext = file_path.suffix.lower()

    if ext == ".pdf":
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text

    elif ext in [".jpg", ".jpeg", ".png"]:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)

    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
        return df.to_string()

    return ""
import fitz  # nom d'import de PyMuPDF
from pathlib import Path

RAW = Path("data/raw")
OUT = Path("data/text")
OUT.mkdir(parents=True, exist_ok=True)

for pdf_path in RAW.glob("*.pdf"):
    doc = fitz.open(pdf_path)
    pages = [page.get_text() for page in doc]
    text = "\n".join(pages)

    out_file = OUT / (pdf_path.stem + ".txt")
    out_file.write_text(text, encoding="utf-8")

    print(f"{pdf_path.name} : {len(doc)} pages, {len(text)} caractères")
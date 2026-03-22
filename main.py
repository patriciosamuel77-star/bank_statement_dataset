from pathlib import Path
import pandas as pd
from extractor import extract_text
from llm_parser import parse_statement

RAW = Path("data/raw")
OUT = Path("data/output")

OUT.mkdir(parents=True, exist_ok=True)

rows = []

for f in RAW.iterdir():
    print("Procesando:", f.name)
    text = extract_text(f)

    if not text:
        continue

    data = parse_statement(text)
    data["File extension"] = f.suffix
    rows.append(data)

df = pd.DataFrame(rows)
df.to_excel(OUT / "resultado.xlsx", index=False)

print("Listo ✅")
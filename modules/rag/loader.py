from pathlib import Path
import json

# Resolve the project root regardless of where Streamlit runs
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def load_general_docs():
    path = DATA_DIR / "general.txt"

    with open(path, "r", encoding="utf-8") as f:
        return [
            f"[GENERAL] {line.strip()}"
            for line in f.readlines()
            if line.strip()
        ]


def load_medical_docs():
    path = DATA_DIR / "medical.json"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []

    for item in data:
        q = item.get("question", "")
        a = item.get("answer", "")
        docs.append(f"[MEDICAL] Q: {q} A: {a}")

    return docs


def load_arxiv_docs():
    path = DATA_DIR / "arxiv.json"

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []

    for item in data:
        title = item.get("title", "")
        abstract = item.get("abstract", "")
        category = item.get("category", "")

        docs.append(
            f"[ARXIV][{category}] {title}: {abstract}"
        )

    return docs


def load_all_documents():
    docs = []

    docs.extend(load_general_docs())
    docs.extend(load_medical_docs())
    docs.extend(load_arxiv_docs())

    if not docs:
        raise ValueError("No documents found in the datasets.")

    print(f"Successfully loaded {len(docs)} documents.")

    return docs

"""ChromaDB Setup"""

from os import environ
from pprint import pprint
from dotenv import load_dotenv

import chromadb

load_dotenv()

# Environment vars.
collection_name: str = environ["COLLECTION_NAME"] or ""

# Data
documents: list[str] = [
    "Dante is the younger brother of Vergil.",
    "Nero is the son of Vergil.",
    "Vergil is a man of motivation.",
]
ids: list[str] = [f"d{i + 1}" for i in range(len(documents))]
query_texts: list[str] = ["Vergil is feeling motivated.", "Dante is my favourite!"]

assert (
    len(collection_name) > 0 and len(documents) > 0
)  # TODO: Remove this from production.

# Client setup
chroma_client = chromadb.Client()

# Collection setup
collection_1 = chroma_client.get_or_create_collection(name=collection_name)
collection_1.upsert(documents=documents, ids=ids)

# Query operation
results = collection_1.query(query_texts=query_texts, n_results=3)
pprint(results)

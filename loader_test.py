from app.ingestion.loader import scan_documents
from app.ingestion.parser import parse_document
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import generate_embeddings

from app.vectorstore.qdrant_store import (
    create_collection,
    store_embeddings
)

docs = scan_documents(
    "/Users/khushbukamal/Desktop/EnterpriseAISearch/enterprise-docs"
)

all_chunks = []

for file in docs:

    parsed_docs = parse_document(file)

    chunks = chunk_documents(parsed_docs)

    all_chunks.extend(chunks)

print(f"\nTotal Chunks: {len(all_chunks)}")

sample_chunks = all_chunks[:20]

vectors = generate_embeddings(sample_chunks)

print(f"Generated {len(vectors)} embeddings")

create_collection()

store_embeddings(sample_chunks, vectors)
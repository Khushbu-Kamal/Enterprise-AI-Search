from app.ingestion.loader import scan_documents
from app.ingestion.parser import parse_document
from app.ingestion.chunker import chunk_documents

from app.retrieval.bm25_retriever import (
    build_bm25_index,
    bm25_search
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

build_bm25_index(all_chunks)

query = "cascading failures"

results = bm25_search(query)

print("\nBM25 RESULTS\n")

for i, (doc, score) in enumerate(results):

    print("=" * 60)

    print(f"RESULT {i+1}")

    print("\nScore:")
    print(score)

    print("\nText:")
    print(doc.page_content[:1000])
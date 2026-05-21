from app.ingestion.loader import scan_documents
from app.ingestion.parser import parse_document
from app.ingestion.chunker import chunk_documents

from app.retrieval.bm25_retriever import (
    build_bm25_index
)

from app.retrieval.hybrid_retriever import (
    hybrid_search
)

docs = scan_documents(
    "/Users/khushbukamal/Desktop/EnterpriseAISearch/enterprise-docs"
)

all_chunks = []

for file in docs:

    parsed_docs = parse_document(file)

    chunks = chunk_documents(parsed_docs)

    all_chunks.extend(chunks)

build_bm25_index(all_chunks)

query = "What causes cascading failures in distributed systems?"

results = hybrid_search(query)

print("\nRERANKED RESULTS\n")

for i, result in enumerate(results):

    retrieved_doc = result[0]

    rerank_score = result[1]

    text = retrieved_doc[0]

    print("=" * 60)

    print(f"RESULT {i+1}")

    print("\nRerank Score:")
    print(rerank_score)

    print("\nText:")
    print(text[:1000])
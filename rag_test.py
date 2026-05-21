from dotenv import load_dotenv

load_dotenv()
from app.ingestion.loader import scan_documents
from app.ingestion.parser import parse_document
from app.ingestion.chunker import chunk_documents

from app.retrieval.bm25_retriever import (
    build_bm25_index
)

from app.retrieval.hybrid_retriever import (
    hybrid_search
)

from app.generation.generator import (
    generate_answer
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

retrieved_results = hybrid_search(query)

answer = generate_answer(
    query,
    retrieved_results
)

print("\nGENERATED ANSWER\n")

print(answer)
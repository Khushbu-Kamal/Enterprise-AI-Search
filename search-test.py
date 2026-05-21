from app.retrieval.retriever import semantic_search

query = "What causes cascading failures?"

results = semantic_search(query)

print("\nSEARCH RESULTS\n")

for i, result in enumerate(results):

    print("=" * 60)

    print(f"RESULT {i+1}")

    print("\nScore:")
    print(result.score)

    print("\nText:")
    print(result.payload["text"][:1000])
from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query, retrieved_docs, top_k=5):

    pairs = []

    for doc, score in retrieved_docs:

        pairs.append([query, doc])

    scores = reranker.predict(pairs)

    reranked = sorted(
        zip(retrieved_docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return reranked[:top_k]
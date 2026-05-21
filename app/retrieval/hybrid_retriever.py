from app.retrieval.retriever import semantic_search
from app.retrieval.bm25_retriever import bm25_search
from app.retrieval.reranker import rerank


def reciprocal_rank_fusion(rankings, k=60):

    fused_scores = {}

    for ranking in rankings:

        for rank, item in enumerate(ranking):

            doc_text = item["text"]

            if doc_text not in fused_scores:
                fused_scores[doc_text] = 0

            fused_scores[doc_text] += 1 / (k + rank + 1)

    reranked = sorted(
        fused_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return reranked


def hybrid_search(query, top_k=5):

    semantic_results = semantic_search(query)

    semantic_docs = []

    for result in semantic_results:

        semantic_docs.append({
            "text": result.payload["text"]
        })

    bm25_results = bm25_search(query)

    bm25_docs = []

    for doc, score in bm25_results:

        bm25_docs.append({
            "text": doc.page_content
        })

    fused_results = reciprocal_rank_fusion([
        semantic_docs,
        bm25_docs
    ])

    top_results = fused_results[:20]

    reranked = rerank(
        query,
        top_results,
        top_k=top_k
    )

    return reranked
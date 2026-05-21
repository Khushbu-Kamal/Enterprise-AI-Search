from rank_bm25 import BM25Okapi

bm25 = None
documents = []


def build_bm25_index(chunks):

    global bm25
    global documents

    documents = chunks

    tokenized_chunks = [
        chunk.page_content.split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_chunks)

    print("BM25 index created.")


def bm25_search(query, top_k=5):

    tokenized_query = query.split()

    scores = bm25.get_scores(tokenized_query)

    ranked_results = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_results[:top_k]
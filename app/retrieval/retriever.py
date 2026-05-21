from qdrant_client import QdrantClient

from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "enterprise_knowledge"

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_search(query, top_k=5):

    query_vector = model.encode(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector.tolist(),
        limit=top_k
    )

    return results.points
from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

from uuid import uuid4

client = QdrantClient(
    host="localhost",
    port=6333
)

COLLECTION_NAME = "enterprise_knowledge"


def create_collection():

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection created.")


def store_embeddings(chunks, vectors):

    points = []

    for chunk, vector in zip(chunks, vectors):

        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=vector.tolist(),
                payload={
                    "text": chunk.page_content,
                    "source": chunk.metadata.get(
                        "source",
                        ""
                    )
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Stored {len(points)} vectors.")
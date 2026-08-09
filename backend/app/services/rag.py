from dataclasses import dataclass
from typing import List
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels

from app.core.config import settings


@dataclass
class RetrievedChunk:
    text: str
    score: float


_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
_client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)


def ensure_collection() -> None:
    existing = [c.name for c in _client.get_collections().collections]
    if settings.qdrant_collection not in existing:
        _client.create_collection(
            collection_name=settings.qdrant_collection,
            vectors_config=qmodels.VectorParams(size=384, distance=qmodels.Distance.COSINE),
        )


def chunk_text(text: str, size: int = 400) -> List[str]:
    words = text.split()
    return [" \".join(words[i:i+size]) for i in range(0, len(words), size)]


def ingest_document(doc_id: str, text: str) -> int:
    ensure_collection()
    chunks = chunk_text(text)
    vecs = _model.encode(chunks).tolist()
    points = [qmodels.PointStruct(id=idx, vector=vec, payload={"doc_id": doc_id, "text": chunk}) for idx, (vec, chunk) in enumerate(zip(vecs, chunks))]
    _client.upsert(collection_name=settings.qdrant_collection, points=points)
    return len(chunks)


def retrieve(query: str, k: int = 4) -> List[RetrievedChunk]:
    ensure_collection()
    qvec = _model.encode(query).tolist()
    res = _client.search(collection_name=settings.qdrant_collection, query_vector=qvec, limit=k)
    return [RetrievedChunk(text=r.payload.get("text", ""), score=float(r.score)) for r in res]

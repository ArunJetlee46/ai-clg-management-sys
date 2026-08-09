from dataclasses import dataclass
from typing import List
import hashlib

from app.core.config import settings


@dataclass
class RetrievedChunk:
    text: str
    score: float


_model = None
_client = None
_memory_store: list[dict] = []


def _embed(texts: list[str]) -> list[list[float]]:
    global _model
    if _model is None:
        try:
            from sentence_transformers import SentenceTransformer

            _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        except Exception:
            _model = False
    if _model:
        return _model.encode(texts).tolist()
    vectors = []
    for text in texts:
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        vec = [digest[i] / 255 for i in range(32)] * 12
        vectors.append(vec[:384])
    return vectors


def _qdrant_client():
    global _client
    if _client is None:
        try:
            from qdrant_client import QdrantClient

            _client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)
        except Exception:
            _client = False
    return _client


def ensure_collection() -> None:
    client = _qdrant_client()
    if not client:
        return
    try:
        from qdrant_client.http import models as qmodels

        existing = [c.name for c in client.get_collections().collections]
        if settings.qdrant_collection not in existing:
            client.create_collection(
                collection_name=settings.qdrant_collection,
                vectors_config=qmodels.VectorParams(size=384, distance=qmodels.Distance.COSINE),
            )
    except Exception:
        return


def chunk_text(text: str, size: int = 400) -> List[str]:
    words = text.split()
    return [" ".join(words[i : i + size]) for i in range(0, len(words), size)]


def ingest_document(doc_id: str, text: str) -> int:
    ensure_collection()
    chunks = chunk_text(text)
    vecs = _embed(chunks)
    client = _qdrant_client()
    if client:
        try:
            from qdrant_client.http import models as qmodels

            points = [
                qmodels.PointStruct(id=idx, vector=vec, payload={"doc_id": doc_id, "text": chunk})
                for idx, (vec, chunk) in enumerate(zip(vecs, chunks))
            ]
            client.upsert(collection_name=settings.qdrant_collection, points=points)
        except Exception:
            pass
    _memory_store.extend([{"doc_id": doc_id, "text": c} for c in chunks])
    return len(chunks)


def retrieve(query: str, k: int = 4) -> List[RetrievedChunk]:
    ensure_collection()
    qvec = _embed([query])[0]
    client = _qdrant_client()
    if client:
        try:
            res = client.search(collection_name=settings.qdrant_collection, query_vector=qvec, limit=k)
            return [RetrievedChunk(text=r.payload.get("text", ""), score=float(r.score)) for r in res]
        except Exception:
            pass
    q_terms = set(query.lower().split())
    ranked = sorted(
        _memory_store,
        key=lambda item: len(q_terms.intersection(set(item["text"].lower().split()))),
        reverse=True,
    )[:k]
    return [RetrievedChunk(text=item["text"], score=0.0) for item in ranked]

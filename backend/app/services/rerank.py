from app.services.rag import RetrievedChunk


def rerank(query: str, chunks: list[RetrievedChunk]) -> list[RetrievedChunk]:
    q = set(query.lower().split())
    return sorted(chunks, key=lambda c: (len(q.intersection(set(c.text.lower().split()))), c.score), reverse=True)

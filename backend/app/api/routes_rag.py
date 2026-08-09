from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag import ingest_document, retrieve
from app.services.rerank import rerank
from app.services.llm import generate_response

router = APIRouter(prefix="/rag", tags=["rag"])


class IngestRequest(BaseModel):
    doc_id: str
    text: str


class QueryRequest(BaseModel):
    query: str


@router.post("/ingest")
def ingest(payload: IngestRequest):
    chunks = ingest_document(payload.doc_id, payload.text)
    return {"chunks": chunks}


@router.post("/query")
async def query(payload: QueryRequest):
    chunks = retrieve(payload.query)
    reranked = rerank(payload.query, chunks)
    context = "\n".join([c.text for c in reranked[:3]])
    prompt = f"Answer using only context.\nContext:\n{context}\nQuestion:{payload.query}"
    answer = await generate_response(prompt)
    return {"answer": answer, "evidence": [c.text for c in reranked[:3]]}

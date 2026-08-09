# Module Catalog (Phase-1 Baseline)

1. **Identity & Access Module** (FastAPI JWT + RBAC)
2. **Academic Records Module**
3. **Attendance Module**
4. **Examination Module**
5. **Placement Module**
6. **Timetable Optimization Module**
7. **Analytics & Reporting Module**
8. **RAG Knowledge Module** (Qdrant/Chroma + embeddings)
9. **Agent Orchestration Module** (LangGraph)
10. **Notification Module**
11. **Audit Trail Agent Module** (immutable decision/event ledger)
12. **Synthetic Data Generator Module** (privacy-safe ML/RAG bootstrapping)
13. **ML Pipeline Module** (train/serve/explain/track)
14. **Monitoring & Reliability Module**

## Module Boundary Rules
- Identity & Access is the sole source of role authorization decisions.
- Agent Orchestration coordinates agents; it does not own core academic records.
- Audit Trail Agent receives immutable append-only events from all AI and critical manual operations.
- Synthetic Data Generator writes to isolated datasets and never overwrites production records.

# Non-Functional Requirements (NFR)

- **NFR-01 Security:** JWT auth, bcrypt password hashing, least-privilege RBAC, and audit logging.
- **NFR-02 Availability:** Graceful model fallback (Groq/Gemini to Ollama).
- **NFR-03 Performance:** p95 API latency < 400ms for non-LLM endpoints, and < 4s for RAG responses.
- **NFR-04 Scalability:** Asynchronous processing with Celery + Redis.
- **NFR-05 Reliability:** Retry with exponential backoff for LLM and queue jobs.
- **NFR-06 Observability:** Metrics via Prometheus, dashboards via Grafana, errors via Sentry.
- **NFR-07 Explainability:** Every prediction must expose top influencing factors.
- **NFR-08 Compliance:** Decisions must be traceable with immutable audit history.
- **NFR-09 Cost:** Solution must be deployable with free-tier/self-hosted services only.
- **NFR-10 Maintainability:** Modular services, typed API contracts, and versioned schemas.

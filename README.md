# Aegis Campus AI

Autonomous multi-agent university operating system built on free/open tooling.

## Why Qdrant + Groq
- Qdrant is selected for production-friendly free/self-hosted vector search with Docker support.
- Groq is default for low-latency free-tier inference; Ollama is implemented as offline fallback.

## Monorepo Layout
- `backend/` FastAPI, LangGraph orchestration, auth, APIs
- `frontend/` React + Vite dashboards
- `agents/` prompt/tool configs and orchestration docs
- `ml/` synthetic data, training, explainability, serving helpers
- `infra/` deployment, monitoring, and CI assets
- `docs/` architecture and workflow diagrams

## Quickstart
1. Copy envs: `cp .env.example .env`
2. Start infra: `docker compose up -d postgres neo4j redis qdrant`
3. Build and run all: `docker compose up --build`
4. Backend docs: `http://localhost:8000/docs`
5. Frontend: `http://localhost:5173`

## Backend local
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend local
```bash
cd frontend
npm install
npm run dev
```

## Migrations
```bash
psql postgresql://postgres@localhost:5432/aegis -f backend/migrations/001_init.sql
```

## Testing
```bash
cd backend && pytest
cd ../frontend && npm test
```

## TODO Tracking
See `TODO.md` for remaining hardening tasks and roadmap leftovers.

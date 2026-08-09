# Problem Statement

## Project
**Aegis Campus AI – Autonomous Multi-Agent University Operating System**

**Tagline:** "An AI workforce that autonomously manages academic operations, predicts student success, and optimizes campus resources through collaborative AI agents."

## Engineered Problem Definition
Build an autonomous multi-agent university operating system that:
- Automates academic operations,
- Predicts student outcomes (performance, attendance, dropout, placement),
- Optimizes resources (timetable, faculty load, rooms),
- Maintains auditable AI decision trails for governance and compliance.

## Mandatory Stack Constraint
The solution must use only free/open-source or free-tier technologies:
- LLM: Groq API or Gemini free tier, with Ollama local fallback
- Orchestration: LangGraph
- Backend: FastAPI
- Auth: JWT with python-jose + passlib (bcrypt)
- Queue/Cache: Celery + Redis
- Relational DB: PostgreSQL
- Knowledge Graph: Neo4j
- Vector DB: Qdrant or ChromaDB
- ML: scikit-learn, XGBoost, LightGBM, SHAP, LIME
- Optimization: OR-Tools
- Frontend: React + Vite + Tailwind + shadcn/ui
- DevOps: Docker, Docker Compose, GitHub Actions
- Hosting: Render/Fly.io (backend), Vercel/Netlify (frontend)
- Monitoring: Prometheus + Grafana
- Error Tracking: Sentry

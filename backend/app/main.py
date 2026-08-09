import sentry_sdk
from fastapi import FastAPI
from prometheus_client import make_asgi_app

from app.api import routes_auth, routes_students, routes_rag, routes_agents, routes_ml, routes_timetable, routes_health
from app.core.config import settings
from app.core.exceptions import register_exception_handlers

if settings.sentry_dsn:
    sentry_sdk.init(dsn=settings.sentry_dsn, traces_sample_rate=0.2)

app = FastAPI(title="Aegis Campus AI API")
app.mount("/metrics", make_asgi_app())

app.include_router(routes_health.router)
app.include_router(routes_auth.router, prefix="/api/v1")
app.include_router(routes_students.router, prefix="/api/v1")
app.include_router(routes_rag.router, prefix="/api/v1")
app.include_router(routes_agents.router, prefix="/api/v1")
app.include_router(routes_ml.router, prefix="/api/v1")
app.include_router(routes_timetable.router, prefix="/api/v1")

register_exception_handlers(app)

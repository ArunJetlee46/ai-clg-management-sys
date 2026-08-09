from celery import Celery
from app.core.config import settings

celery_app = Celery("aegis", broker=settings.redis_url, backend=settings.redis_url)

@celery_app.task
def notify_task(message: str):
    return {"status": "sent", "message": message}

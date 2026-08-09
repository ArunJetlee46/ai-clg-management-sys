import httpx
from app.core.config import settings


async def generate_response(prompt: str) -> str:
    if settings.primary_llm_provider == "groq" and settings.groq_api_key:
        async with httpx.AsyncClient(timeout=30) as client:
            res = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"******"},
                json={
                    "model": settings.groq_model,
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            if res.is_success:
                return res.json()["choices"][0]["message"]["content"]
    async with httpx.AsyncClient(timeout=30) as client:
        res = await client.post(
            f"{settings.ollama_base_url}/api/generate",
            json={"model": settings.ollama_model, "prompt": prompt, "stream": False},
        )
        if res.is_success:
            return res.json().get("response", "")
    return "LLM unavailable"

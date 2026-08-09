from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    env: str = "development"
    secret_key: str = "change_me"
    access_token_expire_minutes: int = 60

    database_url: str = "******localhost:5432/aegis"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "neo4jpassword"

    redis_url: str = "redis://localhost:6379/0"
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection: str = "campus_docs"

    primary_llm_provider: str = "groq"
    groq_api_key: str | None = None
    groq_model: str = "llama-3.1-8b-instant"
    gemini_api_key: str | None = None
    gemini_model: str = "gemini-1.5-flash"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1:8b"

    sentry_dsn: str | None = None


settings = Settings()

from neo4j import GraphDatabase
from app.core.config import settings


driver = GraphDatabase.driver(settings.neo4j_uri, auth=(settings.neo4j_user, settings.neo4j_password))


def run_cypher(query: str, **params):
    with driver.session() as session:
        return list(session.run(query, **params))

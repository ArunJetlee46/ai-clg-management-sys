from app.services.rag import chunk_text


def test_chunking():
    text = 'a ' * 1000
    chunks = chunk_text(text, size=100)
    assert len(chunks) == 10

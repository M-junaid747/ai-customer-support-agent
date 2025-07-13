from fastapi.testclient import TestClient
from app.main import app
from app.services.knowledge_base import retrieve_context

client = TestClient(app)

def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_retrieve_context_found():
    answer = retrieve_context("How do I reset my password?")
    assert answer is not None

def test_retrieve_context_not_found():
    answer = retrieve_context("This is an unrelated question.")
    assert answer is None
# tests/test_endpoints.py (versión corregida y profesional)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test para /resumir
def test_resumir():
    response = client.post("/resumir", json={
        "texto": "Este es un texto de prueba para ver si el resumen funciona correctamente."
    })
    assert response.status_code == 200
    data = response.json()
    assert "resumen" in data

# Test para /upsert
def test_upsert():
    response = client.post("/upsert", json={
        "id": "test-id",
        "titulo": "Título de prueba",
        "texto": "Texto de prueba para insertar en ChromaDB.",
        "metadatos": {"fuente": "test"}
    })
    assert response.status_code == 200
    data = response.json()
    assert "mensaje" in data or "detail" in data

# Test para /query
def test_query():
    response = client.post("/query", json={
        "pregunta": "¿Qué está pasando en Nicaragua?",
        "n_resultados": 3
    })
    assert response.status_code == 200
    data = response.json()
    assert "documents" in data or "resultados" in data

# Test para /clasificar
def test_clasificar():
    response = client.post("/clasificar", json={
        "texto": "La corrupción gubernamental afecta el desarrollo del país."
    })
    assert response.status_code == 200
    data = response.json()
    assert "categorias" in data  # Ajustado a tu API real

# Test para /entidades
def test_entidades():
    response = client.post("/entidades", json={
        "texto": "Daniel Ortega es el presidente de Nicaragua."
    })
    assert response.status_code == 200
    data = response.json()
    # Verificamos las claves correctasclar
    assert "PERSONA" in data
    assert "ORG" in data
    assert "LOC" in data

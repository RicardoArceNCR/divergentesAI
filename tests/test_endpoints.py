# tests/test_endpoints.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_articulos():
    response = client.get("/articulos?n=1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_resumir():
    response = client.post("/resumir", json={
        "texto": "El presidente fue acusado de corrupción y se desató una protesta.",
        "titulo": "Acusación de corrupción",
        "url": "manual"
    })
    assert response.status_code == 200
    assert "resumen" in response.json()

def test_clasificar():
    response = client.post("/clasificar", json={
        "texto": "El presidente fue acusado de soborno..."
    })
    assert response.status_code == 200
    assert "categorias" in response.json()

def test_imagen():
    response = client.get("/imagen?prompt=Un gato espacial")
    assert response.status_code == 200
    assert isinstance(response.json(), str)

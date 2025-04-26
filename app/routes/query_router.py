# app/routes/query_router.py
from fastapi import APIRouter
from app.services.rag_query_services import buscar_articulos_similares

router = APIRouter()

@router.post("/query", tags=["RAG"], summary="Buscar artículos similares")
def consultar_articulos(pregunta: str, n: int = 5):
    """
    Recibe una pregunta y devuelve artículos similares basados en embeddings.
    """
    resultados = buscar_articulos_similares(pregunta, n)
    return {"resultados": resultados}

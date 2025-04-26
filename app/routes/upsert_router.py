# app/routes/upsert_router.py
from fastapi import APIRouter
from app.services.rag_query_service import agregar_articulo_a_chroma
from app.models.schemas import TextoResumenInput

router = APIRouter()

@router.post("/upsert", tags=["RAG"], summary="Agregar artículo manualmente")
def insertar_articulo(data: TextoResumenInput):
    """
    Permite agregar un nuevo artículo a la base RAG enviando título, texto y url.
    """
    respuesta = agregar_articulo_a_chroma(data.titulo, data.texto, data.url)
    return respuesta

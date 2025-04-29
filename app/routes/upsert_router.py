from fastapi import APIRouter
from app.models.schemas import UpsertInput  # 👈 importar el modelo correcto
from app.services.rag_query_services import agregar_articulo_a_chroma

router = APIRouter()

@router.post("/upsert", tags=["RAG"], summary="Agregar artículo manualmente")
def insertar_articulo(data: UpsertInput):
    """
    Permite agregar un nuevo artículo a la base RAG enviando título, texto y url.
    """
    respuesta = agregar_articulo_a_chroma(data.titulo, data.texto, data.url)
    return respuesta

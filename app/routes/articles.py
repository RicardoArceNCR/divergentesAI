from fastapi import APIRouter
from app.services.scraper import obtener_urls_home, extraer_contenido
from app.services.embedding_utils import generar_embedding
from app.logic.summary import resumir
from app.models.article import Articulo
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get(
    "/articulos",
    response_model=list[Articulo],
    tags=["Artículos"],
    summary="Obtener artículos resumidos con embedding"
)
def obtener_articulos(n: int = 5):
    urls = obtener_urls_home()
    resultados = []

    for url in urls[:n]:
        try:
            data = extraer_contenido(url)
            resumen = resumir(data["texto"])
            embedding = generar_embedding(data["texto"])

            resultados.append(Articulo(
                titulo=data["titulo"],
                resumen=resumen,
                url=url,
                autor=data.get("autor", ""),
                fecha=data.get("fecha", ""),
                embedding=embedding  # <- agregado aquí
            ))

        except Exception as e:
            logger.warning(f"Error con {url}: {e}")
            continue

    return resultados  # ✅ solución




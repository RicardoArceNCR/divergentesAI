# Standard Library
import logging

# FastAPI
from fastapi import APIRouter

# Internal Logic
from app.logic.summary import resumir
from app.services.scrapers.coordinador_scrapers import obtener_urls_home
from app.services.scraper_extractor import extraer_contenido
from app.services.nlp_utils.embedding_utils import generar_embedding

# Models
from app.models.article import Articulo, ArticuloExtendido

logger = logging.getLogger(__name__)
router = APIRouter()

def procesar_url(url: str, extendido: bool = False):
    try:
        data = extraer_contenido(url)
        resumen = resumir(data["texto"])
        embedding = generar_embedding(data["texto"])

        if extendido:
            return ArticuloExtendido(
                titulo=data.get("titulo", ""),
                subtitulo=data.get("subtitulo", ""),
                texto=data.get("texto", ""),
                resumen=resumen,
                url=url,
                autor=data.get("autor", ""),
                fecha=data.get("fecha", ""),
                links_relacionados=data.get("links_relacionados", []),
                links_externos=data.get("links_externos", []),
                documentos=data.get("documentos", []),
                apis=data.get("apis", []),
                anuncios=data.get("anuncios", []),
                colores=data.get("colores", []),
                embedding=embedding
            )
        else:
            return Articulo(
                titulo=data["titulo"],
                resumen=resumen,
                url=url,
                autor=data.get("autor", ""),
                fecha=data.get("fecha", ""),
                embedding=embedding
            )
    except Exception as e:
        logger.warning(f"Error con {url}: {e}")
        return None

@router.get("/articulos", response_model=list[Articulo], tags=["Artículos"], summary="Obtener artículos resumidos con embedding")
def obtener_articulos(n: int = 5):
    urls = obtener_urls_home()
    return [a for a in (procesar_url(url) for url in urls[:n]) if a]

@router.get("/articulos/extendidos", response_model=list[ArticuloExtendido])
def articulos_ext(n: int = 5):
    urls = obtener_urls_home()
    return [a for a in (procesar_url(url, extendido=True) for url in urls[:n]) if a]

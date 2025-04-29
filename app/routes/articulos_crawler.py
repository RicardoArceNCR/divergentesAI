# FastAPI
from fastapi import APIRouter

# Servicios internos
from app.services.crawler import crawler_dinamico
from app.services.scraper_extractor import extraer_contenido
from app.logic.summary import resumir
from app.services.nlp_utils.embedding_utils import generar_embedding

# Modelos
from app.models.article import Articulo

# Inicializar router
router = APIRouter()

def procesar_url(url: str) -> Articulo:
    try:
        data = extraer_contenido(url)
        resumen = resumir(data["texto"])
        embedding = generar_embedding(data["texto"])
        
        return Articulo(
            titulo=data.get("titulo", ""),
            resumen=resumen,
            url=url,
            autor=data.get("autor", ""),
            fecha=data.get("fecha", ""),
            embedding=embedding
        )
    except Exception as e:
        print(f"⚠️ Error procesando {url}: {e}")
        return None

@router.get("/articulos_crawler", response_model=list[Articulo])
def articulos_crawler(n: int = 50, profundidad: int = 2):
    urls = crawler_dinamico(base_url="https://www.divergentes.com", max_n=n, max_depth=profundidad)
    return [a for a in (procesar_url(url) for url in urls) if a]

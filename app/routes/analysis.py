from fastapi import APIRouter
from app.services.coordinador_scrapers import obtener_urls_home
from app.logic.analisis import procesar_articulo_completo

router = APIRouter()

@router.get("/articulos/analizados", tags=["Análisis completo"])
def analizar_articulos(n: int = 5):
    urls = obtener_urls_home(n=n)
    resultados = []

    for url in urls:
        print(f"📰 Analizando: {url}")
        resultado = procesar_articulo_completo(url)
        if resultado:
            resultados.append(resultado)

    return resultados

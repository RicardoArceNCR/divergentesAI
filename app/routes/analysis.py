from fastapi import APIRouter
from app.services.scrapers.coordinador_scrapers import obtener_urls_home
from app.logic.analisis import procesar_articulo_completo
import os
import json
from datetime import datetime

router = APIRouter()

@router.get("/articulos/analizados", tags=["Análisis completo"])
def analizar_articulos(n: int = 15):
    urls = obtener_urls_home(n=n)
    resultados = []

    for url in urls:
        print(f"📰 Analizando: {url}")
        resultado = procesar_articulo_completo(url)
        if resultado:
            resultados.append(resultado)

            # Guardar log del resultado
            nombre_archivo = url.strip("/").split("/")[-1][:50] or "sin-nombre"
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            ruta = f"logs/articulos/{nombre_archivo}-{timestamp}.json"

            os.makedirs("logs/articulos", exist_ok=True)
            with open(ruta, "w") as f:
                json.dump(resultado, f, indent=2, ensure_ascii=False)

    return resultados

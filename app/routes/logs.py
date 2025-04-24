from fastapi import APIRouter
import os
import json
from app.models.article import ArticuloExtendido  # usar modelo extendido

router = APIRouter()

@router.get("/logs/resumen", response_model=list[ArticuloExtendido], tags=["Logs"])
def resumen_logs(n: int = 10):
    carpeta = "logs/articulos"
    if not os.path.exists(carpeta):
        return []

    files = sorted(os.listdir(carpeta), reverse=True)[:n]
    resultados = []

    for file in files:
        path = os.path.join(carpeta, file)
        with open(path, encoding="utf-8") as f:
            try:
                datos = json.load(f)
                resultados.append(datos)
            except Exception as e:
                print(f"⚠️ Error al leer {file}: {e}")

    return resultados

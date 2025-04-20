from fastapi import APIRouter
from app.services.openai_client import generar_imagen

router = APIRouter()

@router.get("/imagen", tags=["Imágenes"], summary="Generar imagen desde prompt")
def obtener_imagen(prompt: str):
    url = generar_imagen(prompt)
    return {"imagen_url": url}

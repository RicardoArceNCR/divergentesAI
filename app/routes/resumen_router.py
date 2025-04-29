# app/routes/resumen_router.py

from fastapi import APIRouter
from app.models.schemas import ResumenInput
from summarizer import Summarizer

router = APIRouter()

# Instancia única del modelo BERT
bert_model = Summarizer()

@router.post("/resumir", tags=["Resúmenes"], summary="Resumir un texto automáticamente")
def resumir_texto(data: ResumenInput):
    """
    Recibe un texto y devuelve un resumen automático usando BERT extractivo, adaptado al tamaño del texto.
    """
    texto_original = data.texto.strip()
    longitud_texto = len(texto_original)

    if longitud_texto < 500:
        # No tiene sentido resumir textos muy pequeños
        resumen_generado = texto_original
    elif 500 <= longitud_texto <= 1500:
        # Resumen más corto
        resumen_generado = bert_model(texto_original, min_length=30, max_length=100)
    else:
        # Resumen más extenso para textos largos
        resumen_generado = bert_model(texto_original, min_length=100, max_length=300)

    return {"resumen": resumen_generado}

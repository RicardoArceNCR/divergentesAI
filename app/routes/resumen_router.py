# app/routes/resumen_router.py
from fastapi import APIRouter
from app.models.schemas import TextoResumenInput, TextoOutput
from app.logic.summary import resumir

router = APIRouter()

@router.post("/resumir", response_model=TextoOutput, tags=["Resúmenes"], summary="Resumir un texto")
def resumir_texto(data: TextoResumenInput):
    """
    Genera un resumen básico del texto proporcionado.
    """
    resumen = resumir(data.texto)
    return {"resumen": resumen}

# app/routes/resumen_router.py
from fastapi import APIRouter
from app.models.schemas import ResumenInput
from app.logic.summary import resumir

router = APIRouter()

@router.post("/resumir", tags=["Resúmenes"], summary="Resumir un texto")
def ResumenInput(data: ResumenInput):
    """
    Genera un resumen básico del texto proporcionado.
    """
    resumen = resumir(data.texto)
    return {"resumen": resumen}

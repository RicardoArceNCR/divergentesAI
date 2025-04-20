from fastapi import APIRouter
from app.logic.summary import resumir
from app.schemas import TextoResumenInput, TextoOutput

router = APIRouter()

@router.post("/resumir", response_model=TextoOutput, tags=["Resúmenes"], summary="Resumir texto enviado")
def resumir_texto(data: TextoResumenInput):
    resumen = resumir(data.texto)
    return {"resumen": resumen}

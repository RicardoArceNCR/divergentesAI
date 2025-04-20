from fastapi import APIRouter
from app.models.article import TextoResumenInput
from app.models.classification import ClassificationOutput
from app.services.prompt_utils import clasificar_texto

router = APIRouter()

@router.post(
    "/clasificar",
    response_model=ClassificationOutput,
    tags=["Clasificación"],
    summary="Clasificar texto por temática",
    responses={
        200: {
            "description": "Resultado de clasificación por temática",
            "content": {
                "application/json": {
                    "example": {
                        "categorias": {
                            "política": 0.75,
                            "corrupción": 0.33,
                            "derechos_humanos": 0.5
                        }
                    }
                }
            }
        }
    }
)
def clasificar(data: TextoResumenInput):
    resultado = clasificar_texto(data.texto)
    return {"categorias": resultado}

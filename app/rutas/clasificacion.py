from fastapi import APIRouter
from app.modelos import TextoResumenInput, ClasificacionOutput
from app.services.prompt_utils import clasificar_texto

router = APIRouter()

@router.post(
    "/clasificar",
    response_model=ClasificacionOutput,
    tags=["Clasificación"],
    summary="Clasificar texto por temática",
    responses={
        200: {
            "description": "Resultado de clasificación por temática",
            "content": {
                "application/json": {
                    "example": {
                        "categorias": {
                            "politica": 0.75,
                            "corrupcion": 0.33,
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

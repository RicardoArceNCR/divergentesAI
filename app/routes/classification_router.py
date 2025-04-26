from fastapi import APIRouter
from app.models.article import TextoResumenInput
from app.models.classification import ClassificationOutput
from app.nlp.clasificador import clasificar_texto  # <-- clasificación temática
from app.nlp.entidades_extractores import extraer_entidades

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
    """
    Clasifica un texto recibido por temática utilizando embeddings semánticos.
    """
    resultado = clasificar_texto(data.texto)
    return {"categorias": resultado}


@router.post(
    "/entidades",
    tags=["Clasificación"],
    summary="Extraer entidades nombradas del texto",
    responses={
        200: {
            "description": "Entidades extraídas: personas, organizaciones y lugares",
            "content": {
                "application/json": {
                    "example": {
                        "entidades": {
                            "PERSONA": ["Daniel Ortega", "Rosario Murillo"],
                            "ORG": ["Gobierno de Nicaragua"],
                            "LOC": ["Managua"]
                        }
                    }
                }
            }
        }
    }
)
def entidades(data: TextoResumenInput):
    """
    Extrae entidades nombradas del texto utilizando spaCy (personas, organizaciones, lugares).
    """
    resultado = extraer_entidades(data.texto)
    return {"entidades": resultado}

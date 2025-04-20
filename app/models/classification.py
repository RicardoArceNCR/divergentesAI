from pydantic import BaseModel, Field
from typing import Dict

class ClassificationOutput(BaseModel):
    categorias: Dict[str, float] = Field(
        ...,
        example={
            "política": 0.95,
            "corrupción": 0.8,
            "derechos_humanos": 0.5
        },
        description="Temas detectados en el texto con su nivel de relevancia"
    )

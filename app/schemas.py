from pydantic import BaseModel
from typing import Optional, Dict

class TextoResumenInput(BaseModel):
    texto: str
    titulo: Optional[str] = "Texto sin título"
    url: Optional[str] = "manual"

class TextoOutput(BaseModel):
    resumen: str

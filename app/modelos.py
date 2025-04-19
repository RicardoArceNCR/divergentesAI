from pydantic import BaseModel, Field
from typing import Optional
from typing import Dict

class URLInput(BaseModel):
    url: str

class TextoInput(BaseModel):
    texto: str
    

class Articulo(BaseModel):
    titulo: str
    resumen: Optional[str] = None
    url: str
    autor: Optional[str] = None
    fecha: Optional[str] = None

    
class ClasificacionOutput(BaseModel):
    categorias: Dict[str, float]  # Ej: {"politica": 0.95, "corrupcion": 0.75}
    

class TextoResumenInput(BaseModel):
    texto: str = Field(..., example="El presidente fue acusado de soborno y se desató una protesta en la capital.")

class TextoOutput(BaseModel):
    resumen: str
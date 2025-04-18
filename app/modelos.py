from pydantic import BaseModel
from typing import Optional

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

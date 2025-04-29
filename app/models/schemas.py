from pydantic import BaseModel
from typing import Optional, Dict

# Para /resumir
class ResumenInput(BaseModel):
    texto: str

# Para /upsert
class UpsertInput(BaseModel):
    titulo: str
    texto: str
    url: str

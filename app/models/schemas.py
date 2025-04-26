# app/models/schemas.py

from pydantic import BaseModel
from typing import List, Optional, Dict

# 📄 Para insertar artículos manualmente a Chroma
class ArticleInput(BaseModel):
    id: str
    texto: str
    metadatos: Optional[Dict[str, str]] = None

# 📄 Para consultar artículos similares (query RAG)
class QueryInput(BaseModel):
    pregunta: str
    n_resultados: Optional[int] = 5

# 📄 Para resumir un texto
class ResumenInput(BaseModel):
    texto: str

# 📄 Para clasificar un texto
class ClasificacionInput(BaseModel):
    texto: str

# 📄 Para extraer entidades de un texto
class EntidadesInput(BaseModel):
    texto: str

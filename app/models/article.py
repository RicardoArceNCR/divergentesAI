from pydantic import BaseModel, Field
from typing import Optional, List

class URLInput(BaseModel):
    url: str = Field(..., description="URL del artículo o recurso a procesar")

class TextoInput(BaseModel):
    texto: str = Field(..., description="Texto libre para análisis o clasificación")

class TextoResumenInput(BaseModel):
    texto: str = Field(
        ..., 
        example="El presidente fue acusado de soborno...", 
        description="Texto a resumir"
    )

class TextoOutput(BaseModel):
    resumen: str = Field(..., description="Resumen generado del texto enviado")

class Articulo(BaseModel):
    titulo: str = Field(..., description="Título principal del artículo")
    resumen: Optional[str] = Field(None, description="Resumen automático del contenido")
    url: str = Field(..., description="Enlace original del artículo")
    autor: Optional[str] = Field(None, description="Nombre del autor (si está disponible)")
    fecha: Optional[str] = Field(None, description="Fecha de publicación (si está disponible)")
    embedding: Optional[List[float]] = None  # <- NUEVO

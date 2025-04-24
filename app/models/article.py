from pydantic import BaseModel, Field, validator, HttpUrl
from typing import Optional, List


# 🧾 Entradas simples

class URLInput(BaseModel):
    url: HttpUrl = Field(..., description="URL del artículo o recurso a procesar")

class TextoInput(BaseModel):
    texto: str = Field(..., description="Texto libre para análisis o clasificación")

class TextoResumenInput(BaseModel):
    texto: str = Field(
        ...,
        example="El presidente fue acusado de soborno...",
        description="Texto a resumir"
    )


# 🧠 Salidas generales

class TextoOutput(BaseModel):
    resumen: str = Field(..., description="Resumen generado del texto enviado")


# 📰 Artículo base

class Articulo(BaseModel):
    titulo: str = Field(..., description="Título principal del artículo")
    resumen: Optional[str] = Field(None, description="Resumen automático del contenido")
    url: HttpUrl = Field(..., description="Enlace original del artículo")
    autor: Optional[str] = Field(None, description="Nombre del autor (si está disponible)")
    fecha: Optional[str] = Field(None, description="Fecha de publicación (si está disponible)")
    embedding: Optional[List[float]] = Field(
        None,
        description="Vector de representación semántica del artículo",
        example=[0.123, -0.456, 0.789]
    )

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "titulo": "Protestas sacuden la capital",
                "resumen": "Se registraron protestas masivas...",
                "url": "https://ejemplo.com/articulo",
                "autor": "Juan Pérez",
                "fecha": "2025-04-20",
                "embedding": [0.123, -0.456, 0.789]
            }
        }


# 🧩 Artículo extendido

class ArticuloExtendido(Articulo):
    subtitulo: Optional[str] = Field(None, description="Subtítulo del artículo")
    texto: str = Field(..., description="Cuerpo completo del artículo")

    links_relacionados: Optional[List[str]] = Field(default_factory=list, description="Enlaces internos del sitio")
    links_externos: Optional[List[str]] = Field(default_factory=list, description="Enlaces a otros medios o recursos")
    documentos: Optional[List[str]] = Field(default_factory=list, description="Documentos enlazados (PDF, DOCX, etc.)")
    apis: Optional[List[str]] = Field(default_factory=list, description="Enlaces relacionados con APIs detectadas")
    anuncios: Optional[List[str]] = Field(default_factory=list, description="Fragmentos de texto identificados como anuncios")
    colores: Optional[List[str]] = Field(default_factory=list, description="Colores CSS identificados en estilos inline")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "titulo": "Protestas sacuden la capital",
                "subtitulo": "Grupos civiles se enfrentan con la policía",
                "texto": "El conflicto comenzó luego de...",
                "resumen": "Se registraron protestas masivas...",
                "url": "https://ejemplo.com/articulo",
                "autor": "Juan Pérez",
                "fecha": "2025-04-20",
                "links_relacionados": ["https://ejemplo.com/relacionado1"],
                "links_externos": ["https://medioexterno.com/nota"],
                "documentos": ["https://ejemplo.com/archivo.pdf"],
                "apis": ["https://api.ejemplo.com/endpoint"],
                "anuncios": ["Publicidad 1"],
                "colores": ["#123456", "#abcdef"],
                "embedding": [0.123, -0.456, 0.789]
            }
        }

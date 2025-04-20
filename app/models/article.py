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
    embedding: Optional[List[float]] = Field(
    None,
    description="Vector de representación semántica del artículo",
    example=[0.123, -0.456, 0.789]
    )
    
    class ArticuloExtendido(BaseModel):
    titulo: str = Field(..., description="Título del artículo")
    subtitulo: Optional[str] = Field(None, description="Subtítulo del artículo")
    texto: str = Field(..., description="Cuerpo completo del artículo")
    resumen: Optional[str] = Field(None, description="Resumen automático")
    url: str = Field(..., description="URL original del artículo")
    autor: Optional[str] = Field(None, description="Autor del artículo")
    fecha: Optional[str] = Field(None, description="Fecha de publicación")

    links_relacionados: Optional[List[str]] = Field(default_factory=list)
    links_externos: Optional[List[str]] = Field(default_factory=list)
    documentos: Optional[List[str]] = Field(default_factory=list)
    apis: Optional[List[str]] = Field(default_factory=list)
    anuncios: Optional[List[str]] = Field(default_factory=list)
    colores: Optional[List[str]] = Field(default_factory=list)

    embedding: Optional[List[float]] = Field(
        None,
        description="Vector semántico del artículo",
        example=[0.123, -0.456, 0.789]
    )

    class Config:
        schema_extra = {
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



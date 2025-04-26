# app/logic/analizador.py
from app.extraction.extractor_scraper_based import extraer_contenido
from app.logic.summary import resumir
from app.logic.classification import clasificar_texto
from app.logic.entidades import extraer_entidades
from app.services.embedding_utils import generar_embedding
from app.utils.error_handler import manejar_error

class AnalizadorArticulo:
    def __init__(self, url: str):
        self.url = url
        self.datos = {}
        self.resultado = {}

    def extraer(self):
        try:
            self.datos = extraer_contenido(self.url)
        except Exception as e:
            manejar_error(f"Error al extraer: {self.url}", e)

    def analizar(self):
        if not self.datos.get("texto"):
            manejar_error("Texto vacío", Exception())
            return

        texto = self.datos["texto"]

        self.resultado = {
            "titulo": self.datos.get("titulo", "Sin título"),
            "subtitulo": self.datos.get("subtitulo", ""),
            "autor": self.datos.get("autor", ""),
            "fecha": self.datos.get("fecha", ""),
            "url": self.url,
            "texto": texto,
            "resumen": resumir(texto),
            "categorias": clasificar_texto(texto),
            "entidades": extraer_entidades(texto),
            "embedding": generar_embedding(texto),
        }

    def ejecutar(self):
        self.extraer()
        self.analizar()
        return self.resultado

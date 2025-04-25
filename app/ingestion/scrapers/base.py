# app/ingestion/scrapers/base.py
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def obtener_urls_home(self) -> list:
        pass

    @abstractmethod
    def extraer_contenido(self, url: str) -> dict:
        pass

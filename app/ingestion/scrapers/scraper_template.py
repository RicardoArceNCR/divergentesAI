# app/ingestion/scrapers/scraper_template.py

from abc import ABC, abstractmethod
from typing import List, Dict
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

class BaseScraper(ABC):
    @abstractmethod
    def obtener_urls_home(self, n: int = 2) -> List[str]:
        pass

    @abstractmethod
    def extraer_contenido(self, url: str) -> Dict[str, str]:
        pass

class ScraperTemplate(BaseScraper):
    TEXTOS_BASURA = [
        "Todos los derechos reservados",
        "Esta publicación puede ser utilizada",
        "previa autorización de la dirección del medio",
        "[email protected]",
        "Mostrar más resultados"
    ]

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.scraper = cloudscraper.create_scraper()
        self.timeout = 10  # segundos

    def es_articulo(self, url: str) -> bool:
        return (
            url.strip("/").count("/") >= 2
            and not any(x in url for x in ["opinion", "podcast", "etiqueta", "categoria"])
        )

    def obtener_urls_home(self, n: int = 5) -> List[str]:
        urls = []
        try:
            response = self.scraper.get(self.base_url, timeout=self.timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a", href=True)

            for link in links:
                full_url = urljoin(self.base_url, link["href"])
                if self.es_articulo(full_url) and full_url not in urls:
                    urls.append(full_url)
                if len(urls) >= n:
                    break
        except Exception as e:
            logging.error(f"Error al obtener URLs del home: {e}")
        return urls

    def extraer_contenido(self, url: str) -> Dict[str, str]:
        contenido = {"titulo": "", "texto": ""}
        try:
            response = self.scraper.get(url, timeout=self.timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            titulo_tag = soup.find("h1")
            texto_tags = soup.find_all(["p", "div"], recursive=True)

            if titulo_tag:
                contenido["titulo"] = titulo_tag.get_text(strip=True)

            texto_final = []
            for tag in texto_tags:
                if tag.name == "p" and tag.get_text(strip=True):
                    texto = tag.get_text(strip=True)
                    if not any(basura in texto for basura in self.TEXTOS_BASURA):
                        texto_final.append(texto)

            contenido["texto"] = " ".join(texto_final)

        except Exception as e:
            logging.error(f"Error extrayendo contenido de {url}: {e}")
        
        return contenido

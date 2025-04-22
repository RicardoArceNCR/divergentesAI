
from abc import ABC, abstractmethod
from typing import List, Dict
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class BaseScraper(ABC):
    @abstractmethod
    def obtener_urls_home(self, n: int = 5) -> List[str]:
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

    def es_articulo(self, url: str) -> bool:
        return (
            url.strip("/").count("/") >= 15
            and not any(x in url for x in ["opinion", "podcast", "autor", "etiqueta", "tag", "category"])
            and not url.endswith("/")
        )

    def obtener_urls_desde_url(self, url: str, n: int = 5) -> List[str]:
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        urls = set()

        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a["href"])
            if self.es_articulo(full_url):
                urls.add(full_url)

        return list(urls)[:n]

    def obtener_urls_home(self, n: int = 5) -> List[str]:
        return self.obtener_urls_desde_url(self.base_url, n)

    def extraer_contenido(self, url: str) -> Dict[str, str]:
        print(f"🧠 Scraping: {url}")
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Título
        titulo = soup.title.string.strip() if soup.title else "Sin título"

        # Subtítulo
        subtitulo_tag = soup.find("h2", class_="td-post-sub-title") or soup.find("div", class_="subtitulo")
        subtitulo = subtitulo_tag.get_text(strip=True) if subtitulo_tag else ""

        # Autor
        autor_tag = soup.find("a", class_="td-post-author-name") or soup.find("span", class_="td-author-name")
        autor = autor_tag.get_text(strip=True) if autor_tag else ""

        # Fecha
        fecha_tag = soup.find("time", class_="entry-date") or soup.find("time", {"datetime": True})
        fecha = fecha_tag["datetime"] if fecha_tag and fecha_tag.has_attr("datetime") else ""

        # Contenido principal - con múltiples candidatos
        candidatos = [
            soup.find("div", class_="td-post-content"),
            soup.find("div", class_="post-content"),
            soup.find("article"),
            soup.find("div", {"class": lambda x: x and "content" in x}),
        ]
        contenido = next((c for c in candidatos if c), None)

        if not contenido:
            print(f"⚠️ No se encontró contenido en: {url}")
            return {
                "titulo": titulo,
                "subtitulo": subtitulo,
                "texto": "",
                "autor": autor,
                "fecha": fecha,
                "links_relacionados": [],
                "links_externos": [],
                "documentos": [],
                "apis": [],
                "anuncios": [],
                "colores": []
            }

        # Extraer y limpiar texto
        parrafos = contenido.find_all("p")
        texto = ' '.join(p.get_text().strip() for p in parrafos)

        for basura in self.TEXTOS_BASURA:
            if basura in texto:
                texto = texto.split(basura)[0].strip()

        if not texto.strip():
            print(f"⚠️ El artículo en {url} no tiene texto útil.")
        
        # Links
        all_links = [a['href'] for a in soup.find_all("a", href=True)]
        links_relacionados = [href for href in all_links if "divergentes.com" in href and self.es_articulo(href)]
        links_externos = [href for href in all_links if "divergentes.com" not in href]

        return {
            "titulo": titulo,
            "subtitulo": subtitulo,
            "texto": texto,
            "autor": autor,
            "fecha": fecha,
            "links_relacionados": links_relacionados,
            "links_externos": links_externos,
            "documentos": [],
            "apis": [],
            "anuncios": [],
            "colores": []
        }




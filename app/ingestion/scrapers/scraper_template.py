# app/ingestion/scrapers/scraper_template.py
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.ingestion.scrapers.base_scraper import BaseScraper
from typing import List, Dict

class ScraperTemplate(BaseScraper):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def obtener_urls_desde_url(self, url: str, n: int = 5) -> List[str]:
        import requests
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        urls = set()

        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a["href"])
            urls.add(full_url)

        return list(urls)[:n]

    def obtener_urls_home(self, n: int = 5) -> List[str]:
        return self.obtener_urls_desde_url(self.base_url, n)

    def extraer_contenido(self, url: str) -> Dict[str, str]:
        import requests
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        titulo = soup.title.string.strip() if soup.title else "Sin título"
        subtitulo_tag = soup.find("h2", class_="td-post-sub-title")
        subtitulo = subtitulo_tag.get_text(strip=True) if subtitulo_tag else ""

        autor_tag = soup.find("a", class_="td-post-author-name")
        autor = autor_tag.get_text(strip=True) if autor_tag else ""

        fecha_tag = soup.find("time", class_="entry-date")
        fecha = fecha_tag.get("datetime", "") if fecha_tag else ""

        candidatos = [
            soup.find("div", class_="td-post-content"),
            soup.find("div", class_="post-content"),
            soup.find("article"),
            soup.find("div", class_=lambda x: x and "content" in x)
        ]
        contenido = next((c for c in candidatos if c), None)

        if not contenido:
            print(f"⚠️ No se encontró contenido en: {url}")
            return {}

        parrafos = contenido.find_all("p")
        texto = "\n".join(p.get_text(strip=True) for p in parrafos if p.get_text(strip=True))

        return {
            "titulo": titulo,
            "subtitulo": subtitulo,
            "autor": autor,
            "fecha": fecha,
            "texto": texto
        }

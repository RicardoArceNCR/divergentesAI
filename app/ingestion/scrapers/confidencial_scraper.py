from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from app.ingestion.scrapers.base_scraper import BaseScraper

class ConfidencialScraper(BaseScraper):
    def __init__(self, base_url="https://confidencial.digital"):
        self.base_url = base_url

    def obtener_urls_home(self) -> list:
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        urls = set()

        for a in soup.find_all("a", href=True):
            full_url = urljoin(self.base_url, a["href"])
            if self.base_url in full_url:
                urls.add(full_url)

        return [
            url for url in urls
            if ("/nacion/" in url or "/politica/" in url)
            and not any(x in url for x in ["etiqueta", "video", "opinion"])
        ]

    def extraer_contenido(self, url: str) -> dict:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        titulo_tag = soup.find("h1")
        titulo = titulo_tag.get_text(strip=True) if titulo_tag else "Sin título"

        subtitulo_tag = soup.find("h2")
        subtitulo = subtitulo_tag.get_text(strip=True) if subtitulo_tag else ""

        autor_tag = soup.find("span", class_="autor")
        autor = autor_tag.get_text(strip=True).replace("Por ", "") if autor_tag else ""

        fecha_tag = soup.find("time")
        fecha = fecha_tag.get("datetime") if fecha_tag else ""

        contenido_div = soup.find("div", class_="td-post-content") or soup.find("article")
        if not contenido_div:
            print(f"⚠️ No se encontró contenido en: {url}")
            return {}

        parrafos = contenido_div.find_all("p")
        texto = "\n".join(p.get_text(strip=True) for p in parrafos if p.get_text(strip=True))

        return {
            "titulo": titulo,
            "subtitulo": subtitulo,
            "autor": autor,
            "fecha": fecha,
            "texto": texto
        }

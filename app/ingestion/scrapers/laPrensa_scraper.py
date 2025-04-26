from bs4 import BeautifulSoup
import requests
from app.ingestion.scrapers.base import BaseScraper

class LaPrensaScraper(BaseScraper):
    def extraer_contenido(self, url: str) -> dict:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Título
        titulo_tag = soup.find("h1", class_="title")
        titulo = titulo_tag.get_text(strip=True) if titulo_tag else "Sin título"

        # Subtítulo (si existe)
        subtitulo_tag = soup.find("div", class_="sub-title")
        subtitulo = subtitulo_tag.get_text(strip=True) if subtitulo_tag else ""

        # Autor
        autor_tag = soup.find("span", class_="autor")
        autor = autor_tag.get_text(strip=True).replace("Por ", "") if autor_tag else ""

        # Fecha
        fecha_tag = soup.find("span", class_="td-post-date")
        fecha = fecha_tag.get_text(strip=True) if fecha_tag else ""

        # Contenido
        contenido_div = soup.find("div", class_="td-post-content tagdiv-type")
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

    def obtener_urls_home(self):
        # Implementalo o dejalo pasar por ahora
        return []

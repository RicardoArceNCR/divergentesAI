import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.base_scrapers.scraper_template import ScraperTemplate

class DivergentesScraper(ScraperTemplate):
    def __init__(self, base_url="https://www.divergentes.com/"):
        self.base_url = base_url
        self.scraper = cloudscraper.create_scraper()

    def obtener_urls_home(self) -> list:
        response = self.scraper.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        urls = set()

        for a in soup.find_all("a", href=True):
            full_url = urljoin(self.base_url, a["href"])
            if self.base_url in full_url:
                urls.add(full_url)

        return [
            url for url in urls
            if not any(x in url for x in ["etiqueta", "podcast", "opinion", "autor", "#"])
            and len(url.split("/")) >= 5
        ]

    def extraer_contenido(self, url: str) -> dict:
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Contenido principal
        contenedor = (
            soup.find("div", class_="td-post-content")
            or soup.find("div", class_="entry-content")
            or soup.find("article")
        )
        if contenedor:
            parrafos = contenedor.find_all("p")
            texto = "\n".join(
                p.get_text(strip=True)
                for p in parrafos
                if p.get_text(strip=True)
            )
        else:
            print(f"⚠️ No se encontró contenedor de texto en: {url}")
            texto = ""

        # Título principal
        titulo = soup.find("meta", property="og:title")
        titulo = titulo["content"].strip() if titulo else soup.title.string.strip() if soup.title else ""

        # Subtítulo si existe
        subtitulo = soup.find("h2")
        subtitulo = subtitulo.get_text(strip=True) if subtitulo else ""

        # Autor y fecha
        autor = soup.find("meta", attrs={"name": "author"})
        autor = autor["content"].strip() if autor else ""

        fecha = soup.find("meta", attrs={"property": "article:published_time"})
        fecha = fecha["content"].strip() if fecha else ""

        return {
            "titulo": titulo,
            "subtitulo": subtitulo,
            "autor": autor,
            "fecha": fecha,
            "texto": texto,
        }

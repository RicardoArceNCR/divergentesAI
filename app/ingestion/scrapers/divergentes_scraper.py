# Scraper para Divergentes robusto
# app/ingestion/scrapers/divergentes_scraper.py

from app.ingestion.scrapers.scraper_template import ScraperTemplate
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from typing import List

class DivergentesScraper(ScraperTemplate):
    def __init__(self):
        super().__init__(base_url="https://www.divergentes.com")

    def es_articulo(self, url: str) -> bool:
        url = url.split("#")[0]

        if not url.startswith(self.base_url):
            return False

        path = url.replace(self.base_url, "")
        path = path.strip("/")

        if not path:
            return False
        if path in ["categoria", "etiqueta", "opinion", "podcast", "investigaciones"]:
            return False
        if any(x in path for x in ["#", "?", "search", "tag"]):
            return False

        return path.count("/") >= 1

    def obtener_urls_home(self, n: int = 30) -> List[str]:
        urls = []
        try:
            response = self.scraper.get(self.base_url, timeout=self.timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Ignorar links del menú hamburguesa
            sidenav = soup.find("aside", id="sidenavmenu")
            links_hamburguesa = {urljoin(self.base_url, a["href"]) for a in sidenav.find_all("a", href=True)} if sidenav else set()

            # Ignorar links del navbar principal
            nav = soup.find("nav")
            links_navbar = {urljoin(self.base_url, a["href"]) for a in nav.find_all("a", href=True)} if nav else set()

            for link in soup.find_all("a", href=True):
                full_url = urljoin(self.base_url, link["href"])
                if full_url not in links_hamburguesa and full_url not in links_navbar:
                    # Aquí ya no filtramos por "es_articulo"
                    urls.append(full_url)

            urls = list(dict.fromkeys(urls))  # Eliminamos duplicados
            urls = urls[:n]  # Limitar solo si n está definido

        except Exception as e:
            print(f"⚠️ Error obteniendo URLs de Divergentes: {e}")

        return urls

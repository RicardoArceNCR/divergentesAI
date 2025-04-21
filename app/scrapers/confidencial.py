from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from app.scrapers.base import BaseScraper

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
            if "/nacion/" in url or "/politica/" in url
            and not any(x in url for x in ["etiqueta", "video", "opinion"])
        ]

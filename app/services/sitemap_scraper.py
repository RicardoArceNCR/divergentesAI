import requests
from bs4 import BeautifulSoup
from typing import List

def obtener_urls_sitemap(base_url: str = "https://www.divergentes.com/sitemap_index.xml", n: int = 50) -> List[str]:
    urls = []
    try:
        # Leer el índice de sitemaps
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "xml")

        # Extraer todos los sitemaps secundarios
        sitemap_links = [loc.get_text(strip=True) for loc in soup.find_all("loc")]

        for sitemap_url in sitemap_links:
            sitemap_response = requests.get(sitemap_url, timeout=10)
            sitemap_response.raise_for_status()
            sitemap_soup = BeautifulSoup(sitemap_response.content, "xml")

            # Extraer URLs reales de artículos
            for loc in sitemap_soup.find_all("loc"):
                articulo_url = loc.get_text(strip=True)
                urls.append(articulo_url)
                if len(urls) >= n:
                    break

            if len(urls) >= n:
                break

        urls = list(dict.fromkeys(urls))  # Elimina duplicados
        return urls

    except Exception as e:
        print(f"⚠️ Error leyendo sitemap: {e}")
        return []

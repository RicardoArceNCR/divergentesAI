from typing import List
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawler_dinamico(base_url: str, max_n: int = 50, max_depth: int = 2) -> List[str]:
    """
    Crawler sencillo compatible con Cloudflare.
    """
    scraper = cloudscraper.create_scraper()
    urls_visitadas = set()
    urls_por_visitar = [(base_url, 0)]  # (url, profundidad)

    while urls_por_visitar and len(urls_visitadas) < max_n:
        url_actual, profundidad = urls_por_visitar.pop(0)

        if url_actual in urls_visitadas:
            continue

        try:
            response = scraper.get(url_actual, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Marcar como visitado
            urls_visitadas.add(url_actual)

            # Solo expandir si no hemos alcanzado max_depth
            if profundidad < max_depth:
                for link in soup.find_all("a", href=True):
                    full_url = urljoin(base_url, link['href'])
                    full_url = full_url.rstrip("/")

                    if any(full_url.startswith(x) for x in ["mailto:", "tel:"]):
                        continue
                    if full_url.endswith((".pdf", ".jpg", ".png", ".docx", ".xlsx", ".zip")):
                        continue
                    if "facebook.com" in full_url or "twitter.com" in full_url:
                        continue

                    parsed = urlparse(full_url)
                    if parsed.netloc == urlparse(base_url).netloc:
                        if full_url not in urls_visitadas:
                            urls_por_visitar.append((full_url, profundidad + 1))

        except Exception as e:
            print(f"⚠️ Error en {url_actual}: {e}")

    return list(urls_visitadas)[:max_n]

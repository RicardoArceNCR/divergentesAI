from app.scrapers import SCRAPER_REGISTRY

def obtener_urls_home(n=5) -> list[str]:
    """
    Itera sobre los scrapers registrados y devuelve una lista combinada de URLs de artículos.
    """
    urls = []

    for nombre, scraper in SCRAPER_REGISTRY.items():
        try:
            urls += scraper.obtener_urls_home()[:n]
        except Exception as e:
            print(f"❌ Error al obtener URLs de {nombre}: {e}")

    return urls

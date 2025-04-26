# app/ingestion/ingestion_pipeline.py
from app.ingestion.scrapers.scraper_registry import SCRAPER_REGISTRY

def recolectar_urls(n=5):
    urls = []
    for nombre, scraper in SCRAPER_REGISTRY.items():
        try:
            urls += scraper.obtener_urls_home()[:n]
        except Exception as e:
            print(f"Error scraper {nombre}: {e}")
    return urls

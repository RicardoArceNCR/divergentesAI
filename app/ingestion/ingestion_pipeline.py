from app.ingestion.scrapers.divergentes import DivergentesScraper
from app.ingestion.cleaners.text_cleaner import clean_text
import json
import os

def run_ingestion_guardar(n=5):
    scraper = DivergentesScraper()
    urls = scraper.obtener_urls_home()[:n]
    resultados = []

    for url in urls:
        try:
            data = scraper.extraer_contenido(url)
            data["texto"] = clean_text(data["texto"])  # limpieza adicional
            data["url"] = url
            resultados.append(data)
        except Exception as e:
            print(f"❌ Error al procesar {url}: {e}")

    os.makedirs("data/processed", exist_ok=True)
    with open("data/processed/divergentes.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(resultados)} artículos guardados.")

if __name__ == "__main__":
    run_ingestion_guardar()

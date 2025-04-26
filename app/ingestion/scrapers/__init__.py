from app.ingestion.scrapers.divergentes_scraper import DivergentesScraper
from app.ingestion.scrapers.laPrensa_scraper import LaPrensaScraper
from app.ingestion.scrapers.confidencial_scraper import ConfidencialScraper

SCRAPER_REGISTRY = {
    "divergentes": DivergentesScraper(),
    "laPrensa": LaPrensaScraper(),
    "confidencial": ConfidencialScraper(),
}

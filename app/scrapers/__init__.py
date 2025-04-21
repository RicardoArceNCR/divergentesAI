from app.scrapers.divergentes import DivergentesScraper
from app.scrapers.laPrensa import LaPrensaScraper
from app.scrapers.confidencial import ConfidencialScraper

SCRAPER_REGISTRY = {
    "divergentes": DivergentesScraper(),
    "laPrensa": LaPrensaScraper(),
    "confidencial": ConfidencialScraper(),
}

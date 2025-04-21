from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def obtener_urls_home(self) -> list:
        pass

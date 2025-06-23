# src/scrapers/base_scraper.py
from abc import ABC, abstractmethod

class BaseSongScraper(ABC):
    @abstractmethod
    def fetch_songs(self, limit: int = 50) -> list:
        """Fetch a list of songs up to a limit."""
        pass

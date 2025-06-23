# src/scrapers/saregama_scraper.py
import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseSongScraper

class SaregamaHindiScraper(BaseSongScraper):
    def fetch_songs(self, limit=50):
        print("🔍 Starting fetch_songs in SaregamaHindiScraper")
        base_url = "https://www.saregama.com"
        target_url = f"{base_url}/hindi/song/top-songs"

        response = requests.get(target_url)
        soup = BeautifulSoup(response.content, "html.parser")
        song_cards = soup.select("div.card")[:limit]

        songs = []
        for idx, card in enumerate(song_cards):
            title_tag = card.select_one("div.song_name a")
            artist_tag = card.select_one("div.artists a")

            if not title_tag or not artist_tag:
                continue

            songs.append({
                "id": f"hindi_{idx+1}",
                "title": title_tag.text.strip(),
                "artists": [artist_tag.text.strip()],
                "languages": ["Hindi"],
                "context_tags": ["bollywood", "popular"],
                "familiarity_score": round(1 - idx / limit, 2),
                "audio_features": {}
            })
        print(f"📦 Scraped {len(songs)} songs")
        for song in songs[:5]:
            print(song)
        return songs

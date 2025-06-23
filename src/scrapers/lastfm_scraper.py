import requests
from bs4 import BeautifulSoup
import random
import time

class LastfmHindiScraper:
    def __init__(self):
        self.base_url = "https://www.last.fm/tag/hindi/tracks"

    def fetch_songs(self, limit=50):
        print("🔍 Starting fetch_songs in LastfmHindiScraper")
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        songs = []
        page = 1

        while len(songs) < limit:
            url = f"{self.base_url}?page={page}"
            print(f"🌐 Fetching page {page}: {url}")
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"❌ Failed to fetch page {page}. Status code: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, "html.parser")
            track_elements = soup.select("tbody tr")

            if not track_elements:
                print("⚠️ No track elements found. Stopping.")
                break

            for row in track_elements:
                try:
                    title_elem = row.select_one("td.chartlist-name a")
                    artist_elem = row.select_one("td.chartlist-artist a")
                    if not title_elem or not artist_elem:
                        continue

                    song = {
                        "title": title_elem.text.strip(),
                        "artists": [artist_elem.text.strip()],
                        "languages": ["Hindi"],
                        "context_tags": ["hindi", "lastfm"],
                        "audio_features": {
                            "tempo": random.randint(60, 160),
                            "energy": round(random.uniform(0.4, 0.9), 2),
                            "valence": round(random.uniform(0.2, 0.8), 2),
                            "danceability": round(random.uniform(0.3, 0.9), 2)
                        },
                        "popularity_score": random.randint(40, 100)
                    }

                    songs.append(song)
                    if len(songs) >= limit:
                        break
                except Exception as e:
                    print(f"⚠️ Error parsing row: {e}")

            page += 1
            time.sleep(1.5)

        print(f"📦 Scraped {len(songs)} songs")
        return songs

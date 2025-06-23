from src.utils.paths import DATA_DIR
#from src.scrapers.saregama_scraper import SaregamaHindiScraper
from src.scrapers.lastfm_scraper import LastfmHindiScraper
import os
import json

def generate_from_scraper(scraper_class, filename="hindi_songs.json", limit=50):
    scraper = scraper_class()
    
    songs = scraper.fetch_songs(limit=limit)

    out_path = os.path.join(DATA_DIR, filename)
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(songs, f, indent=2, ensure_ascii=False)

    print(f"✅ {len(songs)} songs saved to {out_path}")

# Call the scraper
if __name__ == "__main__":
    generate_from_scraper(
        scraper_class=LastfmHindiScraper,
        filename="hindi_songs.json",
        limit=50
    )

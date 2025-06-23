import json
import os
from src.utils.paths import DATA_DIR

data = [
    {
        "id": "song_1",
        "title": "Tera Yaar Hoon Main",
        "artists": ["Arijit Singh"],
        "languages": ["Hindi"],
        "context_tags": ["emotional", "friendship"],
        "audio_features": {
            "tempo": 75,
            "energy": 0.52,
            "valence": 0.60,
            "danceability": 0.45
        },
        "familiarity_score": 0.85
    },
    {
        "id": "song_2",
        "title": "Fix You",
        "artists": ["Coldplay"],
        "languages": ["English"],
        "context_tags": ["uplifting", "night"],
        "audio_features": {
            "tempo": 65,
            "energy": 0.40,
            "valence": 0.30,
            "danceability": 0.32
        },
        "familiarity_score": 0.90
    }
]

out_path = os.path.join(DATA_DIR, "songs.json")
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Seed data written to {out_path}")
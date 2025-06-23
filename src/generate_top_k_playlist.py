import os
import json
from src.utils.paths import DATA_DIR
from src.logic.similarity import get_top_k_songs


def load_user_vector():
    """
    Dummy user vector. You can later replace this with real-time input from CLI or Web UI.
    """
    return {
        "energy": 0.7,
        "valence": 0.5,
        "tempo": 100,
        "danceability": 0.6,
        "acousticness": 0.4,
        "instrumentalness": 0.3
    }


def load_song_data(filename="spotify_songs.json"):
    """
    Load curated song list from your data directory.
    """
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return []
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    print(f"📁 Using song data from: {DATA_DIR}")

    user_vector = load_user_vector()
    songs = load_song_data()

    if not songs:
        print("⚠️ No songs found. Aborting.")
        exit(1)

    top_k = get_recommended_songs(user_vector)

    print("\n🎵 Top %d Songs for this user:", k)
    for i, song in enumerate(top_k, 1):
        title = song.get("title", "Unknown Title")
        artists = ", ".join(song.get("artists", []))
        print(f"{i}. {title} by {artists}")

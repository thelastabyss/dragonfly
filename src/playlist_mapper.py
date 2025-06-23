# Placeholder for logic to match emotion input with playlists
import json

def load_songs(path="data/songs.json"):
    with open(path) as f:
        return json.load(f)

songs = load_songs()
print(f"{len(songs)} songs loaded.")

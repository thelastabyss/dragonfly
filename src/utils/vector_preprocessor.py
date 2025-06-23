import json
import numpy as np
import os
from src.utils.paths import DATA_DIR, CONFIG_DIR, SONG_JSON_PATH, SONG_MATRIX_PATH, SONG_METADATA_PATH
from config.settings import ACTIVE_FEATURES, FEATURE_RANGES, SONG_POPULARITY_THRESHOLD  # assumes this imports settings.py

ORDERED_FEATURES = [f for f in ACTIVE_FEATURES if f in FEATURE_RANGES]

def normalize_feature(val, feature):
    min_val, max_val = FEATURE_RANGES[feature]
    return (val - min_val) / (max_val - min_val + 1e-8)

def run_vector_preprocessing(input_json_path):
    matrix = []
    song_meta = []

    with open(input_json_path, "r", encoding="utf-8") as f:
        songs = json.load(f)

    filtered_songs = [
        song for song in songs
        if isinstance(song.get("popularity"), (int, float)) and song["popularity"] >= SONG_POPULARITY_THRESHOLD
    ]
    for song in filtered_songs:
        try:
            vec = [normalize_feature(float(song[feat]), feat) for feat in ORDERED_FEATURES]
            matrix.append(vec)
            song_meta.append(song)  # or just song['id'] if needed
        except Exception:
            continue

    np.save(SONG_MATRIX_PATH, np.array(matrix, dtype=np.float32))
    with open(SONG_METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(song_meta, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved matrix with shape: {len(matrix)} x {len(ORDERED_FEATURES)}")

if __name__ == "__main__":
    run_vector_preprocessing(SONG_JSON_PATH)

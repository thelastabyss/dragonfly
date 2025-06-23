import os
import json
import pandas as pd
from src.utils.paths import DATA_DIR

INPUT_CSV = os.path.join(DATA_DIR, "SpotifyAudioFeaturesApril2019.csv")
OUTPUT_JSON = os.path.join(DATA_DIR, "spotify_songs.json")

def convert_csv_to_json(input_csv=INPUT_CSV, output_json=OUTPUT_JSON):
    df = pd.read_csv(input_csv)

    # Clean column names
    df.columns = [col.strip() for col in df.columns]

    # Convert to records and dump as JSON
    records = df.to_dict(orient="records")

    # Optionally, add unique ID
    for i, song in enumerate(records):
        song["id"] = f"spotify_song_{i+1}"

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(records)} songs to {output_json}")

if __name__ == "__main__":
    convert_csv_to_json()

import os
import numpy as np
import json

# Absolute path to the root of the project (assumes this file lives in /utils/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Common folders
DATA_DIR = os.getenv("DATA_DIR", os.path.join(BASE_DIR, "data"))
OUTPUT_DIR = os.getenv("OUTPUT_DIR", os.path.join(BASE_DIR, "output"))
CONFIG_DIR = os.getenv("CONFIG_DIR", os.path.join(BASE_DIR, "config"))
SONG_JSON_PATH = os.path.join(DATA_DIR, "spotify_songs.json")
SONG_MATRIX_PATH = os.path.join(DATA_DIR, "song_matrix.npy")
SONG_METADATA_PATH = os.path.join(DATA_DIR, "index_to_song.json")
FEEDBACK_DATA_PATH = os.path.join(OUTPUT_DIR, "feedback_log.csv")

SONG_MATRIX, SONG_META = None, None
if os.path.isfile(SONG_MATRIX_PATH):
    SONG_MATRIX = np.load(SONG_MATRIX_PATH)
if os.path.isfile(SONG_METADATA_PATH):
    with open(SONG_METADATA_PATH, "r", encoding="utf-8") as f:
        SONG_META = json.load(f)

print(f"Using DATA_DIR: {DATA_DIR}")
print(f"Using OUTPUT_DIR: {OUTPUT_DIR}")
print(f"Using CONFIG_DIR: {CONFIG_DIR}")
print(f"Using SONG_JSON_PATH: {SONG_JSON_PATH}")
print(f"Using SONG_MATRIX_PATH: {SONG_MATRIX_PATH}")
print(f"Using SONG_METADATA_PATH: {SONG_METADATA_PATH}")
print(f"Using FEEDBACK_DATA_PATH: {FEEDBACK_DATA_PATH}")

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CONFIG_DIR, exist_ok=True)

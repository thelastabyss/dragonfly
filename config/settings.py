# config/settings.py

K=30
N=12
JITTER_SCALE=0.05
SONG_POPULARITY_THRESHOLD=50

FEATURE_RANGES = {
    "energy": (0, 1),
    "valence": (0, 1),
    "danceability": (0, 1),
    "acousticness": (0, 1),
    "instrumentalness": (0, 1),
    "tempo": (0, 250),       # Approximate tempo range in bpm
    "popularity": (0, 100)    # Optional, unused for now
}

USER_FEATURE_MAPPING = {
    "energy": {
        "energetic": {"weight": 0.3, "polarity": 1},
        "tired": {"weight": 0.3, "polarity": -1},
        "focused": {"weight": 0.1, "polarity": 1},
    },
    "valence": {
        "happy": {"weight": 0.3, "polarity": 1},
        "low": {"weight": 0.3, "polarity": -1},
        "anxious": {"weight": 0.1, "polarity": -1},
        "peaceful": {"weight": 0.1, "polarity": 1}
    },
    "danceability": {
        "energetic": {"weight": 0.3, "polarity": 1},
        "tired": {"weight": 0.3, "polarity": -1},
        "happy": {"weight": 0.2, "polarity": 1}
    },
    "acousticness": {
        "peaceful": {"weight": 0.2, "polarity": 1},
        "anxious": {"weight": 0.2, "polarity": -1}
    },
    "instrumentalness": {
        "focused": {"weight": 0.2, "polarity": 1},
        "casual": {"weight": 0.2, "polarity": -1}
    },
    "tempo": {
        "energetic": {"weight": 0.3, "polarity": 1},
        "tired": {"weight": 0.3, "polarity": -1}
    }
}

ACTIVE_FEATURES = list(USER_FEATURE_MAPPING.keys())
print("ACTIVE_FEATURES: ", ACTIVE_FEATURES)

USER_INPUT_LABEL_VALUES = {
    "mood_happy_low": ["low", "happy"],
    "mood_anxious_peaceful": ["peaceful", "anxious"],
    "mood_energetic_tired": ["tired", "energetic"],
    "mental_clarity":["casual", "focused"]
}
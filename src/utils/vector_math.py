import numpy as np
from config.settings import FEATURE_RANGES

def normalize_vector_dict(vec_dict):
    """Takes a dict of feature_name: value, returns normalized np.array"""
    norm_vec = []
    for key in FEATURE_RANGES:
        val = vec_dict.get(key, 0.0)
        min_val, max_val = FEATURE_RANGES[key]
        if max_val - min_val == 0:
            norm_vec.append(0.0)
        else:
            norm_vec.append((val - min_val) / (max_val - min_val))
    return np.array(norm_vec)

def cosine_similarity(vec1, vec2):
    """Both vec1 and vec2 must be numpy arrays"""
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

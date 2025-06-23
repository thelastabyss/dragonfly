import numpy as np
import json
import os
import random
from src.utils.paths import SONG_MATRIX, SONG_META
from config.settings import ACTIVE_FEATURES, FEATURE_RANGES, JITTER_SCALE, K, N

ORDERED_FEATURES = [f for f in ACTIVE_FEATURES if f in FEATURE_RANGES]

def feature_dict_to_vector(user_feature_dict):
    vec = []
    for feat in ORDERED_FEATURES:
        if feat in user_feature_dict:
            val = float(user_feature_dict[feat])
            vec.append(val)
        else:
            vec.append(0.0)  # pad with zero if not available
    return np.array(vec, dtype=np.float32)

def add_jitter_to_scores(scores, jitter_scale=JITTER_SCALE):
    jitter = np.random.normal(loc=0, scale=JITTER_SCALE, size=scores.shape)
    return scores+jitter

def apply_rerank_precision_cutoff(top_k_indices, cutoff):
    random.shuffle(top_k_indices)
    return top_k_indices[:cutoff]

def apply_userfacing_rules(top_n_indices):
    return top_n_indices

def get_recommended_songs(user_feature_dict, k=K, n=N):
    user_vec = feature_dict_to_vector(user_feature_dict)
    print("User vec shape: ", user_vec.shape)
    print("User vector: ", user_vec)
    print("Song matrix shape: ", SONG_MATRIX.shape)
    sim_scores = SONG_MATRIX @ user_vec
    print("Similar scores shape: ", sim_scores.shape)
    sim_scores = add_jitter_to_scores(sim_scores)
    top_k_indices = np.argsort(sim_scores)[::-1][:k]
    print("Top K Indices: ", top_k_indices)
    print("Top scores: ", sim_scores[top_k_indices])
    
    top_n_indices = apply_rerank_precision_cutoff(top_k_indices, n)
    print("Top scores after random: ", sim_scores[top_n_indices])
    top_n_indices = apply_userfacing_rules(top_n_indices)
    print("Top N Indices: ", top_n_indices)

    return [SONG_META[i] for i in top_n_indices]

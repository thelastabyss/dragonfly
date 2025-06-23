# src/utils/user_to_vector.py

import json
import os
import importlib.util
import sys
from src.utils.paths import CONFIG_DIR
from config.settings import USER_FEATURE_MAPPING, ACTIVE_FEATURES, USER_INPUT_LABEL_VALUES

# Load settings.py (feature mappings and weights)
# CONFIG_PATH = os.path.join(CONFIG_DIR, "settings.py")
# spec = importlib.util.spec_from_file_location("settings", CONFIG_PATH)
# settings = importlib.util.module_from_spec(spec)
# sys.modules["settings"] = settings
# spec.loader.exec_module(settings)

def flatten_user_input(user_inputs):
    flattened_input = {}
    for input_field, raw_value in user_inputs.items():
        label_value_index = 0 if (raw_value < 0) else 1
        opp_value_index = 1 - label_value_index
        value_list = USER_INPUT_LABEL_VALUES[input_field]

        flattened_input[value_list[label_value_index]] = abs(raw_value)
        flattened_input[value_list[opp_value_index]] = 0.0
        
    return flattened_input

def compute_user_feature_dict(user_input):
    print("User Inputs: ", user_input)
    user_token_values = flatten_user_input(user_input)
    print("User Flattened Inputs: ", user_token_values)
    user_feature_dict = {}

    for feature in ACTIVE_FEATURES:
        mapping = USER_FEATURE_MAPPING.get(feature, {})
        feature_val = 0.5

        for token, spec in mapping.items():
            weight = spec.get("weight", 1.0)
            polarity = spec.get("polarity", 1.0)
            value = user_token_values.get(token, 0.0)

            feature_val += value * weight * polarity

        user_feature_dict[feature] = feature_val

    print("User features: ", user_feature_dict)
    return user_feature_dict
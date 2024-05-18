import numpy as np

def preprocess_input(features, scaler):
    features_array = np.array(features)
    scaled_features = scaler.transform(features_array)
    return scaled_features

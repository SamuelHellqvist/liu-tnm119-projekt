import pandas as pd
import joblib

#load the model
clf_loaded = joblib.load('random_forest_model.pkl')

# Load MFCCs from CSV file
test_mfcc_features_positive = pd.read_csv('features/test_mfcc_features_pingpongBall.csv', header=None).values
test_mfcc_features_negative = pd.read_csv('features/test_mfcc_features_backgroundNoise.csv', header=None).values

# Ensure the features are in the correct shape (1 sample with multiple features)
#test_mfcc_features = test_mfcc_features_positive
test_mfcc_features = test_mfcc_features_negative

# Predict using the trained model
test_prediction = clf_loaded.predict(test_mfcc_features)

# Print prediction
label = "Ping Pong Ball" if test_prediction[0] == 1 else "Background Noise"
print(f"Prediction for the test audio: {label}")
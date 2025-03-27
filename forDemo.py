import pandas as pd
import joblib

#load the model
clf_loaded = joblib.load('random_forest_model.pkl')

ball = pd.read_csv('ball.csv', header=None).values
hello = pd.read_csv('hello.csv', header=None).values

#choose which feature to test
test_mfcc_features = ball
#test_mfcc_features = hello

# Predict using the trained model
test_prediction = clf_loaded.predict(test_mfcc_features)

# Print prediction
# label = "Ping Pong Ball" if test_prediction[0] == 1 else "Background Noise"
# print(f"Prediction for the test audio: {label}")

# Count ones and zeros in predictions
print(test_prediction)

ones = sum(1 for prediction in test_prediction if prediction == 1)
zeros = sum(1 for prediction in test_prediction if prediction == 0)

# Classify based on counts
final_label = "Ping Pong Ball" if ones > zeros * 0.3 else "Background Noise"
print(f"Final classification based on all predictions: {final_label}")
import pandas as pd
import joblib

#load the model
clf_loaded = joblib.load('random_forest_model.pkl')

# Load MFCCs from CSV file
test_mfcc_features_positive = pd.read_csv('features/test_mfcc_features_pingpongBall.csv', 
                                          header=None).values
test_mfcc_features_negative = pd.read_csv('features/test_mfcc_features_backgroundNoise.csv', 
                                          header=None).values
test_mfcc_features_silence = pd.read_csv('features/test_mfcc_features_silence.csv', 
                                         header=None).values
test_mfcc_features_silentPositive = pd.read_csv('features/test_mfcc_features_silentPingPongBall.csv', 
                                                header=None).values
test_mfcc_features_positive_2 = pd.read_csv('features/test_mfcc_features_pongStuds.csv', 
                                            header=None).values
test_mfcc_features_speech = pd.read_csv('features/test_mfcc_features_prat.csv',
                                            header=None).values
test_mfcc_features_positive_3 = pd.read_csv('features/test_mfcc_features_pos_test.csv', 
                                            header=None).values
test_mfcc_features_trappan_pos = pd.read_csv('features/test_mfcc_features_trappan_pos.csv', 
                                            header=None).values

# Ensure the features are in the correct shape (1 sample with multiple features)
#test_mfcc_features = test_mfcc_features_positive #should be ping pong ball
#test_mfcc_features = test_mfcc_features_negative #should be background noise
#test_mfcc_features = test_mfcc_features_silence #should be background noise
#test_mfcc_features = test_mfcc_features_silentPositive #should be ping pong ball, denna blir FEL
#test_mfcc_features = test_mfcc_features_positive_2 #should be ping pong ball
#test_mfcc_features = test_mfcc_features_speech #should be negative
#test_mfcc_features = test_mfcc_features_positive_3 #should be positive, from the internet
test_mfcc_features = test_mfcc_features_trappan_pos #should be positive, recorded at trappan

# Predict using the trained model
test_prediction = clf_loaded.predict(test_mfcc_features)

# Print prediction
label = "Ping Pong Ball" if test_prediction[0] == 1 else "Background Noise"
print(f"Prediction for the test audio: {label}")
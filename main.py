import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree

# Load MFCCs from CSV file
mfcc_features = pd.read_csv('features/mfcc_features.csv', header=None).values

# Manually label the data (example labels)
labels = [1 if i % 2 == 0 else 0 for i in range(len(mfcc_features))]  # 0: background noise, 1: ping pong ball

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(mfcc_features, labels)

# Evaluate the model
predictions = clf.predict(mfcc_features)
accuracy = np.mean(predictions == labels)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Load MFCCs from CSV file
test_mfcc_features = pd.read_csv('features/test_mfcc_features.csv', header=None).values

# Ensure the features are in the correct shape (1 sample with multiple features)
test_mfcc_features = test_mfcc_features

# Predict using the trained model
test_prediction = clf.predict(test_mfcc_features)

# Print prediction
label = "Ping Pong Ball" if test_prediction[0] == 1 else "Background Noise"
print(f"Prediction for the test audio: {label}")
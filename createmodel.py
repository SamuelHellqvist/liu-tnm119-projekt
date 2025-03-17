import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import joblib

# Load MFCCs from CSV file
mfcc_features = pd.read_csv('features/mfcc_features_big.csv', header=None).values

# Manually label the data (example labels)
labels = [0 if i % 2 == 0 else 1 for i in range(len(mfcc_features))]  # 1: background noise, 0: ping pong ball

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(mfcc_features, labels)

# Evaluate the model
predictions = clf.predict(mfcc_features)
accuracy = np.mean(predictions == labels)
print(f"Model accuracy: {accuracy * 100:.2f}%")


# Save the model to a file
joblib.dump(clf, 'random_forest_model.pkl')


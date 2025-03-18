import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import joblib

# Load MFCCs from CSV file
pos_mfcc_features = pd.read_csv('features/pos_mfcc_features.csv', header=None).values

neg_mfcc_features = pd.read_csv('features/neg_mfcc_features.csv', header=None).values

print(neg_mfcc_features.size)

mfcc_features = np.vstack((pos_mfcc_features, neg_mfcc_features))

print(mfcc_features.size)

# Manually label the data (example labels)
labels = np.hstack((np.ones(pos_mfcc_features.shape[0]), np.zeros(neg_mfcc_features.shape[0])))

print(labels)
# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(mfcc_features, labels)

# # Evaluate the model
# predictions = clf.predict(mfcc_features)
# accuracy = np.mean(predictions == labels)
# print(f"Model accuracy: {accuracy * 100:.2f}%")


# Save the model to a file
joblib.dump(clf, 'random_forest_model.pkl')


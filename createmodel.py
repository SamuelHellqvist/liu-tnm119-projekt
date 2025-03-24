import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from individual pong sounds
for i in range(115):
    dynamic_string = f"features/linus_data/pong_{i+1}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    # Adding the new feature to a big vector
    if i == 0:
        individual_mfcc_features = temp_mfcc_features
    else:
        individual_mfcc_features = np.vstack((individual_mfcc_features, temp_mfcc_features))

# Load the synthetic data and save it to the individual_mfcc_features
for i in range(4):
    dynamic_string = f"features/synthetic/synthetic_{i+1}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    # Adding the new feature to a big vector
    if i == 0:
        individual_mfcc_features_synthetic = temp_mfcc_features
    else:
        individual_mfcc_features_synthetic = np.vstack((individual_mfcc_features_synthetic, temp_mfcc_features))

# Load the 5 specialized random files (produced with AI and randomizer)
for i in range(5):
    dynamic_string = f"features/randomly_generated/random_file_{i}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    if i == 0:
        individual_mfcc_features_random = temp_mfcc_features
    else:
        individual_mfcc_features_random = np.vstack((individual_mfcc_features_random, temp_mfcc_features))

# Load MFCCs from CSV file (our original data)
neg_mfcc_features = pd.read_csv('features/neg_mfcc_features.csv', header=None).values

# The training vector
mfcc_features = np.vstack((individual_mfcc_features, 
                           individual_mfcc_features_random, 
                           neg_mfcc_features))

# Manually label the data
labels = np.hstack((np.ones(individual_mfcc_features.shape[0]),
                    np.ones(individual_mfcc_features_random.shape[0]),
                    np.zeros(neg_mfcc_features.shape[0])))

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(mfcc_features, labels)

# Visualize feature importance
feature_importances = clf.feature_importances_
mfcc_features_importances = [f'MFCC-{i+1}' for i in range(len(feature_importances))]

sorted_indices = np.argsort(feature_importances)[::-1]
sorted_features = [mfcc_features_importances[i] for i in sorted_indices]
sorted_importances = feature_importances[sorted_indices]

plt.figure(figsize=(10, 5))
sns.barplot(x=sorted_importances, y=sorted_features, palette="viridis")
plt.xlabel("Feature Importance")
plt.ylabel("MFCC Features")
plt.title("Feature Importance of MFCCs in Table Tennis Sound Classification")
plt.show()

# Visualize the data distribution for the features
plt.figure(figsize=(10, 5))
sns.scatterplot(x=mfcc_features[:, 3], y=mfcc_features[:, 4], hue=labels, palette=["red", "blue"])
#sns.scatterplot(x=mfcc_features[:, 3], y=mfcc_features[:, 4], hue=labels, palette="viridis")
plt.xlabel("MFCC Feature 4")
plt.ylabel("MFCC Feature 5")
plt.title("Data Distribution for the First Two MFCC Features")
plt.show()

# Save the model to a file
joblib.dump(clf, 'random_forest_model.pkl')

print("done")
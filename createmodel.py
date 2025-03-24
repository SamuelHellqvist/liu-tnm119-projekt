import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

#load data from individual pong sonds
for i in range(51):
    dynamic_string = f"linus_data/pong_{i+1}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    # adding the new feature to a big vector
    if i == 0:
        individual_mfcc_features = temp_mfcc_features
    else:
        individual_mfcc_features = np.vstack((individual_mfcc_features, temp_mfcc_features))

#load data from batch 2
for i in range(65):
    dynamic_string = f"features/pong_batch_2/pong_batch_2_{i+1}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    # adding the new feature to a big vector
    if i == 0:
        individual_mfcc_features_batch_2 = temp_mfcc_features
    else:
        individual_mfcc_features_batch_2 = np.vstack((individual_mfcc_features_batch_2, 
                                                        temp_mfcc_features))

#load the synthetic data and save it to the individual_mfcc_features
for i in range(4):
    dynamic_string = f"features/synthetic/synthetic_{i+1}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    # adding the new feature to a big vector
    if i == 0:
        individual_mfcc_features_synthetic = temp_mfcc_features
    else:
        individual_mfcc_features_synthetic = np.vstack((individual_mfcc_features_synthetic, 
                                                        temp_mfcc_features))

#load the 5 specialized synthetic files (produced with chatgpt)
for i in range(5):
    dynamic_string = f"features/synthetic_2/synthetic_file_{i}.csv"
    temp_mfcc_features = pd.read_csv(dynamic_string, header=None).values

    if i == 0:
        individual_mfcc_features_synthetic_2 = temp_mfcc_features
    else:
        individual_mfcc_features_synthetic_2 = np.vstack((individual_mfcc_features_synthetic_2, 
                                                          temp_mfcc_features))

# Load MFCCs from CSV file (our original data)
pos_mfcc_features = pd.read_csv('features/pos_mfcc_features.csv', header=None).values

neg_mfcc_features = pd.read_csv('features/neg_mfcc_features.csv', header=None).values

silence_mfcc_features = pd.read_csv('features/silence_mfcc_features.csv', header=None).values

# Load MFCCs from CSV file (downloaded data from the internet)
thirdparty_mfcc_features = pd.read_csv('features/thirdparty_mfcc_features.csv', header=None).values

# the training vecotr
mfcc_features = np.vstack((individual_mfcc_features, 
                           individual_mfcc_features_synthetic,
                           individual_mfcc_features_synthetic_2,
                           individual_mfcc_features_batch_2, 
                           pos_mfcc_features, 
                           neg_mfcc_features, 
                           silence_mfcc_features, 
                           thirdparty_mfcc_features))


# Manually label the data
labels = np.hstack((np.ones(individual_mfcc_features.shape[0]), 
                    np.ones(individual_mfcc_features_synthetic.shape[0]),
                    np.ones(individual_mfcc_features_synthetic_2.shape[0]),
                    np.ones(individual_mfcc_features_batch_2.shape[0]),
                    np.ones(pos_mfcc_features.shape[0]), 
                    np.zeros(neg_mfcc_features.shape[0]), 
                    np.zeros(silence_mfcc_features.shape[0]), 
                    np.ones(thirdparty_mfcc_features.shape[0])))

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(mfcc_features, labels)

# visulize feature importance
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

# Save the model to a file
joblib.dump(clf, 'random_forest_model.pkl')

print("done")


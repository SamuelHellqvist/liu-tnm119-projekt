import pandas as pd
import numpy as np

# Load the original CSV file
original_df = pd.read_csv('features/test_mfcc_features_silentPingPongBall.csv')

# Function to introduce small variations
def add_variations(df, variation_factor=0.05):
    varied_df = df.copy()
    for column in df.select_dtypes(include=[np.number]).columns:
        varied_df[column] += np.random.normal(0, variation_factor, size=df[column].shape)
    return varied_df

# generate 5 synthetic datapoints
for i in range(5):
    synthetic_df = add_variations(original_df)
    synthetic_df.to_csv(f'synthetic_file_{i}.csv', index=False)


print("Synthetic data generated and saved to 'synthetic_file.csv'")
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from sklearn.cluster import KMeans
import scipy.signal as signal
from scipy.io.wavfile import write
import librosa

#read the big audio file
file_path = "ljudklipp/main_file.wav"
sample_rate, audio_data = wavfile.read(file_path)

# Split audio into segments
segment_length = 1.0  # 1 second segments
num_segments = int(len(audio_data) / (sample_rate * segment_length))
segments = np.array_split(audio_data, num_segments)

# Extract features (MFCCs)
def extract_features(segment, sample_rate):
    mfccs = librosa.feature.mfcc(y=segment, sr=sample_rate, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

features = [extract_features(segment, sample_rate) for segment in segments]
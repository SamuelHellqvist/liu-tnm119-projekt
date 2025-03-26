import pyaudio
import numpy as np
import joblib
import librosa

# Load the pre-trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Parameters
CHUNK = 5120  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 4  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate in Hz

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open input stream (microphone)
stream_input = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

print("Listening for table tennis ball sounds... Press Ctrl+C to stop.")

def extract_features(audio_data, rate):
    """Extract relevant features from audio data for classification."""
    # Convert raw audio bytes to numpy array
    audio_array = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)
    
    # Ensure n_fft is smaller or equal to the chunk size
    n_fft = min(1024, len(audio_array))  # Use CHUNK size or smaller
    
    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=audio_array, sr=rate, n_mfcc=13, n_fft=n_fft, hop_length=512)
    mfccs_mean = np.mean(mfccs, axis=1)  # Take mean of each MFCC feature
    return mfccs_mean.reshape(1, -1)  # Reshape for model input


try:
    while True:
        # Read audio data from microphone
        data = stream_input.read(CHUNK, exception_on_overflow=False)
        
        # Extract features
        features = extract_features(data, RATE)
        
        # Predict using the Random Forest model
        prediction = model.predict(features)
        
        # Check if the model detects a table tennis ball sound
        if prediction[0] == 1:  # Assuming 1 means table tennis ball sound
            print("Detected ball sound!")

except KeyboardInterrupt:
    print("\nStopping...")

# Close stream
stream_input.stop_stream()
stream_input.close()

# Terminate PyAudio
p.terminate()

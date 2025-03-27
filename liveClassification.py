import pyaudio
import numpy as np
import joblib
import librosa

# Load the pre-trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Parameters
CHUNK = 2000 # Number of audio samples per frame
RATE = 1024 # Sampling rate in Hz
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (1 for mono)

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
    audio_array = audio_array / np.max(np.abs(audio_array))

    
    # Detect peaks in the audio signal
    peak_threshold = np.max(audio_array) * 0.5  # Set a threshold for peak detection
    peaks = audio_array[audio_array > peak_threshold]  # Filter values above the threshold

    if len(peaks) == 0:
        return np.zeros((1, 13))  # Return zero features if no peaks are detected

    # Ensure n_fft is smaller or equal to the chunk size
    n_fft = min(512, len(audio_array))  # Use CHUNK size or smaller
    
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

        print(prediction)
        
        # Check if the majority of predictions in the chunk is 1
        # if np.sum(prediction == 1 ) > (len(prediction) / 2):
        #     print("Ball detected!")

        proba = model.predict_proba(features)[0][1]  # Probability of class 1 (ball hit)
        if proba > 0.53:  # Adjust threshold as needed
            print("Ball detected!")

except KeyboardInterrupt:
    print("\nStopping...")

# Close stream
stream_input.stop_stream()
stream_input.close()

# Terminate PyAudio
p.terminate()
    
import pyaudio
import numpy as np
from scipy.fftpack import fft
import joblib

# Load the pre-trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Audio stream configuration
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (mono)
RATE = 44100  # Sampling rate (44.1 kHz)

def extract_features(audio_data):
    """
    Extract features from audio data for model prediction.
    Example: Use FFT to compute frequency-domain features.
    """
    fft_data = fft(audio_data)
    magnitude = np.abs(fft_data[:len(fft_data)//2])  # Take positive frequencies
    return np.mean(magnitude), np.std(magnitude)  # Example features: mean and std

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Listening for ping pong ball sounds...")

try:
    while True:
        # Read audio data from the microphone
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Extract features and make a prediction
        features = np.array(extract_features(audio_data)).reshape(1, -1)
        prediction = model.predict(features)

        # Check if the detected sound is a ping pong ball
        if prediction[0] == 1:  # Assuming 1 represents ping pong ball
            print("Ping pong ball detected!")
except KeyboardInterrupt:
    print("Stopping detection...")

# Clean up
stream.stop_stream()
stream.close()
audio.terminate()
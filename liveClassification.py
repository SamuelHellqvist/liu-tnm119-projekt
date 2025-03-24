import pyaudio
import numpy as np

# Parameters
CHUNK = 514  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate in Hz
def filter_high_frequencies(data, cutoff=1000):
    # Convert byte data to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)
    # Perform FFT
    fft_data = np.fft.rfft(audio_data)
    # Get frequencies
    frequencies = np.fft.rfftfreq(len(audio_data), d=1/RATE)
    # Zero out frequencies below the cutoff
    fft_data[frequencies < cutoff] = 0
    # Perform inverse FFT
    filtered_audio = np.fft.irfft(fft_data).astype(np.int16)
    # Convert back to bytes
    return filtered_audio.tobytes()
# Initialize PyAudio
p = pyaudio.PyAudio()

# Open input stream (microphone)
stream_input = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

# Open output stream (speaker)
stream_output = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       output=True,
                       frames_per_buffer=CHUNK)

print("Listening and playing back... Press Ctrl+C to stop.")

try:
    while True:
        # Read audio data from microphone
        data = stream_input.read(CHUNK)
        # Play back the audio data
        stream_output.write(data)
except KeyboardInterrupt:
    print("\nStopping...")

# Close streams
stream_input.stop_stream()
stream_input.close()
stream_output.stop_stream()
stream_output.close()

# Terminate PyAudio
p.terminate()
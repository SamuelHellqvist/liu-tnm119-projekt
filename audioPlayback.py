import pyaudio

# Audio configuration
CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of audio channels
RATE = 44100  # Sampling rate in Hz

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open input stream (microphone)
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("Start speaking... (Press Ctrl+C to stop)")

try:
    while True:
        # Read audio data from the microphone
        data = stream.read(CHUNK)
        # Playback the audio
        stream.write(data)
except KeyboardInterrupt:
    print("\nStopping audio playback...")

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()
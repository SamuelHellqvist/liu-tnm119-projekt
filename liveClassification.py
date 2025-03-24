import pyaudio

# Parameters
CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate in Hz

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
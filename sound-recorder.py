import pyaudio
import wave
import datetime

# Set the parameters for the audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recording"

# Initialize the PyAudio module
p = pyaudio.PyAudio()

# Open a stream to the microphone
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording started...")

# Start recording
frames = []

try:
    while True:
        data = stream.read(CHUNK)
        frames.append(data)

except KeyboardInterrupt:
    # Stop recording when "Ctrl + C" is pressed
    pass

print("Recording stopped.")

# Close the stream and terminate the PyAudio module
stream.stop_stream()
stream.close()
p.terminate()

# Get the current time in UTC
utc_time = datetime.datetime.utcnow()

# Format the file name based on the current time
WAVE_OUTPUT_FILENAME = WAVE_OUTPUT_FILENAME + "_" + utc_time.strftime("%Y-%m-%d_%H-%M-%S") + ".wav"

# Save the recorded audio as a wave file
wf = wave.open('.\\all-things\\sound-record\\'+WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("Recorded audio saved as " + WAVE_OUTPUT_FILENAME)

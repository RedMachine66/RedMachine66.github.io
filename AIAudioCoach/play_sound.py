import wave
import pyaudio

def play_wav_file(file_path):
    chunk = 1024

    # Open the .wav file
    wf = wave.open(file_path, 'rb')

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    # Read data in chunks and play
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    # Close and terminate
    stream.close()
    p.terminate()

# Replace 'your_file.wav' with the path to your .wav file
file_path = 'output.wav'
play_wav_file(file_path)
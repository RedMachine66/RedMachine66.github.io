import os, sys, openai, time

from deepgram import Deepgram
import asyncio
import aiohttp

import pyaudio
import websockets
import json
import wave
import threading

# Deepgram API key secret
# deb4d75063f33b15d1f6b77d18941033a0e72d76


class AudioRecorder:
    def __init__(self, filename='output.wav', sample_rate=44100, channels=2, format=pyaudio.paInt16):
        self.filename = filename
        self.sample_rate = sample_rate
        self.channels = channels
        self.format = format
        self.frames = []
        self.keep_recording = False
        self.error_occurred = False

    def start_recording(self):
        try:
            self.keep_recording = True
            audio = pyaudio.PyAudio()
            stream = audio.open(format=self.format,
                                channels=self.channels,
                                rate=self.sample_rate,
                                input=True,
                                frames_per_buffer=1024)

            print("Recording... Press Enter to stop.")

            while self.keep_recording:
                data = stream.read(1024)
                self.frames.append(data)

            print("Finished recording.")
            stream.stop_stream()
            stream.close()
            audio.terminate()

            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(audio.get_sample_size(self.format))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.frames))
            wf.close()

            print(f"Audio saved as {self.filename}")

        except Exception as e:
            self.error_occurred = True
            print(f"Error occurred during recording: {e}")

    def stop_recording(self):
        self.keep_recording = False

def record_audio_on_command():
    recorder = AudioRecorder()

    # Start recording in a separate thread
    record_thread = threading.Thread(target=recorder.start_recording)
    record_thread.start()

    # Listen for Enter key press to stop recording
    input("Press Enter to stop recording...")
    recorder.stop_recording()

    if recorder.error_occurred:
        print("There was an error during audio capture.")

record_audio_on_command()
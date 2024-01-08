import os,sys,openai

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

# Function to handle microphone recording and streaming to Nova-2 API
async def record_and_stream_to_nova2(api_key):
    transcripts = []  # To store transcripts

    # Define audio parameters
    audio_format = pyaudio.paInt16
    channels = 1
    rate = 16000  # Sample rate (Nova-2 might have specific requirements)

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open microphone stream
    stream = audio.open(format=audio_format, channels=channels,
                        rate=rate, input=True, frames_per_buffer=1024)

    # Create a websocket connection to Nova-2 API
    async with websockets.connect('wss://api.nova2.deepgram.com/v1/listen?access_token=' + api_key) as websocket:
        while True:
            try:
                # Read audio data from the microphone
                audio_data = stream.read(1024, exception_on_overflow=False)

                # Send audio data to Nova-2 API
                await websocket.send(json.dumps({"audio": audio_data}))

                # Receive and process transcripts from Nova-2
                response = await websocket.recv()
                transcript = json.loads(response)
                transcripts.append(transcript.get("text"))  # Store the transcript text

                # Check if user wants to stop recording (enter 's' to stop)
                stop_signal = input("Enter 's' to stop recording: ")
                if stop_signal.lower() == 's':
                    break

            except websockets.exceptions.ConnectionClosedOK:
                print("Connection closed")
                break

    # Close the microphone stream and PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return transcripts  # Return all the collected transcripts

# Replace 'YOUR_DEEPGRAM_API_KEY' with your actual Nova-2 API Key
nova2_api_key = eb4d75063f33b15d1f6b77d18941033a0e72d76

# Call the function to start recording and streaming to Nova-2
transcripts = asyncio.run(record_and_stream_to_nova2(nova2_api_key))
print("Transcripts:", transcripts)  # Display all the transcripts after recording stops
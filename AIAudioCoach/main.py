import json
import aiohttp
import asyncio
from deepgram import Deepgram
import pyaudio
import wave
import threading
import os
import re
import requests
from playsound import playsound
import playsound
from openai import OpenAI, OpenAIError


def read_file(file_path, mode='rb'):
    try:
        with open(file_path, mode) as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        return None



# Transcription STT function
async def transcribe_audio_file(audio_file_path, transcript_save_path, api_key_file='deepgram_api.key'):
    try:
        print(f"Reading API key from {api_key_file}...")
        api_key = read_file(api_key_file, 'r')
        if api_key is None:
            raise ValueError("API key file could not be read.")
        api_key = api_key.strip()

        # Initialize the Deepgram SDK
        print("Initializing Deepgram SDK...")
        dg_client = Deepgram(api_key)

        # Read the audio file
        print(f"Reading audio file from {audio_file_path}...")
        audio_data = read_file(audio_file_path)
        if audio_data is None:
            raise ValueError("Audio file could not be read.")

        # Send the audio file to Deepgram for transcription
        print("Transcribing audio file...")
        response = await dg_client.transcription.prerecorded({'buffer': audio_data, 'mimetype': 'audio/wav'}, {'punctuate': True})

        # Extract the transcript
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']

        # Save the transcript to a file
        print(f"Saving transcript to {transcript_save_path}...")
        with open('user_answer.txt', 'w') as file:
            file.write(transcript)

        print("Transcription completed successfully.")
        return transcript

    except Exception as e:
        print(f"An error occurred during transcription: {str(e)}")

# # Example usage
# asyncio.run(transcribe_audio_file('path/to/your/audio/file.wav', 'path/to/save/transcript.txt'))



# Recording function
def record_audio(save_path):
    try:
        # Define audio parameters
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 16000  # Sample rate
        frames_per_buffer = 1024

        # Initialize PyAudio
        audio = pyaudio.PyAudio()

        # Open microphone stream
        stream = audio.open(format=audio_format, channels=channels,
                            rate=rate, input=True, frames_per_buffer=frames_per_buffer)

        print("Recording... Press 'Enter' to stop.")

        # Create a list to store the recorded frames
        frames = []

        # Flag to indicate when to stop recording
        stop_recording = False

        def stop_callback():
            nonlocal stop_recording
            input("Press 'Enter' to stop recording...")
            stop_recording = True

        # Start a separate thread for the stop callback
        stop_thread = threading.Thread(target=stop_callback)
        stop_thread.start()

        # Continue recording until the stop signal is received
        while not stop_recording:
            try:
                # Read audio data from the microphone
                audio_data = stream.read(frames_per_buffer, exception_on_overflow=False)
                frames.append(audio_data)
            except IOError as e:
                print("Error recording: ", str(e))
                break

        print("Recording stopped.")

        # Stop the microphone stream and PyAudio
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio as a WAV file
        with wave.open('user_answer.wav', 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(audio_format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))

        print(f"Recording saved at: {save_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# # Example usage
# save_path = 'path/to/save/recorded_audio.wav'
# record_audio(save_path)



# Voice TTS function
def read_file(file_path):
    """
    Read the content of a file and return it.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def sanitize_filename(filename):
    """
    Remove invalid characters from the filename using regular expression.
    """
    return re.sub(r'[^\w.-]', '', filename)

def convert_text_to_speech(input_file, output_folder):
    # Constants
    CHUNK_SIZE = 1024
    OUTPUT_FILENAME = "voice_output.mp3"
    url = "https://api.elevenlabs.io/v1/text-to-speech/nMn9WiA3xiaf8VVZNUS5"

    # Reading API key and input text
    api_key = read_file('11labs.key')
    if api_key is None:
        print("Failed to read API key.")
        return

    input_text = read_file(input_file)
    if input_text is None:
        print("Failed to read input file.")
        return

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": input_text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, sanitize_filename(OUTPUT_FILENAME))

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
            print(f"Audio file saved successfully as {output_path}.")
        else:
            print(f"Error from API: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error during HTTP request: {e}")

# # Example usage:
# convert_text_to_speech('input.txt', 'output')



# Speaker function
def play_audio(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Check if the file is an audio file
        if not file_path.lower().endswith(('.mp3', '.wav')):
            raise ValueError("The file is not a supported audio format (MP3 or WAV).")

        print(f"Attempting to play the audio file: {file_path}")
        
        # Play the audio file
        playsound.playsound(file_path)

        print("Audio playback completed successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# # Example usage
# play_audio("path/to/your/audiofile.mp3")



#GPT Function
def call_openai_api(history_file_location, gpt_output_location, new_history_location, 
                    api_key_file='openai_api.key', 
                    default_gpt_output='gpt_output.txt',
                    default_new_history='chat_history.txt'):

    try:
        # Read API key
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
    except IOError:
        print("Error: Failed to read the API key file.")
        return

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Check if chat history file exists, otherwise use gpt_config.txt
    history_file_to_use = history_file_location if os.path.exists(history_file_location) else 'gpt_config.json'

    try:
        # Read chat history
        with open(history_file_to_use, 'r') as file:
            history = json.load(file)
    except IOError:
        print(f"Error: Failed to read the chat history from {history_file_to_use}.")
        return
    except json.JSONDecodeError:
        print(f"Error: Chat history file {history_file_to_use} is not a valid JSON.")
        return

    try:
        # Call OpenAI API
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=history
        )

        # Extract GPT response
        gpt_response = completion.choices[0].message
    except OpenAIError as e:
        print(f"Error: OpenAI API call failed - {e}")
        return

    try:
        # Save GPT response
        with open(gpt_output_location or default_gpt_output, 'w') as file:
            file.write(gpt_response)
        print("GPT response saved successfully.")
    except IOError:
        print("Error: Failed to write the GPT response to file.")
        return

    try:
        # Update chat history
        history.append({"role": "assistant", "content": gpt_response})

        # Save new chat history
        with open(new_history_location or default_new_history, 'w') as file:
            json.dump(history, file)
        print("Chat history updated successfully.")
    except IOError:
        print("Error: Failed to update the chat history file.")
    except TypeError:
        print("Error: Problem with updating the chat history structure.")

# Example usage
call_openai_api('path/to/chat_history.json', 'gpt_output.txt', 'chat_history.txt')

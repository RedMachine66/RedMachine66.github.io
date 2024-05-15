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
import openai
import shutil
from datetime import datetime
import soundfile
from tempfile import NamedTemporaryFile



def read_file(file_path, mode='rb'):
    try:
        with open(file_path, mode) as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        return None



# Transcription STT function
async def transcribe_audio_file(audio_file_path='user_answer.wav' , chat_history_path='chat_history.json', api_key_file='deepgram_api.key'):
    try:
        print(f"Reading API key from {api_key_file}...")
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
        if not api_key:
            raise ValueError("API key is empty.")

        # Initialize the Deepgram SDK
        print("Initializing Deepgram SDK...")
        dg_client = Deepgram(api_key)

        # Read the audio file
        print(f"Reading audio file from {audio_file_path}...")
        with open(audio_file_path, 'rb') as file:
            audio_data = file.read()
        if not audio_data:
            raise ValueError("Audio file is empty.")

        # Send the audio file to Deepgram for transcription
        print("Transcribing audio file...")
        response = await dg_client.transcription.prerecorded(
            {'buffer': audio_data, 'mimetype': 'audio/wav'},
            {'punctuate': True}
        )

        # Extract the transcript
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']

        # Read existing chat history
        print(f"Reading chat history from {chat_history_path}...")
        with open(chat_history_path, 'r') as file:
            chat_history = json.load(file)

        # Append transcript as a new user message
        chat_history.append({"role": "user", "content": transcript})

        # Save the updated chat history
        print(f"Appending transcript to chat history and saving to {chat_history_path}...")
        with open(chat_history_path, 'w') as file:
            json.dump(chat_history, file)

        print("Transcription completed successfully.")
        return transcript

    except Exception as e:
        print(f"An error occurred during transcription: {str(e)}")

# # Example usage
# asyncio.run(transcribe_audio_file('path/to/your/audio/file.wav', 'path/to/chat/history/file.json'))



# Recording function
def record_audio(save_path = os.getcwd()):
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

def convert_text_to_speech(input_file='gpt_output.txt', output_folder = os.getcwd()):
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
def convert_to_wav(file_path):
    # Load audio file
    data, samplerate = soundfile.read(file_path)

    # Define output file path
    output_path = os.path.splitext(file_path)[0] + ".wav"

    # Write data to WAV file
    soundfile.write(output_path, data, samplerate, subtype='PCM_16')

    return output_path

def play_audio(file_path='voice_output.mp3'):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Check if the file is an audio file
        if not file_path.lower().endswith(('.mp3', '.wav')):
            raise ValueError("The file is not a supported audio format (MP3 or WAV).")

        print(f"Attempting to play the audio file: {file_path}")

        # Convert to WAV if necessary
        if not file_path.lower().endswith('.wav'):
            print("Converting to WAV...")
            file_path = convert_to_wav(file_path)

        # Open the audio file
        wf = wave.open(file_path, 'rb')

        # Instantiate PyAudio
        p = pyaudio.PyAudio()

        # Open PyAudio stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Read data
        data = wf.readframes(1024)

        # Play audio
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Close stream and PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

        print("Audio playback completed successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# play_audio("path/to/your/audiofile.mp3")




#GPT Function v2
def convert_to_chat_history(history):
    """
    Convert the chat history to the required format if necessary.
    """
    if not isinstance(history, list):
        raise TypeError("Chat history must be a list.")
    for msg in history:
        if not isinstance(msg, dict) or "role" not in msg or "content" not in msg:
            raise ValueError("Each message in the chat history must be a dictionary with 'role' and 'content' keys.")
    return history

def call_openai_api(history_file_location='chat_history.json', gpt_output_location='gpt_output.txt', new_history_location='chat_history.json', 
                    api_key_file='openai_api.key'):
    try:
        # Read API key
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
    except IOError:
        print("Error: Failed to read the API key file.")
        return

    # Initialize OpenAI client
    openai.api_key = api_key

    # Check if chat history file exists, otherwise use gpt_config.txt
    history_file_to_use = history_file_location if os.path.exists(history_file_location) else 'gpt_config.json'
    print(f"Using history file: {history_file_to_use}")  # Add this line for debugging

    try:
        # Read chat history
        with open(history_file_to_use, 'r') as file:
            history = json.load(file)
            history = convert_to_chat_history(history)  # Convert to required format
    except FileNotFoundError:
        print(f"Error: Chat history file {history_file_to_use} not found.")
        return
    except IOError:
        print(f"Error: Failed to read the chat history from {history_file_to_use}.")
        return
    except json.JSONDecodeError:
        print(f"Error: Chat history file {history_file_to_use} is not a valid JSON.")
        return
    except (TypeError, ValueError) as e:
        print(f"Error: Invalid chat history format - {e}")
        return

    try:
        # Call OpenAI API for chat completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history
        )

        # Extract GPT response
        gpt_response = response.choices[0].message
    except Exception as e:
        print(f"Error: OpenAI API call failed - {e}")
        return

    try:
        # Save GPT response
        print(type(gpt_response))
        print(gpt_response)
        with open(gpt_output_location, 'w') as file:
            file.write(gpt_response["content"])
        print("GPT response saved successfully.")
    except IOError:
        print("Error: Failed to write the GPT response to file.")
        return

    try:
        # Update chat history
        # Update chat history
        history.append({"role": "assistant", "content": gpt_response["content"]})


        # Save new chat history
        with open(new_history_location, 'w') as file:
            json.dump(history, file)
        print("Chat history updated successfully.")
    except IOError:
        print("Error: Failed to update the chat history file.")
    except TypeError:
        print("Error: Problem with updating the chat history structure.")

# # Example usage
# call_openai_api('path/to/chat_history.json', 'gpt_output.txt', 'chat_history.txt')




# #GPT Function (not working, outdated)
# def convert_to_chat_history(history):
#     """
#     Convert the chat history to the required format if necessary.
#     """
#     if not isinstance(history, list):
#         raise TypeError("Chat history must be a list.")
#     for msg in history:
#         if not isinstance(msg, dict) or "role" not in msg or "content" not in msg:
#             raise ValueError("Each message in the chat history must be a dictionary with 'role' and 'content' keys.")
#     return history


# def call_openai_api(history_file_location = os.getcwd(), gpt_output_location = 'gpt_output.txt', new_history_location = 'chat_history.json', 
#                     api_key_file='openai_api.key'):

#     try:
#         # Read API key
#         with open(api_key_file, 'r') as file:
#             api_key = file.read().strip()
#     except IOError:
#         print("Error: Failed to read the API key file.")
#         return

#     # Initialize OpenAI client
#     client = OpenAI(api_key=api_key)

#     # Check if chat history file exists, otherwise use gpt_config.txt
#     history_file_to_use = history_file_location if os.path.exists(history_file_location) else 'gpt_config.json'

#     try:
#         # Read chat history
#         with open(history_file_to_use, 'r') as file:
#             history = json.load(file)
#             history = convert_to_chat_history(history)  # Convert to required format
#     except IOError:
#         print(f"Error: Failed to read the chat history from {history_file_to_use}.")
#         return
#     except json.JSONDecodeError:
#         print(f"Error: Chat history file {history_file_to_use} is not a valid JSON.")
#         return
#     except (TypeError, ValueError) as e:
#         print(f"Error: Invalid chat history format - {e}")
#         return

#     try:
#         # Call OpenAI API
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=history
#         )

#         # Extract GPT response
#         gpt_response = completion.choices[0].message
#     except OpenAIError as e:
#         print(f"Error: OpenAI API call failed - {e}")
#         return

#     try:
#         # Save GPT response
#         with open(gpt_output_location or default_gpt_output, 'w') as file:
#             file.write(gpt_response)
#         print("GPT response saved successfully.")
#     except IOError:
#         print("Error: Failed to write the GPT response to file.")
#         return

#     try:
#         # Update chat history
#         history.append({"role": "assistant", "content": gpt_response})

#         # Save new chat history
#         with open(new_history_location or default_new_history, 'w') as file:
#             json.dump(history, file)
#         print("Chat history updated successfully.")
#     except IOError:
#         print("Error: Failed to update the chat history file.")
#     except TypeError:
#         print("Error: Problem with updating the chat history structure.")

# # # Example usage
# # call_openai_api('path/to/chat_history.json', 'gpt_output.txt', 'chat_history.txt')



# Coach termination function
def terminate_coach():
    try:
        # Create folder with name starting with date and time
        folder_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "_conversation_history"
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")

        # Move chat_history.json to the new folder
        shutil.move("chat_history.json", os.path.join(folder_name, "chat_history.json"))
        print("Moved chat_history.json to folder.")

        # Create a new chat_history.json file with empty list
        with open(os.path.join(folder_name, "chat_history.json"), "w") as file:
            json.dump([], file)
        print("Created new chat_history.json file.")

        # Delete voice_output.mp3 if exists
        if os.path.exists("voice_output.mp3"):
            os.remove("voice_output.mp3")
            print("Deleted voice_output.mp3")

        # Delete gpt_output.txt if exists
        if os.path.exists("gpt_output.txt"):
            os.remove("gpt_output.txt")
            print("Deleted gpt_output.txt")

        # Delete user_answer.wav if exists
        if os.path.exists("user_answer.wav"):
            os.remove("user_answer.wav")
            print("Deleted user_answer.wav")

        # Delete user_answer.txt if exists
        if os.path.exists("user_answer.txt"):
            os.remove("user_answer.txt")
            print("Deleted user_answer.txt")

        print("All tasks completed.")
    
    except Exception as e:
        print(f"Error: {e}")

# # Example uasge:
# terminate_coach()

print('Preparing session')
terminate_coach()

user_keyboard_input = ''

while True:
    print('Coach initiated, calling gpt')
    call_openai_api()

    print('Converting to speech')
    convert_text_to_speech()

    print('Playing audio')
    play_audio()

    print('Enter any value to continue or enter "x" to end program')
    user_keyboard_input = input()
    if user_keyboard_input == 'x':
        break

    print('Recording')
    record_audio()

    print('Transcribing your answer')
    asyncio.run(transcribe_audio_file())

print('Ending session')
terminate_coach()

# asyncio.run(transcribe_audio_file('output.wav'))

# print('Coach initiated, calling gpt')
# call_openai_api()

# print('Converting text to speech')
# convert_text_to_speech()

# print('Playing audio')
# play_audio()

# print('Recording your answer')
# record_audio()

# print('Transcribing your answer')
# asyncio.run(transcribe_audio_file())

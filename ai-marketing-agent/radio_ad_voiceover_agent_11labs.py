import os
import requests
import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def sanitize_filename(filename):
    """
    Remove invalid characters from the filename using regular expression.
    Only allows alphanumeric characters, underscores, hyphens, and periods.
    """
    valid_chars = re.sub(r'[^\w.-]', '', filename)
    return valid_chars

def get_output_filename(input_file):
    """
    Create an output filename based on the input filename.
    Replace the extension with '.mp3'.
    """
    base = os.path.basename(input_file)
    name, _ = os.path.splitext(base)
    return sanitize_filename(name + '.mp3')

def convert_text_to_speech(input_file, output_folder):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/nMn9WiA3xiaf8VVZNUS5"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": read_file('11labs.key')
    }

    data = {
        "text": read_file(input_file),
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        os.makedirs(output_folder, exist_ok=True)

        output_file = get_output_filename(input_file)
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        print("Audio file saved successfully.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example usage:
# convert_text_to_speech('input.txt', 'output')

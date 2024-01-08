from deepgram import Deepgram
import asyncio
import json

# Your Deepgram API Key
DEEPGRAM_API_KEY = 'deb4d75063f33b15d1f6b77d18941033a0e72d76'

# Location of the file you want to transcribe. Should include filename and extension.
# Example of a local file: '../../Audio/life-moves-pretty-fast.wav'
# Example of a remote file: 'https://static.deepgram.com/examples/interview_speech-analytics.wav'
FILE = 'output.wav'

# Mimetype for the file you want to transcribe
# Include this line only if transcribing a local file
# Example: 'audio/wav'
MIMETYPE = 'YOUR_FILE_MIME_TYPE'

async def main():

    # Initialize the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    # Check whether requested file is local or remote, and prepare source
    if FILE.startswith('http'):
        # file is remote
        # Set the source
        source = {
            'url': FILE
        }
    else:
        # file is local
        # Open the audio file
        audio = open(FILE, 'rb')

        # Set the source
        source = {
            'buffer': audio,
            'mimetype': MIMETYPE
        }

    # Send the audio to Deepgram and get the response
    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                'smart_format': True,
                'model': 'nova-2',
            }
        )
    )

    # Extract transcript from response
    transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

    # Print the transcript to the console
    print(transcript)

    # Save transcript to a text file
    with open('transcript.txt', 'w') as file:
        file.write(transcript)

try:
    # Run the main function
    asyncio.run(main())
except Exception as e:
    print(f'Error: {e}')
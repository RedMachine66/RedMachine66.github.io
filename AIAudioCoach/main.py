from fastapi import FastAPI, File, UploadFile
from deepgram import Deepgram
import asyncio
import json
import os
from datetime import datetime

def read_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()  # Use strip() to remove any leading/trailing whitespace

app = FastAPI()

async def transcribe_audio(api_key, file_path, mime_type):
    deepgram = Deepgram(api_key)

    with open(file_path, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': mime_type}

        # Await the result of the coroutine before returning
        response = await asyncio.to_thread(
            deepgram.transcription.prerecorded,
            source,
            {'punctuate': True, 'model': 'nova'}
        )

    # Convert datetime objects to ISO format
    response = convert_datetime_to_iso(response)

    # Return the response as a dictionary
    return response

def convert_datetime_to_iso(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, list):
        return [convert_datetime_to_iso(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_datetime_to_iso(value) for key, value in obj.items()}
    return obj


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    deepgram_api_key = read_api_key('deepgram_api.key')
    file_mime_type = 'audio/wav'  # Adjust as needed

    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, 'wb') as temp_file:
        content = await file.read()
        temp_file.write(content)

    # Await the transcription result before printing
    transcription_result = await transcribe_audio(deepgram_api_key, temp_file_path, file_mime_type)

    os.remove(temp_file_path)

    # Use await before json.dumps to resolve the serialization issue
    print(json.dumps(transcription_result, indent=4))

    if transcription_result.get("status") == "success":
        return {"message": "File transcribed successfully", "transcription": transcription_result}
    else:
        return {"message": "Error transcribing file", "transcription": transcription_result}
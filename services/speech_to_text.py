import ssl
import certifi
import urllib.request

ssl._create_default_https_context = ssl.create_default_context
ssl._create_default_https_context().load_verify_locations(certifi.where())

import whisper

model = whisper.load_model("base")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]
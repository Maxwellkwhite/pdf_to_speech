import requests
import json
from pypdf import PdfReader


reader = PdfReader('/Users/maxwellwhite/Documents/PythonPractice/Final_Projects/pdf_to_speech/SPORT_AND_GAMES.pdf')
# printing number of pages in pdf file
print(len(reader.pages))
# getting a specific page from the pdf file
page = reader.pages[2]
text = page.extract_text()

URL = "https://api.elevenlabs.io/v1/voices"

XI_API_KEY = ''

CHUNK_SIZE = 1024  
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  
TEXT_TO_SPEAK = text
OUTPUT_PATH = "output.mp3"  


tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY
}

data = {
    "text": TEXT_TO_SPEAK,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8,
        "style": 0.0,
        "use_speaker_boost": True
    }
}
response = requests.post(tts_url, headers=headers, json=data, stream=True)

if response.ok:
    with open(OUTPUT_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
    print("Audio stream saved successfully.")
else:
    print(response.text)

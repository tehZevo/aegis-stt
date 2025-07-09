import os
import base64
import subprocess
from uuid import uuid4

import whisper
from protopost import ProtoPost

from utils import save_audio_file

PORT = os.getenv("PORT", 80)
MODEL = os.getenv("MODEL", "tiny.en")

whisper_model = whisper.load_model(MODEL)

#data should just be a b64 encoded string
def handle(data):
    data = base64.b64decode(data)
    filename = str(uuid4()) + ".wav"
    save_audio_file(data, filename)
    
    #run whisper
    text = whisper_model.transcribe(filename)
    os.remove(filename)

    #respond with text
    return text


routes = {
    "": handle,
}

ProtoPost(routes).start(PORT)

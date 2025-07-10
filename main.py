import os
import base64
from uuid import uuid4

import whisper
from protopost import ProtoPost

PORT = os.getenv("PORT", 80)
MODEL = os.getenv("MODEL", "tiny.en")

whisper_model = whisper.load_model(MODEL)

#data should just be a b64 encoded string
def handle(data):
    data = base64.b64decode(data)
    #TODO: use bytesio instead of saving to file
    #see https://community.openai.com/t/openai-whisper-send-bytes-python-instead-of-filename/84786/4
    filename = str(uuid4()) + ".mp3"
    with open(filename, "wb") as f:
        f.write(data)
    
    #run whisper
    text = whisper_model.transcribe(filename)
    os.remove(filename)

    #respond with text
    return text


routes = {
    "": handle,
}

ProtoPost(routes).start(PORT)

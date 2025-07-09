import os
import base64
import tempfile
import subprocess
import whisper

from protopost import ProtoPost

PORT = os.getenv("PORT", 80)
MODEL = os.getenv("MODEL", "tiny.en")

whisper_model = whisper.load_model(MODEL)

#data should just be a b64 encoded string
def handle(data):
    tmp = tempfile.NamedTemporaryFile(delete=False)

    with open(tmp.name, "wb") as f:
        #save audio file
        data = base64.b64decode(data)
        f.write(data)
    
    #run whisper
    text = whisper_model.transcribe(tmp.name)
    os.remove(tmp.name)

    #respond with text
    return text


routes = {
    "": handle,
}

ProtoPost(routes).start(PORT)

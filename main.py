import os
import base64
import time
from uuid import uuid4

import whisper
from protopost import ProtoPost

PORT = os.getenv("PORT", 80)
MODEL = os.getenv("MODEL", "tiny.en")
FILE_EXT = os.getenv("FILE_EXT", "mp3")

whisper_model = whisper.load_model(MODEL)

def handle(data):
    t = time.time()
    data = base64.b64decode(data)
    decode_time = time.time() - t

    t = time.time()
    filename = f"{str(uuid4())}.{FILE_EXT}"

    with open(filename, "wb") as f:
        f.write(data)
    save_time = time.time() - t
    
    #run whisper
    t = time.time()
    text = whisper_model.transcribe(filename)
    os.remove(filename)
    whisper_time = time.time() - t

    print(
        "timings:",
        f"decode: {round(decode_time, 2)}s,",
        f"save: {round(save_time, 2)}s,",
        f"whisper: {round(whisper_time, 2)}s"
    )

    #respond with text
    return text


routes = {
    "": handle,
}

ProtoPost(routes).start(PORT)

import os
import base64
import time
from uuid import uuid4

from protopost import ProtoPost

from utils import create_pipeline

PORT = os.getenv("PORT", 8762)
MODEL = os.getenv("MODEL", "distil-whisper/distil-small.en")
FILE_EXT = os.getenv("FILE_EXT", "mp3")

pipe = create_pipeline(MODEL)

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
    text = pipe(filename)["text"]
    whisper_time = time.time() - t
    os.remove(filename)

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

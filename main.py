import os
import base64
import tempfile
import subprocess

from protopost import ProtoPost

PORT = os.getenv("PORT", 80)
MODEL = os.getenv("MODEL", "tiny.en")

#data should just be a b64 encoded string
def handle(data):
    with tempfile.TemporaryDirectory() as temp_dir:
        #switch to new wd
        old_dir = os.getcwd()
        os.chdir(temp_dir)

        #save audio file
        data = base64.b64decode(data)
        with open("audio", "wb") as f:
            f.write(data)
        
        #run whisper
        subprocess.run(["whisper", "--model", MODEL, "--output_format", "txt", "audio"])

        #load resulting file
        with open("audio.txt", "r") as f:
            text = f.read()
        
        #return to old wd
        os.chdir(old_dir)

    #respond with text
    return text


routes = {
    "": handle,
}

ProtoPost(routes).start(PORT)

import os
import base64

from protopost import protopost_client as ppcl

HOST = "http://127.0.0.1:8123"
STT = lambda x: ppcl(HOST, x)

#load file
with open("test.mp3", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

text = STT(data)

print(text)

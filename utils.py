import wave

def save_audio_file(pcm_data, filename):
  with wave.open(filename, "wb") as wavfile:
    channles = 1
    sample_width = 2
    wavfile.setnchannels(1)
    wavfile.setsampwidth(2)
    wavfile.setframerate(48000)
    wavfile.writeframes(pcm_data)
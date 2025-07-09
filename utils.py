import wave

def save_audio_file(pcm_data, filename):
  with wave.open(filename, "wb") as wavfile:
    channles = 2
    sample_width = 2
    sample_rate = 48000
    wavfile.setnchannels(channles)
    wavfile.setsampwidth(sample_width)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcm_data)
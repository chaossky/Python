import librosa
import librosa.display
import matplotlib.pyplot as plt

audio,sr=librosa.load("audio.mp3")

plt.figure(figsize=(10,4))
librosa.display.waveshow(audio,sr=sr)
plt.title("Audio Waveform")
plt.savefig("audio_waveform.png")
plt.show()

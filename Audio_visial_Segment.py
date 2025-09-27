from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

# MP3 파일 로드
audio = AudioSegment.from_mp3("helpless.mp3")
samples = np.array(audio.get_array_of_samples())

# 채널 분리 (모노/스테레오)
if audio.channels == 2:
    samples = samples.reshape((-1, 2))
    samples = samples.mean(axis=1)  # 스테레오 → 모노

# 시각화
plt.figure(figsize=(12, 4))
plt.plot(samples)
plt.title("Waveform of MP3")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.show()

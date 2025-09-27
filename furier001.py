import numpy as np
import matplotlib.pyplot as plt

# Sampling settings
Fs = 1000  # Sampling frequency (Hz)
T = 1 / Fs  # Sampling interval
t = np.arange(0, 1, T)  # Time vector for 1 second

# Signal: combination of 50Hz and 120Hz sine waves
f1 = 50
f2 = 120
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Fourier Transform
fft_result = np.fft.fft(signal)
N = len(fft_result)
freq = np.fft.fftfreq(N, T)

# Magnitude spectrum
magnitude = np.abs(fft_result) / N

# Plotting
plt.figure(figsize=(12, 6))

# Original signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

# Frequency spectrum
plt.subplot(2, 1, 2)
plt.stem(freq[:N // 2], magnitude[:N // 2])  # Removed use_line_collection for compatibility
plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
import numpy as np
# from matplotlib import pyplot as plt

SAMPLE_RATE = 44100
DURATION = 5


def generate_sine_wave(freq, sample_rate, duration):
    X = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = X * freq
    # 2pi because np.sin takes in radians
    Y = np.sin((2 * np.pi) * frequencies)
    return X, Y


# Generate 2 sine waves each at a given frequency
_, nice_tone = generate_sine_wave(432, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

# Mix waves together then normalize them for audio processing
mixed_tone = noise_tone + nice_tone
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

# Uncomment this if you would like to see the audio in the time domain
# plt.plot(normalized_tone[:1000])
# plt.show()

# Uncomment this if you would like to save the audio file locally
from scipy.io.wavfile import write
#
# write("my_distorted_sine_wave.wav", SAMPLE_RATE, normalized_tone)


# REMOVING THE 4000Hz noise from the 400Hz sine wave using FFT:
from scipy.fft import rfft, rfftfreq  # <-- these methods do not calculate the negative half of the frequency

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

# Transforming audio file into the frequency domain
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

# Uncomment this if you would like to see the audio file in the frequency domain
# plt.plot(xf, np.abs(yf))
# plt.show()

# Removing the 4000Hz tone
points_per_freq = len(xf) / (SAMPLE_RATE / 2)
target_idx = int(points_per_freq * 4000)
yf[target_idx - 1: target_idx + 2] = 0

# Uncomment this if you would like to see the 4000Hz being removed from the frequency domain
# plt.plot(xf, np.abs(yf))
# plt.show()


# The Inverse FFT to get back into the time domain
from scipy.fft import irfft

new_sig = irfft(yf)

# Uncomment this if you would like to see the new signal without the 4000Hz frequency
# plt.plot(new_sig[:1000])
# plt.show()

# Normalizing the signal into an audio file and saving it locally
norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
write("clean.wav", SAMPLE_RATE, norm_new_sig)

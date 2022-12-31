import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import basic_units as bs


# Creating waves
frequency1 = 50
frequency2 = 800
frequency_angular1 = 2*np.pi*frequency1
frequency_angular2 = 2*np.pi*frequency2
time = np.linspace(0, 2, 10**6)
rate = time[1]-time[0]
y1 = np.sin(time*frequency_angular1)
y2 = np.sin(time*frequency_angular2)
g = y1 + y2

# fft on g wave
fft = np.fft.fft(g)
fr_spectrum = np.fft.fftfreq(len(fft), rate)
fr_spectrum_abs = fr_spectrum > 0

# Plots
plt.figure(figsize=(8, 4), layout='constrained')

plt.subplot(211)
plt.plot(time, y1, label='$y1= sine(2\pi 50t)$')
plt.plot(time, y2, label='$y2 = sine(2\pi 800t)$')
plt.plot(time, g, label='$g = y1 + y2$')
plt.xlim([0,0.1])
plt.legend(loc='best')
plt.hlines(0, -0.10, 2, colors='black', linestyle='--')
plt.title('Sine wave')
plt.xlabel('$time(s)$')
plt.ylabel('$Magnitude$')
plt.subplot(212)
plt.plot(fr_spectrum[fr_spectrum_abs], fft[fr_spectrum_abs], label='fft')
plt.title('FFT of sine wave g')
plt.xlabel('$Frequency (\omega)$')
plt.legend(loc='best')
plt.xlim(-0.02, 840)
plt.show()

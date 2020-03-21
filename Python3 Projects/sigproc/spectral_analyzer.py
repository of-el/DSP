import cmath
import math
import numpy
import matplotlib.pyplot as plot


def analyze(data, bins, sampling_rate):

    bins = bins + 1
    samples = len(data)

    out = [0.0] * bins
    real = [0.0] * bins
    imaginary = [0.0] * bins

    print("Applying DFT for spectral analysis")
    for m in range(bins):
        for n in range(samples):
            #out[m] = out[m] + (pow((data[n] * _real(n, m, bins)), 2) - pow((data[n] * _imaginary(n, m, bins)), 2))
            real[m] = real[m] + (data[n] * _real(n, m, bins))
            imaginary[m] = imaginary[m] - (data[n] * _imaginary(n, m, bins))
        # Magnitude
        out[m] = cmath.sqrt(pow(real[m], 2) + pow(imaginary[m], 2))
        # Power (power = magnitude squared)
        #out[m] = pow(real[m], 2) + pow(imaginary[m], 2)

    _plot_spectrum(out, bins, sampling_rate)


def _real(n, m, bins):
    
    return math.cos((2 * math.pi * n * m) / bins)


def _imaginary(n, m, bins):

    return math.sin((2 * math.pi * n * m) / bins)


def _plot_spectrum(data, bins, sampling_rate):

    plot.plot(numpy.arange(0, bins) * (sampling_rate / (bins-1)), data, marker='o')
    plot.show(block=True)

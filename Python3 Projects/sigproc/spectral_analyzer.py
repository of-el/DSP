import cmath
import math
import numpy
import matplotlib.pyplot as plot


def analyze(data, bins, sampling_rate):

    bins = bins + 1
    out = [0.0] * bins
    samples = len(data)

    print("Applying DFT for spectral analysis")
    for m in range(bins):
        for n in range(samples):
            out[m] = out[m] + (pow((data[n] * _real(n, m, bins)), 2) - pow((data[n] * _imaginary(n, m, bins)), 2))
    
    _plot_spectrum(out, bins, sampling_rate)


def _real(n, m, bins):
    
    return math.cos((2 * math.pi * n * m) / bins)


def _imaginary(n, m, bins):

    return math.sin((2 * math.pi * n * m) / bins)


def _plot_spectrum(data, bins, sampling_rate):

    plot.plot(numpy.arange(0, bins) * (sampling_rate / (bins-1)), data, marker='o')
    plot.show(block=True)

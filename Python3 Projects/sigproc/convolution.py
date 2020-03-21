import numpy
from scipy import signal
from random import randint
import matplotlib.pyplot as plot


def convolve(input, impulse, sampling_rate, **kwargs):

    plot_data = kwargs.get('plot', False)

    print("Beginning convolution process...")
    output_length = len(input) + len(impulse) + 1
    output = [0.0] * output_length

    for i in range(len(input)):
        for j in range(len(impulse)):
            output[i + j] = output[i + j] + (input[i] * impulse[j])

    if plot_data:
        print("Plotting input signal convolved with impulse response...")
        plot.ylim(-1, 1)
        plot.plot(numpy.arange(0, output_length) / sampling_rate, output, marker='o')
        plot.show()


def generate_impulse(sample_length):

    print("Generating random impulse response...")
    rand_idx = randint(0, sample_length - 1)
    impulse = signal.unit_impulse(sample_length, rand_idx)

    return impulse
import numpy
import matplotlib.pyplot as plot
import sys
import math
import scipy.io.wavfile


waveform = "sin"
harmonics = 1
frequency = 1000
phase_shift = 0
sampling_rate = 44100
duration = 10
period = 1 / frequency
samples = (duration * sampling_rate) + 1
phase = sampling_rate * period
xn = [None] * int(samples)

def init(waveform_, frequency_, phase_shift_, sampling_rate_, duration_, harmonics_=1):

    global waveform
    global harmonics
    global frequency
    global phase_shift
    global sampling_rate
    global duration
    global period
    global samples
    global phase
    global xn

    waveform = waveform_
    harmonics = harmonics_
    frequency = frequency_
    phase_shift = phase_shift_ / 360
    sampling_rate = sampling_rate_
    duration = duration_
    period = 1 / frequency
    samples = (duration * sampling_rate) + 1
    phase = sampling_rate * period # how many samples per period
    xn = [None] * int(samples)

def sine_wave(i, harmonic):

    val = (1 / harmonic) * math.sin(harmonic * 2 * math.pi * ((i - (sampling_rate * phase_shift)) / phase))
    return val

def generate_waveform():

    print("Num of samples : {}".format(samples))
    # Zero out all indices
    for i in range(0, int(samples)):
        xn[i] = 0.0

    # Check what waveform to generate
    if waveform == "sin":
        for i in range(0, int(samples)):
            xn[i] = SineWave(i, harmonics)
            print(xn[i])
    elif waveform == "square":
        for i in range(0, int(samples)):
#            self.xn[i] = math.sin((2 * math.pi * (i / self.phase))) + ((1/3)*math.sin((3 * 2 * math.pi * (i / self.phase))))
            for j in range(harmonics + 1):
                xn[i] = xn[i] + SineWave(i, (2 * j) + 1)
#    elif self.waveform == "saw":
#        self.xn[i] =
#    elif self.waveform == "triangle":
#        self.xn[i] =
#    else:
#        sys.exit("Invalid waveform!")

    plot.ylim(-1, 1)
    plot.plot(numpy.arange(0, samples) / sampling_rate, xn, marker='o')
    plot.show(block=True)

def WriteToWav(file):

    data = numpy.asarray(xn)
    scipy.io.wavfile.write(file, sampling_rate, data)
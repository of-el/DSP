import numpy
import matplotlib.pyplot as plot
import pandas
import sys
import math
import scipy.io.wavfile


class Oscillator:

    def __init__(self, waveform, frequency, phase_shift, sampling_rate, duration, harmonics=1):

        self.waveform = waveform
        self.harmonics = harmonics
        self.frequency = frequency
        self.phase_shift = phase_shift
        self.sampling_rate = sampling_rate
        self.duration = duration
        self.period = 1 / frequency
        self.samples = (duration * sampling_rate) + 1
        self.phase = sampling_rate * self.period
        self.xn = [None] * int(self.samples)

    def SineWave(self, i, harmonic):

        val = (1 / harmonic) * math.sin((harmonic * 2 * math.pi * (i / self.phase)) + self.phase_shift)
        return val

    def GenerateWaveform(self):

        print("Num of samples : {}".format(self.samples))
        # Zero out all indices
        for i in range(0, int(self.samples)):
            self.xn[i] = 0.0

        # Check what waveform to generate
        if self.waveform == "sin":
            for i in range(0, int(self.samples)):
                self.xn[i] = self.SineWave(i, self.harmonics)
                print(self.xn[i])
        elif self.waveform == "square":
            for i in range(0, int(self.samples)):
#                self.xn[i] = math.sin((2 * math.pi * (i / self.phase))) + ((1/3)*math.sin((3 * 2 * math.pi * (i / self.phase))))
                for j in range(self.harmonics + 1):
                    self.xn[i] = self.xn[i] + self.SineWave(i, (2 * j) + 1)
#        elif self.waveform == "saw":
#                self.xn[i] =
#        elif self.waveform == "triangle":
#                self.xn[i] =
#        else:
#                sys.exit("Invalid waveform!")

        plot.ylim(-1, 1)
        plot.plot(numpy.arange(0, self.samples) / self.sampling_rate, self.xn, marker='o')
        plot.show(block=False)

    def WriteToWav(self, file):

        data = numpy.asarray(self.xn)
        scipy.io.wavfile.write(file, self.sampling_rate, data)


def main():

    osc = Oscillator(waveform="sin", frequency=2, phase_shift=0, sampling_rate=32, duration=1, harmonics=1)
    print("Generating waveform")
    osc.GenerateWaveform()
    print("Writing waveform to file")
    osc.WriteToWav("{}_{}Hz_{}s_{}harmonics.wav".format(osc.waveform, osc.frequency, osc.duration, osc.harmonics))
    plot.show()


if __name__ == '__main__':
    main()
import numpy
import matplotlib.pyplot as plot
import sys
import math
import scipy.io.wavfile
import csv


_waveform = "sine"
_amplitude = 1
_harmonics = 1
_frequency = 1000
_phase_shift = 0
_sampling_rate = 44100
_duration = 10
_period = 1 / _frequency
_samples = (_duration * _sampling_rate) + 1
_phase = _sampling_rate * _period
_xn = [None] * int(_samples)


def init(waveform, frequency, phase_shift, sampling_rate, duration, amplitude=1, harmonics=1):

    global _waveform
    global _amplitude
    global _harmonics
    global _frequency
    global _phase_shift
    global _sampling_rate
    global _duration
    global _period
    global _samples
    global _phase
    global _xn

    _waveform = waveform
    _amplitude = amplitude
    _harmonics = harmonics
    _frequency = frequency
    _phase_shift = phase_shift / 360
    _sampling_rate = sampling_rate
    _duration = duration
    _period = 1 / _frequency
    _samples = (_duration * _sampling_rate) + 1
    _phase = _sampling_rate * _period # how many samples per period
    _xn = [None] * int(_samples)


def _sine_wave(i, harmonic):

    val = _amplitude * (1 / harmonic) * math.sin(harmonic * 2 * math.pi * ((i - (_sampling_rate * _phase_shift)) / _phase))
    return val


def generate_waveform(**kwargs):

    return_data = kwargs.get('ret', False)
    plot_data = kwargs.get('plot', False)

    print("Generating {} waveform...".format(_waveform))
    # Zero out all indices
    for i in range(0, int(_samples)):
        _xn[i] = 0.0

    # Check what waveform to generate
    if _waveform == "sine":
        for i in range(0, int(_samples)):
            _xn[i] = _sine_wave(i, _harmonics)
    elif _waveform == "square":
        for i in range(0, int(_samples)):
            for j in range(_harmonics + 1):
                _xn[i] = _xn[i] + _sine_wave(i, (2 * j) + 1)
#    elif self.waveform == "saw":
#        self.xn[i] =
#    elif self.waveform == "triangle":
#        self.xn[i] =
#    else:
#        sys.exit("Invalid waveform!")

    if plot_data:
        print("Plotting waveform...")
        plot.ylim(-1, 1)
        plot.plot(numpy.arange(0, _samples) / _sampling_rate, _xn, marker='o')
        plot.show(block=True)

    if return_data:
        return _xn


def write_to_wav(wav_file, **kwargs):

    read_in_data = kwargs.get('rid', None)

    if read_in_data is not None:
        data = numpy.asarray(_read_in_csv(read_in_data))
    else:
        data = numpy.asarray(_xn)
    
    print(type(data))
    print(data)

    print("Writing data to WAV file : {}".format(wav_file))
    scipy.io.wavfile.write(wav_file, _sampling_rate, data)


def write_to_csv(csv_file):

    print("Writing data to CSV file : {}".format(csv_file))
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['time', 'amplitude'])
        for index, value in enumerate(_xn):
            writer.writerow([index/_sampling_rate, value])


def _read_in_csv(csv_file):
    
    data = []

    print("Reading data from CSV file : {}".format(csv_file))
    with open(csv_file, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            data.append(float(row[1]))

    return data

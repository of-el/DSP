import spectral_analyzer as spec
import oscillator_trashy as osc
import convolution as conv


def main():

    sr = 16000
    osc.init(waveform="sine", amplitude=1, frequency=1000, phase_shift=0, sampling_rate=sr,
             duration=10, harmonics=1)
    data = osc.generate_waveform(ret=True, plot=True)
    osc.write_to_wav("Sine.wav")
    #impulse = conv.generate_impulse(sample_length=20)
    #print(impulse)
    #conv.convolve(data, impulse, sr, plot=True)
    spec.analyze(data, bins=64, sampling_rate=sr)


if __name__ == "__main__":
    main()

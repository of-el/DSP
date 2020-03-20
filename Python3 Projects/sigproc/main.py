from oscillator import Oscillator as Osc
from filter import LowPass as lpf
import spectral_analyzer as spec
import oscillator_noclass as osc


def main():
    osc.init(waveform="sine", frequency=4, phase_shift=0, sampling_rate=64, 
             duration=1, harmonics=1)
    data = osc.generate_waveform(ret=True)
    spec.analyze(data, bins=64, sampling_rate=64)


if __name__ == "__main__":
    main()

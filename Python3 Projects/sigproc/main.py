from oscillator import Oscillator as Osc
from filter import LowPass as lpf
import spectral_analyzer as spec
import oscillator_noclass as osc


def main():
#    osc.init(waveform_="sin", frequency_=7, phase_shift_=0, sampling_rate_=6, duration_=1, harmonics_=1)
    print(osc.sampling_rate)
    print("Generating waveform")
    osc.generate_waveform()


if __name__ == "__main__":
    main()
from oscillator import Oscillator as Osc
from filter import LowPass as lpf
import spectral_analyzer as spec
import oscillator_noclass as osc


def main():
    osc.init(waveform="sine", frequency=500, phase_shift=0, sampling_rate=2000, 
             duration=1, harmonics=1)
    osc.generate_waveform()
    osc.write_to_csv("SineWav.csv")
    osc.write_to_wav("Sine_Wav.wav", rid="SineWav.csv")
    #print("Applying DFT for spectral analysis")
    #spec.analyze(data, bins=16)


if __name__ == "__main__":
    main()

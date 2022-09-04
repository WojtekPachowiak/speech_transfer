import sounddevice as sd
import soundfile as sf

filename = 'output.wav'

data,fs = sf.read(filename, dtype='float32')
sd.play(data,fs)
status = sd.wait()

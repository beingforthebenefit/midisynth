# Let's play some tones!

import pyaudio
import numpy

p = pyaudio.PyAudio()

volume = 0.5
fs = 44100
duration = 1.0
f = 440.0

samples = (numpy.sin(2*numpy.pi*numpy.arange(fs*duration)*f/fs)).astype(numpy.float32)

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()
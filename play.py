# Let's play some tones!

import pyaudio
import numpy

def noteToFrequency(note):
        return 27.5 * ((2.0 ** (1.0/12.0)) ** float(note-1))

def playNote(note, duration):
    p = pyaudio.PyAudio()
    volume = 0.5
    sampleRate = 44100
    frequency = noteToFrequency(note)
    print(frequency)
    samples = (numpy.sin(2*numpy.pi*numpy.arange(sampleRate*duration)*frequency/sampleRate)).astype(numpy.float32)
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sampleRate,
                    output=True)
    stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()

playNote(56, 1)
playNote(55, 1)
playNote(56, 1)
playNote(55, 1)
playNote(56, 1)
playNote(51, 1)
playNote(54, 1)
playNote(52, 1)
playNote(49, 3)
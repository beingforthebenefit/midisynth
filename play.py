# Let's play some tones!

import pyaudio
import numpy

def noteToFrequency(note):
        return 27.5 * ((2.0 ** (1.0/12.0)) ** float(note-1))

def playNotes(notes):
    p = pyaudio.PyAudio()
    volume = 0.5
    sampleRate = 44100

    for note in notes:
        frequency = noteToFrequency(note[0])
        print(frequency)
        samples = (numpy.sin(2*numpy.pi*numpy.arange(sampleRate*note[1])*frequency/sampleRate)).astype(numpy.float32)
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=sampleRate,
                        output=True)
        stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()

notes = [
    [56, 1],
    [55, 1],
    [56, 1],
    [55, 1],
    [56, 1],
    [51, 1],
    [54, 1],
    [52, 1],
    [49, 3]
]

playNotes(notes)
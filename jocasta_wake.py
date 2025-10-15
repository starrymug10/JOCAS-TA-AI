import time
import pvporcupine
import pyaudio
from jocasta_voice import speak

class WakeListener:
    def __init__(self, keyword="jocasta"):
        self.porcupine = pvporcupine.create(keywords=[keyword])
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def listen(self):
        while True:
            pcm = self.stream.read(self.porcupine.frame_length, exception_on_overflow=False)
            pcm = [int.from_bytes(pcm[i:i+2], "little", signed=True) for i in range(0, len(pcm), 2)]
            keyword_index = self.porcupine.process(pcm)
            if keyword_index >= 0:
                speak("Ya?", realistic=True)
                return
            time.sleep(0.1)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.porcupine.delete()

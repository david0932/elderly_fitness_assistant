import pyttsx3
import threading

class Speaker:
    def __init__(self, rate=180, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.last_warn_time = 0
        self.last_good_time = 0

    def say(self, text):
        threading.Thread(target=self._speak, args=(text,), daemon=True).start()

    def _speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

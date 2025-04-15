import pygame
import threading

class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.lock = threading.Lock()

    def play_wav(self, wav_file):
        threading.Thread(target=self._play, args=(wav_file,), daemon=True).start()

    def _play(self, wav_file):
        with self.lock:
            try:
                sound = pygame.mixer.Sound(wav_file)
                sound.play()
                pygame.time.wait(int(sound.get_length() * 1000))
            except Exception as e:
                print(f"Error playing audio file {wav_file}: {e}")
import pygame
import threading
import time

pygame.mixer.init()

def play_music():
    try:
        pygame.mixer.music.load("start.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print(f"Error playing music: {e}")
    finally:
        pygame.mixer.quit()  # 確保釋放音訊設備

music_thread = threading.Thread(target=play_music, daemon=True)
music_thread.start()

time.sleep(5)  # 等待播放完成
pygame.mixer.quit()  # 程式結束時關閉

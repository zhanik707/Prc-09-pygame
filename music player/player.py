import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base = os.path.dirname(__file__)

        self.tracks = [
            os.path.join(base, "music/track1.wav"),
            os.path.join(base, "music/track2.wav")
        ]

        self.index = 0

    def play(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.tracks[self.index])
            pygame.mixer.music.play()
            print("Playing:", self.tracks[self.index])
        except Exception as e:
            print("ERROR:", e)

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def get_current_track(self):
        return os.path.basename(self.tracks[self.index])
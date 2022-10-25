import os
import pygame
import time
import random

audio_folder = '/home/dperez48/Documents/Projects/Bluecon/Audios'


audio_list = os.listdir(audio_folder)

random_audio = random.choice(audio_list)

pygame.mixer.init()

pygame.mixer.music.load(os.path.join(audio_folder,random_audio))
pygame.mixer.music.play()
time.sleep(30)
pygame.mixer.stop()



print('script ran correctly')

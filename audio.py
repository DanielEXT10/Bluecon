import os
import pygame
import time
import random


#os.environ['SDL_AUDIODRIVER'] ='dsp'
user = os.getlogin()
#current_folder = os.getcwd()

audio_folder =  '/home/'+ user +'/Documents/Bluecon/audio/HSE'


print('Reproducing audio from: ' + audio_folder)


audio_list = os.listdir(audio_folder)

random_audio = random.choice(audio_list)

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(os.path.join(audio_folder,random_audio))
pygame.mixer.music.play()
time.sleep(30)
pygame.mixer.stop()



print('script ran correctly')

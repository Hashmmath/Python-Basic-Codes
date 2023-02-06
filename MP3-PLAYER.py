'''Note that you will need to install the pygame library 
first using the following command: pip install pygame
Also, make sure to replace the "song.mp3" with the path 
to your MP3 music file.'''

import pygame

pygame.init()

pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()

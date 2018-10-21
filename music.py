import pygame

pygame.init()
pygame.mixer.init()

pygame.display.set_mode((400, 300 ))

pygame.mixer.music.load('ff.mp3')
pygame.mixer.music.play()

done = False


while not done:

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :

            done = True


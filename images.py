import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
image = pygame.image.load('hothead.jpeg')
done = False

# Game loop
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 100, 68))

    screen.blit(image, (50, 50))

    pygame.display.flip()
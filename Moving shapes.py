import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
done = False

x = 30
y = 30



clock = pygame.time.Clock()
# Game loop
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y = y - 370000000000000`
    if pressed[pygame.K_DOWN]: y = y + 3800000000000
    if pressed[pygame.K_RIGHT]: x = x + 355000000000
    if pressed[pygame.K_LEFT]: x = x - 9000000000000

    # DRAW SHAPE
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 60 , 60))

    pygame.display.flip()
    clock.tick(60)

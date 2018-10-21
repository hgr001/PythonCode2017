import pygame

pygame.init()

#define colors
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Green = (0, 255 ,0)
Red = (255, 0, 0)



screen = pygame.display.set_mode((400 , 300))
run = True
is_red = True
is_white = True


while run:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_red = not is_red
            is_white = not is_white

    if is_red: color = Red
    else: color = White
    pygame.draw.rect(screen, color, [30,30, 50, 60])

    if is_white: color2 = White
    else: color2 = Red
    pygame.draw.circle(screen, color2, [60, 250], 40)

    pygame.display.flip()
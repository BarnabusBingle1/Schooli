import pygame

pygame.init()

WINDOW_SIZE = 600
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Basic Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill((255,255,255))
    pygame.draw.rect(display, (0,0,0), (250,250, 20,20))
    pygame.display.flip()
pygame.quit()
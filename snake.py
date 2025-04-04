import pygame

pygame.init()

WINDOW_SIZE = 600

display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Moving Rectangle")

rect_x = 250
rect_y = 250

running = True
while running:
    for event in pygame.event.get()
    if event.type == pygame.QUIT:
        running = False 

    rect_x += 2
    rect_y += 2

    display.fill((255,255,255))
    pygame.draw.rect(display(0,0,0). (rect_x, rect_y, 20,20))
    pygame.display.flip()
    pygame.time.Clock(). tick(60)
pygame.quit()
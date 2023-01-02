#Python 3.4.3 with Pygame
import pygame

pygame.init()
pygame.display.set_caption('Crash!')
window = pygame.display.set_mode((300, 300))


CIRCLE = pygame.draw.ellipse(screen, RED, [100,50, 200, 200], 4)
pygame.display.update()
# Main Loop
while True:

    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    
    if CIRCLE.collidepoint(pos) and pressed1:
        print("You have opened a chest!")

      for event in pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(1)
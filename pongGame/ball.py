#screeeeeeeee importing agaaaaaaaaiiiiiinnnnnnnnn
import pygame
from random import randint
#back color
BLACK = (0,0,0)
# a class for the baaaaaal 
class Ball(pygame.sprite.Sprite):
  
    def __init__(self, color, width, height):
        #constructor
        super().__init__()
      
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball :P
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        #math :P
        self.velocity = [randint(4,8),randint(-8,8)]
        
        self.rect = self.image.get_rect()
  #updating ball movement 
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
#detecting collision
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
#immmmmmppppppporrrrrrrrrtttttiiiinnnngggggg
import pygame
BLACK = (0,0,0)
#paddle clsas :P
class Paddle(pygame.sprite.Sprite):
 
#definin object    
    def __init__(self, color, width, height):
        # Constructor
        super().__init__()
        
      
        # Set the background color 
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle :P
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
      
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
		
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
	
        if self.rect.y > 400:
          self.rect.y = 400

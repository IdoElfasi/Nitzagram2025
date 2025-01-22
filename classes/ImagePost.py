import pygame
from constants import *
from helpers import *
from Post import *

class ImagePost(Post):
    def __init__(self, path, username,location,description):
        super().__init__(username,location,description)
        self.path = path
        
    
    def display(self):
        path = self.path
        super().display()
        image = pygame.image.load(path)
        image = pygame.transform.scale(image,(POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))
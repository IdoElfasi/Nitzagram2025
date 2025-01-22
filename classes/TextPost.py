
import pygame

from constants import *
from helpers import *
from classes.Post import *





class TextPost(Post):
    def __init__(self,text,text_color,background_color,username,location,description):
        #post init
        super().__init__(username,location,description)
        #TextPost init
        self.text=text
        self.text_color=text_color
        self.background_color=background_color

    #creating a background
    def create_background(self):
           pygame.draw.rect(screen,self.background_color,pygame.Rect((POST_X_POS,POST_Y_POS),(POST_WIDTH,POST_HEIGHT)))


#placing text on the middle of the background
    def place_text(self):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)
        text=font.render(self.text,True,self.text_color)
        middle=center_text(1,text,1)
        screen.blit(text,middle)



    def display(self):
        super().display()
        self.create_background()
        self.place_text()


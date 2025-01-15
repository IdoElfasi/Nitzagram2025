import pygame
from constants import *
from helpers import screen,from_text_to_array,draw_comment_text_box

class Comment:
    def __init__(self,text):
        self.text=text

    def display(self,i):
        font = pygame.font.SysFont("Tahoma", 23)
        text = font.render(self.text, True, BLACK)
        screen.blits(text, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS+(COMMENT_LINE_HEIGHT*i)))



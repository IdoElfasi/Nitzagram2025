import pygame

from constants import *
from helpers import screen





class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,username,location,description): #TODO: add parameters
        self.username = username
        self.location = location
        self.description = description
        self.comments = list()
        self.likes_counter = 0

        
    def display_likes(self):
        font=pygame.font.SysFont("chalkduster.ttf",UI_FONT_SIZE)
        text=font.render(f"Likes by  :{self.likes_counter}",True,BLACK)
        screen.blit(text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

    def display_location(self):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)
        text = font.render(self.location, True, BLACK)
        screen.blit(text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

    def display_description(self):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)
        text = font.render(self.description ,True, BLACK)
        screen.blit(text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))




    def display_username(self):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)
        text = font.render(self.username, True, BLACK)
        screen.blit(text, (USER_NAME_X_POS, USER_NAME_Y_POS))

    def display(self):
        self.display_likes()
        self.display_location()
        self.display_username()
        self.display_likes()
        self.display_description()
        self.display_comments()


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = len(self.comments)
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_likes(self):
        self.likes_counter += 1

    def add_comment(self,text):
        self.comments.append(text)




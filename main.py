import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.ImagePost import ImagePost
from classes.TextPost import *
from buttons import *

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    image = ImagePost("Images/noa_kirel.jpg", "nitay", "kfar kasem", "#freebeersheva")
    image2 = ImagePost("Images/ronaldo.jpg", "blok", "kfar kasem", "#freebeersheva")
    textpost = TextPost("hello", BLACK, LIGHT_GRAY, "hello", "israel", "je;;op")
    postlist = [image, image2, textpost]
    currentPostIndex = 0
    running = True
    
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if mouse_in_button(click_post_button, pos):
                    currentPostIndex = (currentPostIndex + 1) % len(postlist)

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        postlist[currentPostIndex].display()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()

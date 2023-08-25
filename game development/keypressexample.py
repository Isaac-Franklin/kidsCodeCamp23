# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop or Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Was the close button pressed? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
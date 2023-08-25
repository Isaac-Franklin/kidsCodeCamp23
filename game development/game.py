# Import the pygame module
import random

import pygame

import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        time_sec -= 1

    return False

# countdown(5)

# Setup for sounds. Defaults are good.
pygame.mixer.init()

pygame.mixer.music.load("Without.mp3")
pygame.mixer.music.play(loops=-1)

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

move_up_sound = pygame.mixer.Sound('soundOne.mp3')
move_down_sound = pygame.mixer.Sound('soundTwo.mp3')
end_sound = pygame.mixer.Sound('soundThree.mp3')

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.Surface((75, 25))
        self.surf = pygame.image.load('player.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            move_up_sound.play()
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            move_down_sound.play()
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # self.surf = pygame.Surface((25, 100))
        self.surf = pygame.image.load('enemy.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(-10, 5)


    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load('pycloud.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

        self.speed = random.randint(0, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()



# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()
# Instantiate enemy. Right now, this is just a rectangle.
# enemy = Enemy()

# Create a custom event for adding a new enemy. I do this by using the reserved pygame event called 'USEREVENT' and
# adding +1 cos I want it to be unique.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 3000)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 3000)


enemies = pygame.sprite.Group()
all_characters = pygame.sprite.Group()
all_characters.add(player)
all_clouds = pygame.sprite.Group()
# all_clouds.add(Cloud)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

if running == False:
    end_sound.play()
    endNow = player.kill()
    pygame.time.set_timer(endNow, 3000)

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                # running = False
                end_sound.play()
                endNow = player.kill()
                pygame.time.set_timer(endNow, 3000)

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            end_sound.play()
            # running = False
            end_sound.play()
            endNow = player.kill()
            pygame.time.set_timer(endNow, 3000)

        # the add enemy event. This is run when the enemy is created from the set_timer fxn
        elif ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_characters.add(new_enemy)

        elif ADDCLOUD:
            newCloud = Cloud()
            all_characters.add(newCloud)
            all_clouds.add(newCloud)

    enemies.update()
    all_clouds.update()

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))
    # screen = pygame.image.load('temple.jpg').convert()

    # Draw the player on the screen
    # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # screen.blit(player.surf, player.rect)
    # screen.blit(enemy.surf, enemy.rect)
    # Draw all sprites
    for entity in all_characters:
        screen.blit(entity.surf, entity.rect)


    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        # move_up_sound.stop()
        # move_down_sound.stop()
        pygame.mixer.music.stop()
        # pygame.mixer.quit()
        player.kill()
        end_sound.play()
        # running = countdown(0)
        running = countdown(10)


    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(100)


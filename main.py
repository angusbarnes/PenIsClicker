# Lets get this shit started
# Beginners Reference: https://www.pygame.org/docs/tut/PygameIntro.html

import sys, pygame
from pygame.locals import *

def get_centred_coords(rect, surf): # Centers an object on a surface
    x =  surf.get_width() / 2 - rect.width / 2
    y =  surf.get_height() / 2 - rect.height / 2
    rect.x = x
    rect.y = y
    return rect

pygame.init() # Init basic library
myfont = pygame.font.SysFont('Comic Sans MS', 30) # TODO: Look at up freetype module (May provide better text rendering)
clock = pygame.time.Clock()

size = width, height = 800, 450 # Screen size
speed = [2, 2]
black = 0, 0, 0 # Black colour as RGB (255, 255, 255)

screen = pygame.display.set_mode(size) # Initialises a window/screen of specified size

ball = pygame.image.load("pen.png") # Loading a game image
bg = pygame.image.load("Background.png")
rect_bg = bg.get_rect()

ballrect = ball.get_rect() # Gets dimensions of rect object (left, top, height, width)


clicked = 0
while 1: # While True


    # Event Polling
    # Loop through all the new 'events' that happened last frame
    # Key presses, frame updates, mouse movements and other inputs
    # Events can also be generated from other elements of the game
    # i.e 'EnnemyHit'
    for event in pygame.event.get():

        # One line if statement: check if any of the 'events' are a quit message,
        # if so, quit the game (pygame.QUIT is just some hard coded integer, likely -1)
        if event.type == pygame.QUIT: sys.exit() # I THINK THIS LINE IS REALLY IMPORTANT TO NOT FUCK SHIT UP

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('A Pressed')
                
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.Rect.collidepoint(ballrect, event.pos):
                    clicked += 1
                    print("Clicked on rect")

    textsurface = myfont.render(str(clicked), False, (255, 0, 0))
    txt_fps = myfont.render(str(clock.get_fps()), False, (0, 255, 0))

    clock.tick(30)
    
    screen.fill(black) # Fill a Surface with solid colour
    screen.blit(bg, rect_bg)
    screen.blit(textsurface,(400,0))
    screen.blit(ball, get_centred_coords(ballrect, screen))
    screen.blit(txt_fps, (0,0))
    pygame.display.flip() # Update full display to the screen
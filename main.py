# Lets get this shit started
# Beginners Reference: https://www.pygame.org/docs/tut/PygameIntro.html

import sys, pygame


pygame.init() # Init basic library

size = width, height = 1600, 900 # Screen size
speed = [2, 2]
black = 0, 0, 0 # Black colour as RGB (255, 255, 255)

screen = pygame.display.set_mode(size) # !! Something to do with display config

ball = pygame.image.load("HCH LOGO_1.png") # Loading a game image

ballrect = ball.get_rect() # Gets dimensions of rect object (left, top, height, width)

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

    # Some hinky dinky movement shit
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # !! What are these mysterious elements. Hmmm
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
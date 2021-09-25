import sys, pygame
from pygame.locals import *
from pygame.time import *
import colors
from gameplay_functions import *
from helper_functions import *


# Init nonsense
FPS_MAX = 60
FONT_MAIN = 'Comic Sans MS' # Can be the name of any system font

pygame.init()
fnt_comic_sans_30 = pygame.font.SysFont(FONT_MAIN, 30)
clock = pygame.time.Clock()
pygame.display.set_caption('PenIsClicker')
img_balls = pygame.image.load('images/balls.png')
pygame.display.set_icon(img_balls)

# Set up screen
screen_size = width, height = 800, 450
screen = pygame.display.set_mode(screen_size)

# Initialise images and their rects
img_pen = pygame.image.load("images/pen.png")
rect_pen = img_pen.get_rect() # Gets dimensions of rect object (left, top, height, width)
img_pen_clicked = pygame.image.load("images/pen_clicked.png")
rect_pen_clicked = img_pen_clicked.get_rect()

img_bg = pygame.image.load("images/Background.png")
rect_bg = img_bg.get_rect()

img_title = pygame.image.load("images/title_screen.png")
rect_title = img_title.get_rect()
while clock.get_time() < 2:
    screen.blit(img_title, [0,0])

clicks = get_clicks() # Click counter
clicked = False # Pen is clicked or not
fps = 0
running = True
while running:

    fps = round(clock.get_fps(), 2)

    for event in pygame.event.get():

        if event.type == pygame.QUIT: running = False # I THINK THIS LINE IS REALLY IMPORTANT TO NOT FUCK SHIT UP

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clicks += 1 * multiplier(clicks)
                clicked = click_pen(clicked)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.Rect.collidepoint(rect_pen, event.pos):
                    clicks += 1 * multiplier(clicks)
                    clicked = click_pen(clicked)
                    print("Clicked the pen")

    txt_click_count = fnt_comic_sans_30.render(str(clicks), False, colors.BLUE)
    txt_fps = fnt_comic_sans_30.render("fps " + str(fps), False, colors.RED)

    clock.tick(FPS_MAX)
    
    screen.fill(colors.ERROR_PINK) # If this color shows through, something is wrong
    screen.blit(img_bg, rect_bg)

    tp_cntr = get_centred_x_coords(txt_click_count.get_rect(), screen)
    screen.blit(txt_click_count, tp_cntr)
    if clicked:
        screen.blit(img_pen_clicked, get_centred_coords(rect_pen, screen))
    else:
        screen.blit(img_pen, get_centred_coords(rect_pen, screen))
    screen.blit(txt_fps, (0,0))
    pygame.display.flip() # Update full display to the screen

save_clicks(clicks)
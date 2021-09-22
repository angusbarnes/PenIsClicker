import sys, pygame
from pygame.locals import *
import colors

def get_centred_coords(rect, surf): # Centers an object on a surface
    x =  surf.get_width() / 2 - rect.width / 2
    y =  surf.get_height() / 2 - rect.height / 2
    rect.x = x
    rect.y = y
    return rect

# Init nonsense
pygame.init()
fnt_comic_sans_30 = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
FPS_MAX = 60

# Set up screen
screen_size = width, height = 800, 450
screen = pygame.display.set_mode(screen_size)

# Initialise images and their rects
img_pen = pygame.image.load("images/pen.png")
rect_pen = img_pen.get_rect() # Gets dimensions of rect object (left, top, height, width)

img_bg = pygame.image.load("images/Background.png")
rect_bg = img_bg.get_rect()

clicked = 0
fps = 0
while True:

    fps = clock.get_fps()

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit() # I THINK THIS LINE IS REALLY IMPORTANT TO NOT FUCK SHIT UP

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('A Pressed')
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.Rect.collidepoint(rect_pen, event.pos):
                    clicked += 1
                    print("Clicked on rect")

    txt_click_count = fnt_comic_sans_30.render(str(clicked), False, colors.BLUE)
    txt_fps = fnt_comic_sans_30.render(str(fps), False, colors.RED)

    clock.tick(FPS_MAX)
    
    screen.fill(colors.ERROR_PINK) # If this color shows through, something is wrong
    screen.blit(img_bg, rect_bg)

    tp_cntr = get_centred_coords(txt_click_count.get_rect(), screen)
    tp_cntr.y = 0;
    screen.blit(txt_click_count, tp_cntr)
    screen.blit(img_pen, get_centred_coords(rect_pen, screen))
    screen.blit(txt_fps, (0,0))
    pygame.display.flip() # Update full display to the screen
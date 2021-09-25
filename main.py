import sys, pygame
from pygame.locals import *
import colors

def get_centred_x_coords(rect, surf): # Centers an object on a surface in the x-axis
    x =  surf.get_width() / 2 - rect.width / 2
    rect.x = x
    return rect

def get_centred_y_coords(rect, surf): # Centers an object on a surface in the y-axis
    y =  surf.get_height() / 2 - rect.height / 2
    rect.y = y
    return rect

def get_centred_coords(rect, surf): # Centers an object on a surface
    rect = get_centred_x_coords(rect, surf)
    rect = get_centred_y_coords(rect, surf)
    return rect

def click_pen(clicked): # Changes clicked/unclicked
    return not clicked

def multiplier(clicks):
    if clicks >= 10000:
        return 10
    elif clicks >= 5000:
        return 5
    elif clicks >= 1000:
        return 5
    elif clicks >= 420:
        return 3
    elif clicks >= 69:
        return 2
    else: return 1

def get_clicks():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        no_clicks = open("high_score.txt", "r")
        high_score = int(no_clicks.read())
        no_clicks.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
 
 
def save_clicks(new_high_score):
    try:
        # Write the file to disk
        no_clicks = open("high_score.txt", "w")
        no_clicks.write(str(new_high_score))
        no_clicks.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")

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
                clicked += 1
                
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
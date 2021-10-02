import sys, pygame
from pygame.key import start_text_input
from pygame.locals import *
from pygame.time import *
import colors
from gameplay_functions import *
from helper_functions import *
from config import DEFAULT_CONFIG_PATH, config, default_config
from scenes import *
from pygame import mixer

# Parts of the game now exist inside classes.
# The concept behing this is to think of each part of the game as a 'scene'
# There is some fancy black magic behind the scenes here to make this work.
# This class 'inherits' from the master class called 'scene'. Don't worry
# about that detail too much though
class main_scene(scene):
    #             ^^^^
    # When a class inherits from 'scene' it gains some fancy functions
    # a function called 'awake' will be called once when the scene loads
    def awake(self):
        # Init nonsense, things that only need to be done once should happen here
        # This is all code wer already had written
        # variables that need to be accessed at other points in the scene must be stored in 'self'
        
        # This is the new config API, we can use it to save and load stuff.
        # I advise against touching it right now as it is an unstable API
        self.DEFAULT_SETTINGS = config('DEFAULT_SETTINGS')
        self.settings = default_config(self.DEFAULT_SETTINGS, 'user_settings.cfg')
        self.FPS_MAX = self.settings.get("FPS_MAX")
        self.FONT_MAIN = self.settings.get("FONT_MAIN")


        self.fnt_comic_sans_30 = pygame.font.SysFont(self.FONT_MAIN, 30)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('PenIsClicker')
        self.img_balls = pygame.image.load('images/balls.png')
        pygame.display.set_icon(self.img_balls)

        # Set up screen
        self.screen_size = width, height = 800, 450
        self.screen = pygame.display.set_mode(self.screen_size)

        # Initialise images and their rects
        self.img_pen = pygame.image.load("images/pen.png")
        self.rect_pen = self.img_pen.get_rect() # Gets dimensions of rect object (left, top, height, width)
        self.img_pen_clicked = pygame.image.load("images/pen_clicked.png")
        self.rect_pen_clicked = self.img_pen_clicked.get_rect()

        self.img_bg = pygame.image.load("images/Background.png")
        self.rect_bg = self.img_bg.get_rect()

        self.img_title = pygame.image.load("images/title_screen.png")
        self.rect_title = self.img_title.get_rect()

        self.clicks = get_clicks() # Click counter

        # This is how we load 'one shot' audio samples
        # fx_ is the prefix we will use for this purpose
        self.sfx_click = mixer.Sound("audio/pen click but clickier.ogg")
        self.clicked = False

    # functions named update gets called once every frame, this is where we put the main gameplay loop.
    def update(self):
        
        # Local function (can only be accessed inside of update)
        # This is just to clean up the repeated code we had below
        def click_event():
            self.clicks += 1 * multiplier(self.clicks)
            self.clicked = not self.clicked
            self.time = update_clicks_per_second()
            self.sfx_click.play()

        fps = round(self.clock.get_fps(), 2)
        cps = 0
        self.time = 0

        # WE DO NOT NEED TO HANDLE pygame.QUIT, this gets handled outside of the scene
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    click_event()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.Rect.collidepoint(self.rect_pen, event.pos):
                        click_event()

        cps = round(get_clicks_per_second(), 1) * multiplier(self.clicks)

        txt_click_count = self.fnt_comic_sans_30.render(str(self.clicks), False, colors.BLUE)
        txt_multiplier = self.fnt_comic_sans_30.render("click multiplier: " + str(multiplier(self.clicks)), False, colors.BLUE)
        txt_fps = self.fnt_comic_sans_30.render("fps " + str(fps), False, colors.RED)
        txt_cps = self.fnt_comic_sans_30.render("Clicks per second:  " + str(cps), False, colors.BLUE)

        self.clock.tick(self.FPS_MAX)
        
        self.screen.fill(colors.ERROR_PINK) # If this color shows through, something is wrong
        self.screen.blit(self.img_bg, self.rect_bg)

        tp_cntr = get_centred_x_coords(txt_click_count.get_rect(), self.screen)
        self.screen.blit(txt_click_count, tp_cntr)
        txt_multiplier_pos = get_centred_x_coords(txt_multiplier.get_rect(), self.screen)
        txt_multiplier_pos.y += 30
        self.screen.blit(txt_multiplier, txt_multiplier_pos)

        txt_cps_pos = get_centred_x_coords(txt_cps.get_rect(), self.screen)
        txt_cps_pos.y += 60
        self.screen.blit(txt_cps, txt_cps_pos)

        if self.clicked:
            self.screen.blit(self.img_pen_clicked, get_centred_coords(self.rect_pen, self.screen))
        else:
            self.screen.blit(self.img_pen, get_centred_coords(self.rect_pen, self.screen))
        self.screen.blit(txt_fps, (0,0))
        pygame.display.flip() # Update full display to the screen

    # the function named 'end' gets called once at the end of a scene.
    # the 'scene_manager' class is responsible for managing scenes. It will tell
    # scenes when to end and call the relevant functions. See scenes.py for more info
    def end(self):
        # Doing some housekeeping and last minute clean up
        self.settings.save()
        save_clicks(self.clicks)
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

class main_scene(scene):

    def awake(self):
        # Init nonsense
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

        self.fx_click = mixer.Sound("audio/pen click but clickier.ogg")
        self.clicked = False

    def update(self):
        
        fps = 0
        cps = 0
        self.time = 0

        fps = round(self.clock.get_fps(), 2)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.clicks += 1 * multiplier(self.clicks)
                    self.clicked = not self.clicked
                    self.time = update_clicks_per_second()
                    self.fx_click.play()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.Rect.collidepoint(self.rect_pen, event.pos):
                        self.clicks += 1 * multiplier(self.clicks)
                        self.clicked = not self.clicked
                        self.time = update_clicks_per_second()
                        self.fx_click.play()

        self.cps = round(get_clicks_per_second(), 1)

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

        
    
    def end(self):
        self.settings.save()
        save_clicks(self.clicks)
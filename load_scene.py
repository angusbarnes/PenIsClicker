from scenes import *
import pygame
import colors
from main_scene import *

class loading_scene(scene):
    def awake(self):
        self.img_splash = pygame.image.load("images/title_screen.png")
        self.img_bg = pygame.image.load("images/Load Background.png")
        self.img_button_hover = pygame.image.load("images/play_hovered.png")
        self.img_button_normal = pygame.image.load("images/play_normal.png")
        self.rect_play_button = pygame.Rect(312, 203, 176, 69)
        self.rect_bg = self.img_splash.get_rect()

        self.screen_size = width, height = 800, 450
        self.screen = pygame.display.set_mode(self.screen_size)
        self.sfx_intro = pygame.mixer.Sound("audio/game intro.mp3")
        self.sfx_intro.play()

        # THIS IS HELLA SCUFFED BUT IT WORKS SO DONT TOUCH IT
        self.screen.blit(self.img_splash,(0,0))
        pygame.time.delay(100)
        for i in range (256):
            self.screen.fill(colors.BLACK)  
            self.img_splash.set_alpha(256 - i)
            self.screen.blit(self.img_splash,(0,0))
            pygame.display.flip()
            pygame.time.delay(3)

        for i in range (255):
            self.screen.fill(colors.BLACK)  
            self.img_bg.set_alpha(i)
            self.screen.blit(self.img_bg,(0,0))
            self.img_button_normal.set_alpha(i) 
            self.screen.blit(self.img_button_normal,(0,0))
            pygame.display.flip()
            pygame.time.delay(3)

    def update(self):
        self.screen.fill(colors.ERROR_PINK)
        self.screen.blit(self.img_bg,(0,0))

        hovered = pygame.Rect.collidepoint(self.rect_play_button, pygame.mouse.get_pos())
        for event in pygame.event.get():
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and hovered:
                    print("clicked dat bitch")
                    scene_manager.instance.load_scene(main_scene())
                        
        self.screen.blit(self.img_button_hover if hovered else self.img_button_normal,(0,0))
        pygame.display.flip()
from scenes import *
import pygame
import colors

class loading_scene(scene):
    def awake(self):
        self.img_bg = pygame.image.load("images/title_screen.png")
        self.rect_bg = self.img_bg.get_rect()

        self.screen_size = width, height = 800, 450
        self.screen = pygame.display.set_mode(self.screen_size)

    def update(self):
        self.screen.fill(colors.ERROR_PINK)
        self.screen.blit(self.img_bg, self.rect_bg)
        pygame.display.flip()
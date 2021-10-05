import pygame
from enum import Enum

class button():

    def __init__(self, dimesions, button_normal: pygame.image, button_hovered: pygame.image = None, button_sfx: pygame.Sound = None):
        pass

    # Handle graphics processing for each frame
    def draw(ui_update_event = None):
        if ui_update_event:
            raise NotImplemented("UI event system has not been implemented")

        pass

    def clicked() -> bool:
        pass

class ui_update_event(Enum):
    UI_DISABLE_ELEMENT = 0
    UI_ENABLE_ELEMENT = 1
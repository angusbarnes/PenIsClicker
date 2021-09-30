from main_scene import main_scene
from load_scene import loading_scene
import scenes
import pygame

pygame.init()
sm = scenes.scene_manager()
sm.load_scene(loading_scene())
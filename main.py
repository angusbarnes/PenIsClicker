from main_scene import main_scene
from load_scene import loading_scene
import scenes
import pygame

# FIRST READ COMMENTS IN 'main_scene.py' THEN READ 'scenes.py'
# THEN COME BACK HERE TO UNDERSTAND
pygame.init()

# Create a scene manager
sm = scenes.scene_manager()
# Load the first scene (The fancy thing is called a walrus operator, dont worry about it too much)
sm.load_scene(scene_load := loading_scene())

# LAST REMARKS, FULL PROGRAM CLEAN UP, OR FINAL DEBUG MESSAGES SHOULD GO HERE. THIS CODE WILL NOT BE REACHED
# UNLESS THE PROGRAM EXITS AS SCENE_MANAGER INITIATES AN INFINTE LOOP

# IF YOU WANT TO TEST THIS OR SIMPLY JUST LOAD THE MAIN_SCENE FOR TESTING PURPOSES
# CREATE A FILE NAMED 'test.py' THIS WILL BE IGNORED BY GIT
# COPY THE ABOVE CODE INSTEAD USING 'main_scene()' RATHER THAN 'loading_scene()'
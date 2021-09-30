from main_scene import main_scene
from load_scene import loading_scene
import scenes

sm = scenes.scene_manager()
sm.load_scene(loading_scene())
sm.load_scene(main_scene())
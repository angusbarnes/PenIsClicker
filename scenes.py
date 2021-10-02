
import pygame

# SCROLL DOWN TO SEE THE SCENE MANAGER CODE
# IGNORE THIS FOR THE MOMENT
class is_serialisable:

    def save() -> dict:
        raise NotImplemented("The save function has not been implemented on this object")

    def load() -> object:
        raise NotImplemented("The load function has not been implemented on this object")

# IGNORE THIS BLACK MAGIC
# TODO: Use typings to create statically typed args parser
class delegate():

    def __init__(self):
        self.funcs = []

    def __call__(self):
        for func in self.funcs:
            func()

    def subscribe(self, callback):
        self.funcs.append(callback)
    
    def unsubscribe(self, callback):
        self.funcs.remove(callback)

    def __iadd__(self, callback):
        self.subscribe(callback)
        return self
    
    def __isub__(self, callback):
        self.unsubscribe(callback)
        return self

    def __str__(self) -> str:
        return "delegate object with " + str(len(self.funcs)) + " callbacks"
    
    def __repr__(self) -> str:
        return self.__str__()

# IGNORE THIS, THIS IS JUST A TEMPLATE FOR THE SCENE CLASSES TO INHERIT FROM
class scene(is_serialisable):

    def __new__(cls, *args, **kwargs):
        scene_obj= super(scene, cls).__new__(cls)
        scene_obj.__setattr__('on_awake', delegate())
        scene_obj.__setattr__('on_update', delegate())
        scene_obj.__setattr__('on_end', delegate())
        print("created scene " +  str(scene_obj.on_update))
        return scene_obj

    def __init__(self):
        self.on_awake += self.awake
        self.on_update += self.update
        self.on_end += self.end
        print(self.on_awake)

    def awake(self):
        pass

    def update(self):
        pass

    def end(self):
        pass

    def end_scene(self):
        self.on_end()
        self._running = False

    @property
    def is_running(self):
        return self._running

    def _awake(self):
        self._running = True
        self.on_awake()

    def _update(self):
        self.on_update()

# This is interesting
class scene_manager:

    instance = None # Global variable. this can always be accessed via scene_manager.instance

    def __init__(self):

        # This is called a singleton design pattern. It means that only once
        # instance of this class can be created globally. Google it if you're
        # curious as to why this would be usefull
        if not scene_manager.instance:
            scene_manager.instance = self
        else: raise Exception("There should only be one instance of scene_manager")
        
        self.currently_playing = None

    # This function runs the whole game
    def load_scene(self, scene):
        
        # If there is a scene currently playing when we wish to load a new one
        # stop the scene by telling it to end gracefully.
        if self.currently_playing:
            self.currently_playing.end_scene()
        
        # Set the newly loaded scene to currently playing
        self.currently_playing = scene
        scene._awake() # Call the scenes internal awake function
   
        # Begin the game loop for the scene
        while scene.is_running:

            # If we receive the END_SIGNAL we should gracefully exist the scene BEFORE
            # the next update
            if pygame.event.get(pygame.QUIT):
                scene.end_scene()

            # Update the scene
            scene._update()
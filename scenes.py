
import pygame

class is_serialisable:

    def save() -> dict:
        raise NotImplemented("The save function has not been implemented on this object")

    def load() -> object:
        raise NotImplemented("The load function has not been implemented on this object")

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

class scene_manager:

    def __init__(self):
        pass

    def load_scene(self, scene):
        scene._awake()
   
        while scene.is_running:
            if pygame.event.get(pygame.QUIT):
                scene.end_scene()
            scene._update()
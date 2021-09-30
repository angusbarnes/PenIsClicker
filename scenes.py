
class is_serialisable:

    def save() -> dict:
        raise NotImplemented("The save function has not been implemented on this object")

    def load() -> object:
        raise NotImplemented("The load function has not been implemented on this object")

class delegate():

    def __init__(self):
        self.funcs = []

    def __call__(self):
        for func in self.funcs:
            func()

class scene(is_serialisable):

    def __new__(cls, *args, **kwargs):
        scene_obj= super(scene, cls).__new__(cls)
        scene_obj.__setattr__('on_awake', "hello world")
        return scene_obj

    def __init__(self, name):
        print(self.test)

    def awake():
        pass

    def update():
        pass
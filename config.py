import os
import json

global DEFAULT_CONFIG_PATH 
DEFAULT_CONFIG_PATH = './cfg/'

class config():

    """
    Initialise a new config with a unique identifier
    """
    def __init__(self, identifier):
        self.id = identifier

        self.file_path = DEFAULT_CONFIG_PATH + identifier
        self.configuration_dict = {}

        # There is room for a bug here but with simple use case it should be ok
        if os.path.exists(self.file_path) == False:
            with open(self.file_path, 'w') as FILE:
                FILE.write("{}")
        else:
            with open(self.file_path, 'r') as FILE:
                self.configuration_dict = json.load(FILE)
        

    def add(self, key, item):
        self.configuration_dict[key] = item

    def get(self, key):
        if key in self.configuration_dict:
            return self.configuration_dict[key]
        else: raise NameError("Key Not Present In Configuration")

    def has_key(self, key):
        return (key in self.configuration_dict)

    def save(self):
        try:
            with open(self.file_path, 'w') as FILE:
                FILE.write(json.dumps(self.configuration_dict, indent=4, sort_keys=True))
        except IOError:
            print("This bitch dont exist: " + self.file_path)
        finally:
            print("File Saved")

class default_config():

    def __init__(self, base_config, identifier):
        self.default = base_config
        self.internal = config(identifier)

    def add(self, key, item):
        self.internal.add(key, item)

    def get(self, key):
        if self.internal.has_key(key):
            return self.internal.get(key)
        else: 
            return self.default.get(key)

    def save(self):
        try:
            with open(self.internal.file_path, 'w') as FILE:
                FILE.write(json.dumps(self.internal.configuration_dict, indent=4, sort_keys=True))
        except IOError:
            print("This bitch dont exist: " + self.internal.file_path)
        finally:
            print("File Saved")
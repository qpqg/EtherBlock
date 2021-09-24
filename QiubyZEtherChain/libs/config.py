from os import path
from json import load

class configs(object):
    def __init__(self, file_name=None):
        super(configs, self).__init__()
        self.file_name = file_name

    def setfile_name(self, file_name):
        self.file_name = file_name

    def _load(self):
        return open(path.dirname(path.abspath(__file__)) + self.file_name)

    def getConfigs(self):
        return load(self._load())

class Configuration(configs):
    def __init__(self, **kwargs):
        super(Configuration, self).__init__(**kwargs)
        self.json_configs = {}

    def set(self, k, v):
        self.json_configs[k] = v

    def _show_configs(self):
        self.json_configs = self.getConfigs()

# conf = Configuration(file_name="/settings.json")
# print(conf.getConfigs())
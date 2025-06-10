import json

class Config:
    def __init__(self, path='appsettings.json'):
        with open(path, 'r') as f:
            self._cfg = json.load(f)

    def get(self, key, default=None):
        return self._cfg.get(key, default)

class Config:
    def __init__(self):
        self.settings = {
            "debug": True,
            "version": "1.0"
        }

    def get(self, key):
        return self.settings.get(key)

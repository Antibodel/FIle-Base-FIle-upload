import json

class JSONStorage:
    def __init__(self, filepath):
        self.filepath = filepath

    def save(self, data):
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

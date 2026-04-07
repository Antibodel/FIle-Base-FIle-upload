class Logger:
    def __init__(self):
        self.logs = []

    def log(self, level, message):
        entry = {
            "level": level,
            "message": message
        }
        self.logs.append(entry)

    def get_logs(self):
        return self.logs

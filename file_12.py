import time

class RateLimiter:
    def __init__(self):
        self.calls = {}

    def allow(self, user):
        now = time.time()
        if user not in self.calls or now - self.calls[user] > 1:
            self.calls[user] = now
            return True
        return False

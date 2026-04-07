from datetime import datetime, timedelta

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        expiry = datetime.now() + timedelta(hours=1)
        self.sessions[user_id] = expiry
        return expiry

    def is_valid(self, user_id):
        return user_id in self.sessions and self.sessions[user_id] > datetime.now()

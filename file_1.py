import hashlib
from datetime import datetime

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        user_id = hashlib.md5(username.encode()).hexdigest()
        self.users[user_id] = {
            "username": username,
            "password": hashlib.sha256(password.encode()).hexdigest(),
            "created_at": datetime.now().isoformat()
        }
        return user_id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def validate_login(self, username, password):
        for uid, user in self.users.items():
            if user["username"] == username:
                return user["password"] == hashlib.sha256(password.encode()).hexdigest()
        return False

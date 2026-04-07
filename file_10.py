class AuthMiddleware:
    def __init__(self, session_manager):
        self.session_manager = session_manager

    def authorize(self, user_id):
        return self.session_manager.is_valid(user_id)

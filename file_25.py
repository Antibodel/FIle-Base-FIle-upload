class APIResponse:
    def success(self, data):
        return {
            "status": "success",
            "data": data
        }

    def error(self, message):
        return {
            "status": "error",
            "message": message
        }

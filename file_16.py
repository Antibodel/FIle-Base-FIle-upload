class Validator:
    def is_email(self, value):
        return "@" in value and "." in value

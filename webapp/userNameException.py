# Excaption to handle duplicated username when connecting with client
class UserNameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

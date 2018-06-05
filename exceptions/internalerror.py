from exceptions.error import PlyError

class PlyInternalError(PlyError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return 'InternalError: {0}'.format(self.message)

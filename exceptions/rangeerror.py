from exceptions.error import PlyError

class PlyRangeError(PlyError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return 'RangeError: {0}'.format(self.message)

from exceptions.error import PlyError

class PlyRangeError(PlyError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    @staticmethod
    def out(var):
        if type(var) is str:
            return PlyRangeError('string out of range')

    def __str__(self):
        return 'RangeError: {0}'.format(self.message)

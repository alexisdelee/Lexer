from os import path
from inspect import getframeinfo
from exceptions.error import PlyError

class PlyRangeError(PlyError):
    def __init__(self, frame, message):
        super().__init__(frame, message)
        self.frame = frame
        self.message = message

    @staticmethod
    def out(frame, var):
        if type(var) is str:
            return PlyRangeError(frame, 'string out of range')

    def __str__(self):
        frameinfo = getframeinfo(self.frame)
        return 'RangeError: {0} ({1}:{2})'.format(self.message, path.basename(frameinfo.filename), frameinfo.lineno)

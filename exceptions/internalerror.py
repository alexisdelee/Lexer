from os import path
from inspect import getframeinfo
from exceptions.error import PlyError

class PlyInternalError(PlyError):
    def __init__(self, frame, message):
        super().__init__(frame, message)
        self.frame = frame
        self.message = message

    def __str__(self):
        frameinfo = getframeinfo(self.frame)
        return 'InternalError: {0} ({1}:{2})'.format(self.message, path.basename(frameinfo.filename), frameinfo.lineno)

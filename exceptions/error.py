from os import path
from inspect import getframeinfo

class PlyError(Exception):
    def __init__(self, frame, message):
        super().__init__(message)
        self.frame = frame
        self.message = message

    def __str__(self):
        frameinfo = getframeinfo(self.frame)
        return 'Error: {0} ({1}:{2})'.format(self.message, path.basename(frameinfo.filename), frameinfo.lineno)

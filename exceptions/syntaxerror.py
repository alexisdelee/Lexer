from os import path
from inspect import getframeinfo
from exceptions.error import PlyError

class PlySyntaxError(PlyError):
    def __init__(self, frame, message):
        super().__init__(frame, message)
        self.frame = frame
        self.message = message

    @staticmethod
    def undefined(frame, var):
        raise PlySyntaxError(frame, '"{0}" is not defined'.format(var))

    @staticmethod
    def defined(frame, var):
        raise PlySyntaxError(frame, 'variable "{0}" already defined'.format(var))

    @staticmethod
    def expected(frame, argc):
        raise PlySyntaxError(frame, 'this function expected {0} arguments'.format(argc))

    def __str__(self):
        frameinfo = getframeinfo(self.frame)
        return 'SyntaxError: {0} ({1}:{2})'.format(self.message, path.basename(frameinfo.filename), frameinfo.lineno)

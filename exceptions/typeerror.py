from os import path
from inspect import getframeinfo
from exceptions.error import PlyError

class PlyTypeError(PlyError):
    def __init__(self, frame, message):
        super().__init__(frame, message)
        self.frame = frame
        self.message = message

    @staticmethod
    def require(frame, var, datatypes):
        for datatype in datatypes:
            if datatype is None:
                if var is None:
                    return var
            elif type(var) is datatype:
                return var
        raise PlyTypeError(frame, 'this method wait a variable of type {0} instead of {1}'.format(datatypes[0], type(var)))

    @staticmethod
    def assignment(frame):
        return PlyTypeError(frame, 'assignment to constant variable')

    @staticmethod
    def unknown(frame):
        return PlyTypeError(frame, 'unknown type')

    def __str__(self):
        frameinfo = getframeinfo(self.frame)
        return 'TypeError: {0} ({1}:{2})'.format(self.message, path.basename(frameinfo.filename), frameinfo.lineno)

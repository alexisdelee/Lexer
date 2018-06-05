from exceptions.error import PlyError

class PlyTypeError(PlyError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    @staticmethod
    def require(var, datatypes):
        for datatype in datatypes:
            if type(var) is datatype:
                return var
        raise PlyTypeError('this method wait a variable of type {0} instead of {1}'.format(datatypes[0], type(var)))

    def __str__(self):
        return 'TypeError: {0}'.format(self.message)

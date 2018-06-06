from exceptions.error import PlyError

class PlySyntaxError(PlyError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    @staticmethod
    def undefined(var):
        raise PlySyntaxError('"{0}" is not defined'.format(var))

    @staticmethod
    def defined(var):
        raise PlySyntaxError('variable "{0}" already defined'.format(var))

    def __str__(self):
        return 'SyntaxError: error at [ {0} ]'.format(self.message)

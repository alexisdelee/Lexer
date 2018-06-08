def flatten(arguments, argumentsList = []):
    for argument in arguments:
        if type(argument) is not tuple:
            argumentsList = argumentsList + [ argument ]
        else:
            argumentsList = argumentsList + flatten(argument, argumentsList)

    return argumentsList

def getAllScope(context, argumentKeys, argumentsValues):
    arguments = flatten(argumentsValues)
    scope = { **context, **argumentKeys }

    index = len(arguments) if len(arguments) < len(argumentKeys.items()) else len(argumentKeys.items())
    i = 0
    for key, data in list(argumentKeys.items())[:index]:
        if type(arguments[i]) is int or type(arguments[i]) is float:
            scope[key] = Variable(arguments[i], Variable.number, True, None)
        else:
            scope[key] = Variable(arguments[i], Variable.string, True, None)
        i = i + 1

    return scope

class Variable:
    none = 1
    pointer = 2
    number = 4
    string = 8
    char = 16
    function = 32
    unknown = 1073741824
    reference = 2147483648

    def __init__(self, value, type, writable, arguments):
        self.value = value
        self.type = type
        self.writable = writable
        self.arguments = {}

        if arguments is not None:
            for argument in arguments:
                self.arguments[argument] = Variable(None, Variable.none, True, None)

    @staticmethod
    def getScope(var):
        _ = var.value if var.type & Variable.pointer else var
        if _.type & Variable.pointer:
            return Variable.getScope(_)
        else:
            return _

    @staticmethod
    def getReferenceType(var):
        flag = 0

        _ = Variable.getScope(var)
        if type(_.value) is int or type(_.value) is float:
            flag = Variable.number
        elif type(_.value) is str:
            flag = Variable.string
        elif _.type & Variable.function:
            flag = Variable.function

        if var.type & Variable.pointer:
            flag = flag | Variable.pointer

        return flag

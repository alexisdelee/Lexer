from exceptions.error import PlyError
from exceptions.internalerror import PlyInternalError
from exceptions.rangeerror import PlyRangeError
from exceptions.syntaxerror import PlySyntaxError
from exceptions.typeerror import PlyTypeError

def flatten(arguments, argumentsList = []):
    for argument in arguments:
        if type(argument) is not tuple:
            argumentsList = argumentsList + [ argument ]
        else:
            argumentsList = argumentsList + flatten(argument, argumentsList)

    return argumentsList

class Variable:
    none      = 1
    pointer   = 2
    number    = 4
    string    = 8
    char      = 16
    function  = 32
    unknown   = 1073741824
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

# stock all used variables
variables = {}

def runtime(p):
    if type(p) is int \
            or type(p) is float \
            or type(p) is str \
            or p is None:
        return p
    else:
        if p[0] == '+':
            a = PlyTypeError.require(runtime(p[1]), [ int, float, str ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float, str ])
            if type(a) is str or type(b) is str:
                return str(a) + str(b)
            else:
                return a + b
        elif p[0] == '-':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a - b
        elif p[0] == '*':
            a = PlyTypeError.require(runtime(p[1]), [ int, float, str ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a * b
        elif p[0] == '/':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a / b
        elif p[0] == '**':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a ** b
        elif p[0] == '%':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a % b
        elif p[0] == '<':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a < b
        elif p[0] == '<=':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a <= b
        elif p[0] == '>':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a > b
        elif p[0] == '>=':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a >= b
        elif p[0] == '==':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a == b
        elif p[0] == '!=':
            a = PlyTypeError.require(runtime(p[1]), [ int, float ])
            b = PlyTypeError.require(runtime(p[2]), [ int, float ])
            return a != b
        elif p[0] == '=':
            try:
                _ = Variable.getScope(variables[p[2]])
                a = runtime(p[3])

                if p[1] & Variable.pointer:
                    b = _ if p[1] & Variable.reference else variables[p[2]]
                    if b.writable is False:
                        raise PlyTypeError.assignment()

                    if p[1] & Variable.unknown:
                        try:
                            b.value = variables[p[3]]
                            b.type = Variable.pointer
                        except LookupError:
                            raise PlySyntaxError.undefined(p[3])
                    else:
                        b.value = a
                        b.type = Variable.number if type(a) is int or type(a) is float else Variable.string
                elif p[1] & ( Variable.number | Variable.string ):
                    if _.writable is False:
                        raise PlyTypeError.assignment()

                    _.value = a
                    _.type = Variable.number if type(a) is int or type(a) is float else Variable.string
            except LookupError:
                raise PlySyntaxError.undefined(p[2])
        elif p[0] == 'RETURN':
            try:
                variables[p[1]]
                _ = Variable.getScope(variables[p[1]])
                if _.type & ( Variable.number | Variable.string ):
                    return _.value
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'DEFINE':            
            try:
                variables[p[3]]
                raise PlySyntaxError.defined(p[3])
            except LookupError:
                if p[1] & Variable.pointer:
                    if p[1] & Variable.unknown:
                        try:
                            variables[p[3]] = Variable(variables[p[4]], p[1] ^ Variable.unknown, p[2], None) # remove unknown flag
                        except:
                            raise PlySyntaxError.undefined(p[4])
                elif p[1] & ( Variable.number | Variable.string ):
                    a = runtime(p[4])
                    if type(a) is int or type(a) is float:
                        variables[p[3]] = Variable(a, Variable.number, p[2], None)
                    else:
                        variables[p[3]] = Variable(a, Variable.string, p[2], None)
                elif p[1] & Variable.function:
                    variables[p[3]] = Variable(p[5], Variable.function, p[2], None if p[4] is None else flatten(p[4]))
                else:
                    raise PlyTypeError.unknown()
        elif p[0] == 'CALL_FUNCTION':
            try:
                _ = Variable.getScope(variables[p[1]])
                if _.type & Variable.function:
                    if p[2] is not None:
                        arguments = flatten(p[2])
                        scope = { **variables, **_.arguments }

                        index = len(arguments) if len(arguments) < len(_.arguments.items()) else len(_.arguments.items())
                        i = 0
                        for key, data in list(_.arguments.items())[:index]:
                            if scope[key] is not None:
                                scope[key] = Variable(arguments[i], Variable.none, True, None)
                                i = i + 1

                        for key, value in scope.items():
                            print('item', key, value.value)

                    print('content', _.value)
                    return runtime(_.value)
                else:
                    raise PlySyntaxError('this method wait a variable of type <class \'function\'>')
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'IF':
            a = PlyTypeError.require(runtime(p[1]), [ bool ])
            return runtime(p[2]) if a else None
        elif p[0] == 'IFELSE':
            a = PlyTypeError.require(runtime(p[1]), [ bool ])
            return runtime(p[2]) if a else runtime(p[3])
        elif p[0] == 'FOR':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            for i in range(a, b + 1):
                runtime(p[3])
                a = PlyTypeError.require(runtime(p[1]), [ int ]) # refresh
                b = PlyTypeError.require(runtime(p[2]), [ int ])
        elif p[0] == 'WHILE':
            a = PlyTypeError.require(runtime(p[1]), [ bool ])
            while a:
                runtime(p[2])
                a = PlyTypeError.require(runtime(p[1]), [ bool ]) # refresh
        elif p[0] == 'PRINT':
            # return eval(p[1])
            print(runtime(p[1]))
        elif p[0] == 'SETAT':
            try:
                a = Variable.getScope(variables[p[2]]) if p[1] & Variable.pointer and variables[p[2]].type & Variable.pointer else variables[p[2]]
                PlyTypeError.require(a.value, [ str ])

                b = PlyTypeError.require(runtime(p[3]), [ int ])
                c = PlyTypeError.require(runtime(p[4]), [ str ])
                if len(c) != 1:
                    raise PlyTypeError('this method wait a variable of type <type \'char\'> instead of <type \'str\'>')
                elif b < 0 or b > len(c) - 1:
                    raise PlyRangeError.out(c)

                d = list(a.value)
                d[b] = c[0]
                a.value = ''.join(d)
            except LookupError:
                raise PlySyntaxError.undefined(p[2])
        elif p[0] == 'GETAT':
            try:
                variables[p[1]]
                _ = Variable.getScope(variables[p[1]])

                if _.type & Variable.string:
                    _ = PlyTypeError.require(_.value, [ str ])

                if _ is not None:
                    a = PlyTypeError.require(runtime(p[2]), [ int, str ])
                    if type(a) is int:
                        return _[a]
                    elif type(a) is str:
                        return _.index(a) # indexOf
            except ValueError:
                return -1
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'SUBSTRING':
            try:
                variables[p[1]]
                _ = Variable.getScope(variables[p[1]])

                if _.type & Variable.string:
                    _ = PlyTypeError.require(_.value, [ str ])

                if _ is not None:
                    a = PlyTypeError.require(runtime(p[2]), [ None, int ])
                    b = PlyTypeError.require(runtime(p[3]), [ None, int ])
                    return _[a:b] # substring
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'TYPEOF':
            try:
                variables[p[1]]

                prefix = ''
                if variables[p[1]].writable is False:
                    prefix = 'constant of '

                if variables[p[1]].type & Variable.pointer:
                    return prefix + 'pointer'
                elif variables[p[1]].type & Variable.number:
                    return prefix + 'number'
                elif variables[p[1]].type & Variable.string:
                    return prefix + 'string'
                elif variables[p[1]].type & Variable.function:
                    return 'function'
                else:
                    return 'none'
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'DELETE':
            try:
                variables[p[1]]
                del variables[p[1]]
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        else:
            for item in enumerate(p):
                if len(p) is 2:
                    runtime(item[1])
                else:
                    runtime(item[0])

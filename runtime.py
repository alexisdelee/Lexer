from exceptions.error import PlyError
from exceptions.internalerror import PlyInternalError
from exceptions.rangeerror import PlyRangeError
from exceptions.syntaxerror import PlySyntaxError
from exceptions.typeerror import PlyTypeError

class Variable:
    none     = 1
    pointer  = 2
    number   = 4
    string   = 8
    array    = 16
    function = 32
    
    def __init__(self, value, type, writable, arguments):
        self.value = value
        self.type = type
        self.writable = writable
        self.arguments = {}

        if arguments is not None:
            for argument in arguments:
                if len(argument) is 3:
                    self.arguments[argument[1]] = argument
                else:
                    self.arguments[argument[0]] = None

    @staticmethod
    def getScope(var):
        _ = var.value if var.type & Variable.pointer else var
        if _.type & Variable.pointer:
            return Variable.getScope(_)
        else:
            return _

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
                variables[p[2]]

                _ = Variable.getScope(variables[p[2]])
                if _.writable is False:
                    raise PlyTypeError.assignment()

                if p[1] & ( Variable.number | Variable.string ):
                    a = runtime(p[3])
                    variables[p[2]].value = a

                    if type(a) is int or type(a) is float:
                        variables[p[2]].type = Variable.number
                    elif type(a) is str:
                        variables[p[2]].type = Variable.string
                elif p[1] & Variable.pointer:
                    _.value = runtime(p[3])
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
                variables[p[2]]
                raise PlySyntaxError.defined(p[2])
            except LookupError:
                if p[1] & ( Variable.number | Variable.string ):
                    variables[p[3]] = Variable(runtime(p[4]), p[1], p[2], None)
                elif p[1] & Variable.pointer:
                    try:
                        variables[p[4]]
                        variables[p[3]] = Variable(variables[p[4]], p[1], p[2], None)
                    except LookupError:
                        raise PlySyntaxError.undefined(p[4])
                elif p[1] & Variable.function:
                    variables[p[3]] = Variable(p[5], p[1], p[2], p[4])
        elif p[0] == 'CALL_FUNCTION':
            try:
                variables[p[1]]
                _ = Variable.getScope(variables[p[1]])
                if _.type & Variable.function:
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
                variables[p[2]]
                a = None

                if p[1] & Variable.pointer:
                    a = [ Variable.getScope(variables[p[2]]), None ]
                    a[1] = a[0] # avoid duplicated data
                else:
                    a = [ variables[p[2]], Variable.getScope(variables[p[2]]) ]

                b = PlyTypeError.require(runtime(p[3]), [ int ])
                c = PlyTypeError.require(runtime(p[4]), [ str ])

                d = list(a[1].value)
                d[b] = c[0]
                a[0].value = ''.join(d)
                a[0].type = Variable.string
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
                if variables[p[1]].type & Variable.pointer:
                    return 'pointer'
                elif variables[p[1]].type & Variable.number:
                    return 'number'
                elif variables[p[1]].type & Variable.string:
                    return 'string'
                elif variables[p[1]].type & Variable.function:
                    return 'function'
                else:
                    return 'none'
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        else:
            for item in enumerate(p):
                if len(p) is 2:
                    runtime(item[1])
                else:
                    runtime(item[0])

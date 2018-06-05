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
    
    def __init__(self, value, type, arguments):        
        self.value = value
        self.type = type
        self.arguments = {}

        if arguments is not None:
            for argument in arguments:
                if len(argument) is 3:
                    self.arguments[argument[1]] = argument
                else:
                    self.arguments[argument[0]] = None

    @staticmethod
    def getType(var):
        if var is None:
            return Variable.none
        elif type(var) is int or type(var) is float:
            return Variable.number
        elif type(var) is str:
            return Variable.string
        else:
            return None

# stock all used variables
variables = {}

def runtime(p):
    if type(p) is int \
            or type(p) is str\
            or p is None:
        return p
    else:
        if p[0] == '+':
            a = PlyTypeError.require(runtime(p[1]), [ int, str ])
            b = PlyTypeError.require(runtime(p[2]), [ int, str ])
            if type(a) is str or type(b) is str:
                return str(a) + str(b)
            else:
                return a + b
        elif p[0] == '-':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a - b
        elif p[0] == '*':
            a = PlyTypeError.require(runtime(p[1]), [ int, str ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a * b
        elif p[0] == '/':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a / b
        elif p[0] == '**':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a ** b
        elif p[0] == '%':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a % b
        elif p[0] == '<':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a < b
        elif p[0] == '<=':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a <= b
        elif p[0] == '>':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a > b
        elif p[0] == '>=':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a >= b
        elif p[0] == '==':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a == b
        elif p[0] == '!=':
            a = PlyTypeError.require(runtime(p[1]), [ int ])
            b = PlyTypeError.require(runtime(p[2]), [ int ])
            return a != b
        elif p[0] == '=':
            try:
                variables[p[2]] 
                # if p[1] == 'simple':
                    # variables[p[2]].value = runtime(p[3])
                    # variables[p[2]].type = 'simple'
                # elif p[1] == 'pointer':
                    # variables[p[2]].value.value = runtime(p[3])
                if p[1] & ( Variable.number | Variable.string ):
                    variables[p[2]].value = runtime(p[3])
                elif p[1] & Variable.pointer:
                    variables[p[2]].value.value = runtime(p[3])
            except LookupError:
                raise PlySyntaxError.undefined(p[2])
        elif p[0] == 'RETURN':
            try:
                variables[p[1]]                    
                # if variables[p[1]].type == 'simple':                    
                    # return variables[p[1]].value
                # elif variables[p[1]].type == 'pointer':
                    # return variables[p[1]].value.value
                if variables[p[1]].type & ( Variable.number | Variable.string ):
                    return variables[p[1]].value
                elif variables[p[1]].type & Variable.pointer:
                    return variables[p[1]].value.value
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'DEFINE':            
            try:
                variables[p[2]]
                raise PlySyntaxError.defined(p[2])
            except LookupError:
                # if p[1] == 'simple':
                    # variables[p[2]] = Variable(runtime(p[3]), 'simple', None)
                # elif p[1] == 'pointer':
                    # try:
                        # variables[p[3]]
                        # variables[p[2]] = Variable(variables[p[3]], 'pointer', None)
                    # except LookupError:
                        # raise PlySyntaxError.undefined(p[3])
                # elif p[1] == 'function':
                    # variables[p[2]] = Variable(p[4], 'function', p[3])
                if p[1] & ( Variable.number | Variable.string ):
                    variables[p[2]] = Variable(runtime(p[3]), p[1], None)
                elif p[1] & Variable.pointer:
                    try:
                        variables[p[3]]
                        variables[p[2]] = Variable(variables[p[3]], p[1], None)
                    except LookupError:
                        raise PlySyntaxError.undefined(p[3])
                elif p[1] & Variable.function:
                    variables[p[2]] = Variable(p[4], p[1], p[3])
        elif p[0] == 'CALL_FUNCTION':
            try:
                variables[p[1]]
                if (variables[p[1]].type & Variable.function) is 0:
                    raise PlySyntaxError('this method wait a variable of type <class \'function\'>')
                return runtime(variables[p[1]].value)
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
        elif p[0] == 'AT':
            try:
                variables[p[1]]
                a = None

                # if variables[p[1]].type == 'simple':
                if variables[p[1]].type & ( Variable.number | Variable.string ):
                    a = PlyTypeError.require(variables[p[1]].value, [ str ])
                #elif variables[p[1]].type == 'pointer':
                elif variables[p[1]].type & Variable.pointer:
                    a = PlyTypeError.require(variables[p[1]].value.value, [ str ])

                if a is not None:
                    b = PlyTypeError.require(runtime(p[2]), [ int, str ])
                    if type(b) is int:
                        return a[b]
                    elif type(b) is str:
                        return a.index(b) # indexOf
            except ValueError:
                return -1
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        elif p[0] == 'SUBSTRING':
            try:
                variables[p[1]]
                a = None

                # if variables[p[1]].type == 'simple':
                if variables[p[1]].type & ( Variable.number | Variable.string ):
                    a = PlyTypeError.require(variables[p[1]].value, [ str ])
                # elif variables[p[1]].type == 'pointer':
                elif variables[p[1]].type & Variable.pointer:
                    a = PlyTypeError.require(variables[p[1]].value.value, [ str ])

                if a is not None:
                    b = PlyTypeError.require(runtime(p[2]), [ None, int ])
                    c = PlyTypeError.require(runtime(p[3]), [ None, int ])
                    return a[b:c] # substring
            except LookupError:
                raise PlySyntaxError.undefined(p[1])
        else:
            for item in enumerate(p):
                if len(p) is 2:
                    runtime(item[1])
                else:
                    runtime(item[0])

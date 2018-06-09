from inspect import currentframe
from exceptions.error import PlyError
from exceptions.internalerror import PlyInternalError
from exceptions.rangeerror import PlyRangeError
from exceptions.syntaxerror import PlySyntaxError
from exceptions.typeerror import PlyTypeError
from business import Variable, flatten, getAllScope

# stock all used variables
variables = {}

def runtime(p, context = variables):
    if type(p) is int \
            or type(p) is float \
            or type(p) is str \
            or p is None:
        return p
    else:
        if p[0] == '+':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float, str ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float, str ])
            if type(a) is str or type(b) is str:
                return str(a) + str(b)
            else:
                return a + b
        elif p[0] == '-':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a - b
        elif p[0] == '*':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float, str ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a * b
        elif p[0] == '/':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a / b
        elif p[0] == '**':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a ** b
        elif p[0] == '%':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a % b
        elif p[0] == '<':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a < b
        elif p[0] == '<=':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a <= b
        elif p[0] == '>':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a > b
        elif p[0] == '>=':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a >= b
        elif p[0] == '==':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a == b
        elif p[0] == '!=':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int, float ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, float ])
            return a != b
        elif p[0] == '=':
            try:
                _ = Variable.getScope(context[p[2]])
                a = runtime(p[3], context)

                if p[1] & Variable.pointer:
                    b = _ if p[1] & Variable.reference else context[p[2]]
                    if b.writable is False:
                        raise PlyTypeError.assignment(currentframe())

                    if p[1] & Variable.unknown:
                        try:
                            b.value = context[p[3]]
                            b.type = Variable.pointer
                        except LookupError:
                            raise PlySyntaxError.undefined(currentframe(), p[3])
                    else:
                        b.value = a
                        b.type = Variable.number if type(a) is int or type(a) is float else Variable.string
                elif p[1] & ( Variable.number | Variable.string ):
                    if _.writable is False:
                        raise PlyTypeError.assignment(currentframe())

                    _.value = a
                    _.type = Variable.number if type(a) is int or type(a) is float else Variable.string
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[2])
        elif p[0] == 'RETURN':
            try:
                context[p[1]]
                _ = Variable.getScope(context[p[1]])
                if _.type & ( Variable.number | Variable.string ):
                    return _.value
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[1])
        elif p[0] == 'DEFINE':            
            # try:
            #     variables[p[3]]
            #     raise PlySyntaxError.defined(p[3])
            # except LookupError:
            #     if p[1] & Variable.pointer:
            #         if p[1] & Variable.unknown:
            #             try:
            #                 variables[p[3]] = Variable(variables[p[4]], p[1] ^ Variable.unknown, p[2], None) # remove unknown flag
            #             except:
            #                 raise PlySyntaxError.undefined(p[4])
            #     elif p[1] & ( Variable.number | Variable.string ):
            #         a = runtime(p[4], context)
            #         if type(a) is int or type(a) is float:
            #             variables[p[3]] = Variable(a, Variable.number, p[2], None)
            #         else:
            #             variables[p[3]] = Variable(a, Variable.string, p[2], None)
            #     elif p[1] & Variable.function:
            #         a = p[4] if type(p[4]) is tuple else tuple([ p[4] ])
            #         variables[p[3]] = Variable(p[5], Variable.function, p[2], None if p[4] is None else flatten(a))
            #     else:
            #         raise PlyTypeError.unknown()
            try:
                context[p[3]]
                raise PlySyntaxError.defined(currentframe(), p[3])
            except LookupError:
                if p[1] & Variable.pointer:
                    if p[1] & Variable.unknown:
                        try:
                            context[p[3]] = Variable(context[p[4]], p[1] ^ Variable.unknown, p[2], None)  # remove unknown flag
                        except:
                            raise PlySyntaxError.undefined(currentframe(), p[4])
                elif p[1] & (Variable.number | Variable.string):
                    a = runtime(p[4], context)
                    if type(a) is int or type(a) is float:
                        context[p[3]] = Variable(a, Variable.number, p[2], None)
                    else:
                        context[p[3]] = Variable(a, Variable.string, p[2], None)
                elif p[1] & Variable.function:
                    a = p[4] if type(p[4]) is tuple else tuple([p[4]])
                    context[p[3]] = Variable(p[5], Variable.function, p[2], None if p[4] is None else flatten(a))
                else:
                    raise PlyTypeError.unknown(currentframe())
        elif p[0] == 'CALL_FUNCTION':
            try:
                _ = Variable.getScope(context[p[1]])
                scope = context
                if _.type & Variable.function:
                    if p[2] is not None:
                        a = p[2] if type(p[2]) is tuple else tuple([ p[2] ])
                        b = list(map(lambda b: runtime(b, context), list(a)))
                        scope = getAllScope(context.copy(), _.arguments, b)
                    else:
                        argc = len(_.arguments.items())
                        if argc != 0:
                            raise PlySyntaxError.expected(currentframe(), argc)

                    return runtime(_.value, scope.copy())
                else:
                    raise PlySyntaxError(currentframe(), 'this method wait a variable of type <class \'function\'>')
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[1])
        elif p[0] == 'IF':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ bool ])
            return runtime(p[2], context.copy()) if a else None
        elif p[0] == 'IFELSE':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ bool ])
            return runtime(p[2], context.copy()) if a else runtime(p[3], context)
        elif p[0] == 'FOR':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int ])
            b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int ])
            for i in range(a, b + 1):
                runtime(p[3], context.copy())
                a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ int ]) # refresh
                b = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int ])
        elif p[0] == 'WHILE':
            a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ bool ])
            while a:
                runtime(p[2], context.copy())
                a = PlyTypeError.require(currentframe(), runtime(p[1], context), [ bool ]) # refresh
        elif p[0] == 'PRINT':
            # return eval(p[1])
            print(runtime(p[1], context))
        elif p[0] == 'SETAT':
            try:
                a = Variable.getScope(variables[p[2]]) if p[1] & Variable.pointer and variables[p[2]].type & Variable.pointer else variables[p[2]]
                PlyTypeError.require(currentframe(), a.value, [ str ])

                b = PlyTypeError.require(currentframe(), runtime(p[3], context), [ int ])
                c = PlyTypeError.require(currentframe(), runtime(p[4], context), [ str ])
                if len(c) != 1:
                    raise PlyTypeError(currentframe(), 'this method wait a variable of type <type \'char\'> instead of <type \'str\'>')
                elif b < 0 or b > len(c) - 1:
                    raise PlyRangeError.out(currentframe(), c)

                d = list(a.value)
                d[b] = c[0]
                a.value = ''.join(d)
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[2])
        elif p[0] == 'GETAT':
            try:
                context[p[1]]
                _ = Variable.getScope(context[p[1]])

                if _.type & Variable.string:
                    _ = PlyTypeError.require(currentframe(), _.value, [ str ])

                if _ is not None:
                    a = PlyTypeError.require(currentframe(), runtime(p[2], context), [ int, str ])
                    if type(a) is int:
                        return _[a]
                    elif type(a) is str:
                        return _.index(a) # indexOf
            except ValueError:
                return -1
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[1])
        elif p[0] == 'SUBSTRING':
            try:
                context[p[1]]
                _ = Variable.getScope(context[p[1]])

                if _.type & Variable.string:
                    _ = PlyTypeError.require(currentframe(), _.value, [ str ])

                if _ is not None:
                    a = PlyTypeError.require(currentframe(), runtime(p[2], context), [ None, int ])
                    b = PlyTypeError.require(currentframe(), runtime(p[3], context), [ None, int ])
                    return _[a:b] # substring
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[1])
        elif p[0] == 'TYPEOF':
            try:
                context[p[1]]

                prefix = ''
                if context[p[1]].writable is False:
                    prefix = 'constant of '

                if context[p[1]].type & Variable.pointer:
                    return prefix + 'pointer'
                elif context[p[1]].type & Variable.number:
                    return prefix + 'number'
                elif context[p[1]].type & Variable.string:
                    return prefix + 'string'
                elif variables[p[1]].type & Variable.function:
                    return 'function'
                else:
                    return 'none'
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[1])
        elif p[0] == 'DELETE':
            try:
                variables[p[1]]
                del variables[p[1]]
            except LookupError:
                raise PlySyntaxError.undefined(currentframe(), p[1])
        else:
            for item in enumerate(p):
                if len(p) is 2:
                    runtime(item[1], context)
                else:
                    runtime(item[0], context)

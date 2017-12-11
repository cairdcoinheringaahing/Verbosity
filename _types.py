import sys

import _exceptions as exceptions

text = sys.stdin.read()
stdin = iter(text)
lines = iter(text.split('\n'))

class BaseClass(object):
    def __init__(self, value=None):
        try: self.base = self.__class__.__mro__[2]
        except: self.base = self.__class__
        try: self.value = self.base(value)
        except: self.value = self.base()
        
    @staticmethod
    def __run_method__(master, method, args):
        try: func = getattr(master, method)
        except: return exceptions.RaiseException('UnknownMethodCall')
        value = func(*args)
        master.value = value
        return value

    def __repr__(self):
        return '{}<{}>'.format(self.__class__.__name__, self.value)

class Array(BaseClass, list):
    def __repr__(self):
        return "Array<{}>".format("; ".join(map(str, self.value)))

class Binary(BaseClass):
    def __repr__(self):
        return "BinaryInteger<{}>".format("".join(map(str, self.value)))

class Boolean(BaseClass):
    TRUE = True
    FALSE = False

    def __init__(self, value=None):
        self.value = bool(value)
    
    def __repr__(self):
        return "Boolean<{}>".format("TRUE" if self.value else "FALSE")

    def LessThan(self, x, y):
        return x.value < y.value

    def GreaterThan(self, x, y):
        return x.value > y.value

    def ArgumentsAreEqual(self, x, y):
        return x.value == y.value

    def GreaterThanOrEqualTo(self, x, y):
        return x.value >= y.value

    def LessThanOrEqualTo(self, x, y):
        return x.value <= y.value

    def LogicalNot(self, value):
        return not value.value

    def LogicalAnd(self, x, y):
        return x.value and y.value

    def LogicalOr(self, x, y):
        return x.value or y.value

class Complex(BaseClass, complex):
    def __init__(self, real, imag):
        self.REAL = real
        self.IMAGINARY = imag
                
    def __repr__(self):
        return "Complex<{}; {}>".format(self.real, self.imag)

class Dictionary(BaseClass, dict):
    pass

class FloatingPoint(BaseClass, float):
    pass

class Input(BaseClass):
    def __repr__(self):
        return "Input metaclass"
    
    def ReadAllFromInput(self):
        return ''.join(stdin)
    
    def ReadCharacterFromInput(self):
        return next(stdin)
    
    def ReadEvaluatedLineFromInput(self):
        return eval(next(lines))
    
    def ReadEvaluatedStringFromInput(self):
        return eval(''.join(stdin))
    
    def ReadLineFromInput(self):
        return next(lines)
    
    def ReadIntegerFromInput(self):
        global stdin
        token = ''
        for char in stdin:
            if char.isdigit():
                token += char
            else:
                break
        stdin = iter([char] + list(stdin))
        return int(token)

class Integer(BaseClass, int):
    def Increment(self):
        return self.value + 1
        
    def Decrement(self):
        return self.value - 1

    def Sum(self, y):
        return self.value + y.value

    def Difference(self, y):
        return self.value - y.value

    def Product(self, y):
        return self.value * y.value

    def Quotient(self, y):
        if type(y) != Integer:
            exceptions.RaiseException('Right argument must be Integer type')
        return self.value / y.value
    def Remainder(self, y):
        return self.value % y.value

    __str__ = BaseClass.__repr__

class Output(BaseClass):
    FILE = sys.stdout
    LAST = ''
    WRITTEN = ''
    
    def __repr__(self):
        return "Output metaclass"

    def DisplayAsText(self, text, end='\n'):
        text, end = map(str, [text, end])
        Output.FILE.write(text + end)
        Output.LAST = text
        Output.WRITTEN += text + end

class String(BaseClass, str):
    def TakeLastCharacters(self, n):
        return self.value[Integer(-n):]
    
    def TakeFirstCharacters(self, n):
        return self.value[:Integer(-n)]

    def RemoveCharactersFromStart(self, n):
        return self.value[Integer(n):]

    def RemoveCharactersFromEnd(self, n):
        return self.value[:Integer(n)]

class UnorderedSet(BaseClass, set):
    def __repr__(self):
        return "UnorderedSet<{}>".format("; ".join(map(str, self.value)))

import exceptions

class BaseClass(object):
	def __init__(self, value=None):
		base = self.__class__.__mro__[2]
		try: self.value = base(value)
		except: self.value = base()
			
	def __run_method__(self, method, args):
		try: getattr(self, method)
		except: return exceptions.RaiseException('UnknownMethodCall')
		value = getattr(self, method)(*args)
		self = value
		return value

class Array(BaseClass, list):
	def __repr__(self):
		return "Array<{}>".format("; ".join(map(str, self.value)))

class Binary(BaseClass):
	def __repr__(self):
		return "BinaryInteger<{}>".format("; ".join(map(str, self.value)))

class Boolean(BaseClass):
	def __repr__self):
		return "Boolean<{}>".format(["False", "True"][self.value])

class Complex(BaseClass, complex):
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
		
	def __repr__(self):
		return "Complex<{}; {}>".format(self.real, self.imag)

class Dictionary(BaseClass, dict):
	pass

class FloatingPoint(BaseClass, float):
	def __repr__(self):
		return "FloatingPoint<{}>".format(self.value)

class Input(BaseClass):
	def __repr__(self):
		return "Input metaclass"

class Integer(BaseClass, int):
	def __repr__(self):
		return "Integer<{}>".format(self.value)

class Output(BaseClass):
	def __repr__(self):
		return "Output metaclass"

class String(BaseClass, str):
	def __repr__(self):
		return "String<{}>".format(self.value)

class Set(BaseClass, set):
	def __repr__(self):
		return "Set<{}>".format("; ".join(map(str, self.value)))

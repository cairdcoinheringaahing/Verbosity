import exceptions

class BaseClass(object):
	def __init__(self, value=None):
		self.base = self.__class__.__mro__[2]
		try: self.value = self.base(value)
		except: self.value = self.base()
	
	@staticmethod
	def __run_method__(master, method, args):
		try: func = getattr(master, method)
		except: return exceptions.RaiseException('UnknownMethodCall')
		value = func(master, *args)
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
	def __repr__(self):
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
	pass

class Input(BaseClass):
	def __repr__(self):
		return "Input metaclass"

class Integer(BaseClass, int):
	def Increment(self):
		return self.value + 1
	
	def Decrement(self):
		return self.value - 1

class Output(BaseClass):
	def __repr__(self):
		return "Output metaclass"

class String(BaseClass, str):
	pass

class Set(BaseClass, set):
	def __repr__(self):
		return "Set<{}>".format("; ".join(map(str, self.value)))

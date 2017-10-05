import exceptions

class BaseClass(object):
	def __init__(self, value=None):
		base = self.__class__.__mro__[1]
		try: self.value = base(value)
		except: self.value = base()
			
	def __run_method__(self, method, args):
		try: getattr(self, method)
		except: exceptions.RaiseException('UnknownMethodCall')
		value = getattr(self, method)(*args)
		self = value
		return value

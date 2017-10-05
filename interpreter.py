import re
import sys

import exceptions
import parser
import _types as types

VARIABLES = {}
INCLUDES = []
PARENTS = {'Array':types.Array,
	   'Binary':types.Binary,
	   'Boolean':types.Boolean,
	   'Complex':types.Complex,
	   'Dictionary':types.Dictionary,
	   'FloatingPoint':types.FloatingPoint,
	   'Input':types.Input,
           'Integer':types.Integer,
	   'Output':types.Output,
           'String':types.String,
	   'Set':types.Set}

STRUCTURES = {'Class':types.Structures.Class,
	      'Conditional':types.Structures.Conditional,
	      'Error':types.Structures.Error,
	      'Function':types.Structures.Function,
	      'Loop':types.Structures.Loop}

def isint(string):
	return re.search(r'^-?\d+$', string) and 'Integer' in INCLUDES

def isreal(string):
	return re.search(r'^-?\d+\.\d+$', string) and 'FloatingPoint' in INCLUDES

def iscomplex(string):
	return re.search(r'^\d+(\.\d+)?[\+-]\d+(\.\d+)?j$', string) and 'Complex' in INCLUDES

def isstring(string):
	return re.search(r'^"|(""").*\1$', string) and 'String' in INCLUDES

def arg_eval(args):
	for arg in args:
		if isint(arg):
			yield types.Integer(arg)
		if isreal(arg):
			yield types.FloatingPoint(arg)
		if iscomplex(arg):
			yield types.Complex(arg)
		if isstring(arg):
			yield types.String(arg)
		if arg.split(':')[0] in INCLUDES:
			type_ = PARENTS[arg.split(':')[0]]
			method = arg.split(':')[1]
			a = list(arg_eval(arg))
			yield type_.__run_method__(method, a)
		if arg.split(':')[0] in VARIABLES.keys():
			var = VARIABLES[arg.split(':')[0]]
			method = arg.aplit(':')[1]
			a = list(arg_eval(arg))
			yield var.__run_method__(method, a)
			
		try:
			yield eval("types." + str(arg))
		except:
			try: yield eval(arg)
			except: yield []

def interpreter(code, stdin, ARGV, stdout):
	code = parser.parser(code)
	for line in code:
		func = line[0]
		
		if func == 'Include':
			new_type = line[1]
			INCLUDES.append(new_type[0])
			
		if re.search(r'({}):DefineVariable'.format('|'.join(INCLUDES)), func):
			variable_type = PARENTS[func.split(':DefineVariable')[0]]
			name = line[1][0]
			value = line[1][1]
			VARIABLES[name] = variable_type(value)
			
		elif re.search(r'({}):RedefineVariable'.format('|'.join(INCLUDES)), func):
			name = line[1][0]
			new_value = line[1][1]
			try: variable_type = VARIABLES[name].type_of
			except: raise AttemptToRedefineUnknownVariable(name)
			VARIABLES[name] = variable_type(value)
			
		elif func.split(':')[0] in INCLUDES:
			type_ = PARENTS[func.split(':')[0]]
			method = func.split(':')[1]
			args = list(args_eval(line[1]))
			type_.__run_method__(method, args)
			
		elif func.split(':')[0] in VARIABLES.keys():
			var = VARIABLES[func.split(':')[0]]
			method = func.split(':')[1]
			args = list(args_eval(line[1]))
			var.__run_method__(method, args)
		
print(INCLUDES)

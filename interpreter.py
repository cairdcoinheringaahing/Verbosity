import re
import sys

import exceptions
import parser
import _types as types
import _structs as structures

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

STRUCTURES = {'Class':structures.Class,
	      'Conditional':structures.Conditional,
	      'Error':structures.Error,
	      'Function':structures.Function,
	      'Loop':structures.Loop}

def isint(string):
	return re.search(r'^-?\d+$', string) and 'Integer' in INCLUDES

def isreal(string):
	return re.search(r'^-?\d+\.\d+$', string) and 'FloatingPoint' in INCLUDES

def iscomplex(string):
	return re.search(r'^-?\d+(\.\d+)?[+-]\d+(\.\d+)?j$', string) and 'Complex' in INCLUDES

def isstring(string):
	return re.search(r'^"|(""").*\1$', string) and 'String' in INCLUDES

def standard_eval(*args):
	for value in args:
		if isint(value):
			yield types.Integer(value)
		if isreal(value):
			yield types.FloatingPoint(value)
		if iscomplex(value):
			yield types.Complex(value)
		if isstring(value):
			yield types.String(value)
		if value in VARIABLES.keys():
			yield VARIABLES[value]

def define_eval(*args):
	args = args[:(args[0].split(':')[0] in INCLUDES)+1]
	if len(args) == 1:
		value = args[0]
	else:
		type_, method = args[0].split(':')
		type_ = PARENTS[type_]
		new_args = list(standard_eval(*args[1]))
		return type_.__run_method__(type_, method, new_args)

	if isint(value):
		return types.Integer(value)
	if isreal(value):
		return types.FloatingPoint(value)
	if iscomplex(value):
		return types.Complex(value)
	if isstring(value):
		return types.String(value)

def handle_line(line):
	func = line[0]
		
	if func == 'Include':
		new_type = line[1]
		INCLUDES.append(new_type[0])
			
	elif re.search(r'({}):DefineVariable'.format('|'.join(INCLUDES)), func):
		variable_type = PARENTS[func.split(':DefineVariable')[0]]
		name = line[1][0]
		value = define_eval(*line[1][1:])
		VARIABLES[name] = variable_type(value)
			
	elif re.search(r'({}):RedefineVariable'.format('|'.join(INCLUDES)), func):
		name = line[1][0]
		new_value = define_eval(*line[1][1:])
		try: variable_type = VARIABLES[name].__class__
		except: exceptions.RaiseException('AttemptToRedefineUnknownVariable')
		VARIABLES[name] = variable_type(new_value)
			
	elif func.split(':')[0] in INCLUDES:
		type_ = PARENTS[func.split(':')[0]]
		method = func.split(':')[1]
		args = list(standard_eval(*line[1]))
		type_.__run_method__(type_, method, args)
			
	elif func.split(':')[0] in VARIABLES.keys():
		var = VARIABLES[func.split(':')[0]]
		type_ = var.__class__
		method = func.split(':')[1]
		args = list(standard_eval(*line[1]))
		type_.__run_method__(var, method, args)

def interpreter(code):
	code = parser.parser(code)
	for i, line in enumerate(code, 1):
		handle_line(line)

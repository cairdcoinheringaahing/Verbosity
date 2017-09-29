import re, sys
import exceptions, parser, types

VARIABLES = {}
PARENTS = {'Array':types.Array, 'Binary':types.Binary, 'Boolean':types.Boolean,
           'Class':types.Class, 'Complex':types.Complex,
           'Conditional':types.Conditional, 'Dictionary':types.Dictionary,
           'Error':types.Error, 'FloatingPoint':types.FloatingPoint,
           'Function':types.Function, 'Input':types.Input,
           'Integer':types.Integer, 'Loop':types.Loop, 'Output':types.Output,
           'String':types.String, 'Set':types.Set}
           
INCLUDES = []

def interpreter(code, stdin, ARGV, stdout):
	code = parser.parser(code)
	for line in code:
		func = line[0]
		if func == 'Include':
			new_type = line[1]
			if len(new_type) > 1:
				for new in new_type:
					INCLUDES.append(PARENTS[new])
			else:
				INCLUDES.append(new_type[0])
		if func.search(r'({}):DefineVariable'.format('|'.join(INCLUDES)), func):
			variable_type = PARENTS[func.split(':DefineVariable')[0]]
			name = line[1][0]
			value = line[1][1]
			VARIABLES[name] = variable_type(value)
		elif func.search(r'({}):RedefineVariable'.format('|'.join(INCLUDES)), func):
			name = line[1][0]
			new_value = line[1][1]
			try: variable_type = VARIABLES[name].type_of
			except: raise AttemptToRedefineUnknownVariable(name)
			VARIABLES[name] = variable_type(value)
		elif func.split(':')[0] in PARENTS.keys():
			type_ = PARENTS[func.split(':')[0]]
			method = func.split(':')[1]
			args = line[1]
			try: type_
			

print(INCLUDES)

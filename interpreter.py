import parser, sys, types

VARIABLES = {}
PARENTS = {'Array':types.Array, 'Binary':types.Binary, 'Boolean':types.Boolean,
           'Class':types.Class, 'Complex':types.Complex,
           'Conditional':types.Conditional, 'Dictionary':types.Dictionary,
           'Error':types.Error, 'FloatingPoint':types.FloatingPoint,
           'Function':types.Function, 'Input':types.Input,
           'Integer':types.Integer, 'Loop':types.Loop, 'Output':types.Output,
           'String':types.String, 'Set':types.Set}
           
INCLUDES = []

program = parser.parser(open(input()).read())

def func_progress(string):
    parent = 

for line in program:
    func = func_process(line[0])
    args = args_process(line[1:])

print(INCLUDES)

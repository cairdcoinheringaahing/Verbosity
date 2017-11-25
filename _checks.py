import builtins

import _types as types

def ispytype(instance):
    pass

def boolean(value):
    try:
        return value.value
    except:
        return value

import functools

from PackageTest.Calculator2Operands import logger

@logger
def sum(*args):
    if len(args) == 0:
        return 0
    else:
        return functools.reduce(lambda x,y:x+y, args)

@logger
def sub(a,b):
    return a - b

@logger
def multiply(*args):
    return 1 if len(args) == 0 else functools.reduce(lambda x, y:x*y, args)

@logger
def division(a,b):
    return float(a) / float(b)

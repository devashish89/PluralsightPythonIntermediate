# context manager is an object to be used with-statement
# with context-manager:
#     //enter() /context-manager.begin() is like setup() or allocation()
#     Body
#     //exit() /context-manager.end() is like tearDown() or deallocation()
# these context-manager.begin() and context-manager.end() works in case of exceptions

class LoggingContextManager:

    def __enter__(self):
        print("LoggingContextManager().__enter__()")
        return "You are in with block"

    def __exit__(self, exception_type, exception_value, traceback):
        # __exit__() return False : propagate exceeption
        # __exit__() return True : swallow the exception
        if exception_type is None:
            print("LoggingContextManager.__exit__() exited without exception")
        else:
            print("LoggingContextManager().__exit__({}, {}, {})".format(exception_type, exception_value, traceback))
        return None ## None == False in boolean

try:
    with LoggingContextManager() as x:
        print(x)
        raise ValueError("Test ValueError")
except Exception as e:
    print(e.args)

## x is bound to return value of __enter__() method

## but in case of with open(file.txt, "rt") as f: //Here f is object of context-manager
f = open("sample.txt", "rt")
with f as g:
    print("__entry__() is returning self:", f is g)

### https://www.python.org/dev/peps/pep-0343/

print("-"*50)
## context manager using generator and contextlib.contextmanager decorator #####################################
import sys
import contextlib

@contextlib.contextmanager
def logging_context_manager():
    print("logging context manager: enter")
    try:
        yield("You are in with block")
        print("logging context manager: normal exit")
    except Exception:
        print("logging context manager: exception exit", sys.exc_info())
        #raise Exception(f"Error: {sys.exc_info()}") ## propagted error outiside with block


with logging_context_manager() as h:
    print(h)

print("."*25)

with logging_context_manager() as x:
    print(x)
    raise ValueError("Logging Failed!") ## exceptions didnt get propagated outiside with block

print("="*50)

#### Multiple Context Managers / Nested Context Managers ##########
import sys
import contextlib

@contextlib.contextmanager
def inner_gen(name):
    print("__enter__() inner context manager")
    try:
        yield name
        print("__exit__() inner context manager: without exception")

    except Exception:
        print("__exit__() inner context manager: with Exception", sys.exc_info())

@contextlib.contextmanager
def outer_gen(name):
    print( "__enter__() outer context manager" )
    try:
        yield name
        print( "__exit__() outer context manager: without exception" )

    except Exception:
        print( "__exit__() outer context manager: with Exception", sys.exc_info() )


## way1 ##
with outer_gen("deva") as f:
    with inner_gen("rohan") as g:
        print(f)
        print(g)


print("."*25)

## way2 ##
with outer_gen("bill") as f, inner_gen("sam") as g:
    print(f)
    print(g)









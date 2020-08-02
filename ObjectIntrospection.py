i =2

print(type(i))
print(i.__class__) # type class has method __class__
print(i.__class__.__name__)
print(i.__class__.__class__)
print(i.__class__.__class__.__class__)

print(issubclass(type, object))

print(dir(i)) # provides class attributes : variables and methods of int class

print(getattr(i, 'numerator'))
print(getattr(i, 'denominator'))

try:
    print(getattr(i, 'index'))

except AttributeError:
    print("Attribute Error! is that attribute is not found")

class Test:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def say_hello(self):
        print(f"hello! {self.name}")


t = Test("Deva")

print(t)
print(type(t))
print(dir(t))

print(getattr(t, 'name'))
print(hasattr(t, 'say_hello'))
print(hasattr(t, "say_hello23"))
print(getattr(t, 'say_hello'))

try:
    print(getattr(t, 'fullname'))
except Exception as e:
    print(e)


print("="*50)
## globals() #####

a = 32
# globals() is dictionary of all global variables
from pprint import pprint as pp
pp(globals())

print("__name__ == '__main__'", globals()['__name__'])

## create global variable using globals() #####

globals()["b"] = 50
print(b)


print("#"*50)
## locals() for all local variables #####

def report_scope(arg):
    from pprint import pprint as pp
    x=400
    pp(locals())

report_scope(10)


print("*"*50)

dic = dict(name="Deva", age=20)
print("My name is {name} and I m {age} years old".format(**dic))
lst = ["Deva", 20]
print("My name is {lst[0]} and I m {lst[1]} years old".format(lst = lst))


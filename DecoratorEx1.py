#decorators: takes callable object as argument and returns callable object too
#Function as decorator

#use case: we need to convert function return into ascii

def vegetable():
    return "blomkål"

def animal():
    return "bjørn"

def mineral():
    return "stål"

# Non Scalable way

def vegetable1():
    return ascii("blomkål")

def animal1():
    return ascii("bjørn")

def mineral1():
    return ascii("stål")

# Scalable way using Decorator

def escape_unicode(func):
    def wrap(*args, **kwargs):
        x = func(*args, **kwargs)
        return ascii(x)

    return wrap

@escape_unicode
def vegetableWithDecorator():
    return "blomkål"

@escape_unicode
def animalWithDecorator():
    return "bjørn"

@escape_unicode
def mineralWithDecorator():
    return "stål"

print(vegetable())
print(animal())
print(mineral())

print("-"*50)

print(vegetable1())
print(animal1())
print(mineral1())

print("."*50)
print(vegetableWithDecorator())
print(animalWithDecorator())
print(mineralWithDecorator())


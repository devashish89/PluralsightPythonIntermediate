def sum(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum+=i

    return sum

def getPersonDetails(name, **kwargs):
    print("."*20)
    print(name)
    print(type(kwargs))
    print(kwargs)

print(sum(1,3))
print(sum(1,3,4))
print(sum())

print("*"*50)

print(getPersonDetails("Deva"))
print(getPersonDetails("Mohan", age=20, email="mohan@abc.com"))
print(getPersonDetails("Sohan", age=30, email="sohan@xyz.com", deptt="Engg."))

print("*"*50)

def test(*args, **kwargs):
    for i in args:
        print(i)

    for k,v in kwargs.items():
        print("{}=>{}".format(k,v))

# def func(**kwargs, *args) is not allowed
# def test2(**kwargs, *args):
#     pass

test(1,2,3,email="xyz@abc.com")


def test3(arg1, arg2, kwarg1, kwarg2, *args, **kwargs):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", kwarg1)
    print("arg4", kwarg2)
    print("*args", args)
    print("**kwargs", kwargs)

## test3(1,2,kwarg1=2,kwarg2=3,5,6,7,8,deptt="HR") ##error

test3(1,2,3,4,5,6,7,8,deptt="HR") #keyword args must be last

print("."*20)

def test3(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print("arg1", arg1)
    print("arg2", arg2)
    print("*args", args)
    print("karg1", kwarg1)
    print("*kargs2", kwarg2)
    print("**kwargs", kwargs)

test3(1,2,3,4,56,7,kwarg2=34, kwarg1=21, age=20, deptt="HR")

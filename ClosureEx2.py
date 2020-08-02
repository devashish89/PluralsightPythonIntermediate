import logging

logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    def log_func(*args, **kwargs):
        logging.info("Running function: {} with args: {} and kwargs: {}".format(func.__name__, args, kwargs))
        print(func(*args, **kwargs))
    return log_func

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

def sub(a,b):
    return a-b

def person_details(**kwargs):
    #print(kwargs)
    #print(kwargs.keys())
    try:
        print("I'm {name}. I'm {age} years old".format(**kwargs))
    except KeyError as e:
        print("Missing key {}".format(e))

fadd = logger(add)
fadd(1,2,3,4)

fsub = logger(sub)
fsub(5,2)

fdetails = logger(person_details)
fdetails(name="Deva", age=30)





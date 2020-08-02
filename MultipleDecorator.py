def logger(original_function):
    import logging
    logging.basicConfig( filename="decorator_test.log", level=logging.INFO)
    def wrapper_logger(*args, **kwargs):
        print("executing function: {} with arguments: {} and keyword arguments: {}".format( original_function.__name__, args, kwargs))
        logging.info( "executing function: {} with arguments: {} and keyword arguments: {}".format( original_function.__name__, args, kwargs))
        result = original_function(*args, **kwargs)
        return result

    return wrapper_logger


def timer(original_function):
    import time
    def wrapper_timer(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()
        print("{} executed for {} secs".format(original_function.__name__,t2-t1))
        return result

    return wrapper_timer

@logger #second: logger(timer(hello))
@timer # first: timer(hello) == wrapper_timer
def hello(name):
    import time
    time.sleep(5) #sleep 5 seconds
    return name


def person_details(name,age):
    import time
    time.sleep(2) #sleep 2 secs
    return "My name is {} and I'm {} years old".format(name,age)


print(hello("John"))
print("."*75)

f = timer(person_details) #@timer
print(f.__name__)

l = logger(f) #@logger
print(l.__name__)

print(l("Danny", 22))
print("."*75)

########## Chain of Decorator function ################

#Below code is similar to writing multiple decorators below
#@timer
#@logger

f=timer(logger(person_details))
print(f.__name__)
print(f("Chintu", 10))

print("#"*75)
##########################################
# below decorator_test.log file you can see that it is creating logs for wrapper_time than person_details() or hello() which
# are original functions because of multiple decorators

# INFO:root:executing function: wrapper
# INFO:root:executing function: wrapper with arguments: ('John',) and keyword arguments: {}
# INFO:root:executing function: wrapper with arguments: ('John',) and keyword arguments: {}
# INFO:root:executing function: hello with arguments: ('John',) and keyword arguments: {} -- correct
# INFO:root:executing function: wrapper with arguments: ('John',) and keyword arguments: {}
# INFO:root:executing function: wrapper_timer with arguments: ('John',) and keyword arguments: {}
# INFO:root:executing function: wrapper_timer with arguments: ('Danny', 22) and keyword arguments: {}
# INFO:root:executing function: wrapper_timer with arguments: ('John',) and keyword arguments: {}
# INFO:root:executing function: wrapper_timer with arguments: ('Danny', 22) and keyword arguments: {}
# INFO:root:executing function: wrapper_timer with arguments: ('John',) and keyword arguments: {}
# INFO:root:executing function: wrapper_timer with arguments: ('Danny', 22) and keyword arguments: {}
# INFO:root:executing function: person_details with arguments: ('Chintu', 10) and keyword arguments: {} --correct

######### Fix to above issue ################################################################

from functools import wraps

def logger1(original_function):
    import logging
    logging.basicConfig( filename="decorator_test.log", level=logging.INFO)

    @wraps(original_function) ## fix
    def wrapper_logger1(*args, **kwargs):
        print("executing function: {} with arguments: {} and keyword arguments: {}".format( original_function.__name__, args, kwargs))
        logging.info( "executing function: {} with arguments: {} and keyword arguments: {}".format( original_function.__name__, args, kwargs))
        result = original_function(*args, **kwargs)
        return result

    return wrapper_logger1


def timer1(original_function):
    import time

    @wraps(original_function)#fix
    def wrapper_timer1(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()
        print("{} executed for {} secs".format(original_function.__name__,t2-t1))
        return result

    return wrapper_timer1

@timer1
@logger1
def say_hello(name):
    import time
    time.sleep(1.5)
    return "Hello, {}".format(name)

@logger1
@timer1
def employee_info(name,age, deptt):
    import time
    time.sleep(2) #sleep 2 secs
    return "My name is {} and I'm {} years old and works for {}".format(name,age, deptt)


say_hello("Rinky")
employee_info("Ram", 40, "HR")






#Instance of class as decorator

class Trace:
    def __init__(self,enabled):
        self.enabled = enabled

    def __call__(self, original_function):
        def wrapper(*args, **kwargs):
            if self.enabled == True:
                print("Executing function: {}".format(original_function.__name__))
            return original_function(*args, **kwargs)

        return wrapper


def sum(*args):
    sum=0
    for i in args:
        sum += i
    return sum

obj = Trace(True)

@obj
def product(*args):
    prod =1
    for i in args:
        prod*=i
    return prod

################################################################################################
obj1 = Trace(True)
f = obj1(sum)
print(f.__name__) #wrapper
print(f(1,2,3,4))
print("."*50)
###############################################################################################
print(product(1,2,3,4))

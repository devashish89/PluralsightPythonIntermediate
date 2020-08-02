#class as decorator

class CallCount:
    def __init__(self, original_function):
        self.original_function = original_function
        self.count = 0

    def __call__(self, *args, **kwargs):
        x = self.original_function(*args, **kwargs)
        self.count += 1
        return "Hello my name is{}".format(x)


def hello(name):
    return "Hello {}!".format(name)

@CallCount
def hello_to_dog(name):
    return "Hello {}! to dog".format(name)


################################################################################
obj = CallCount(hello)
print(obj("John"))
print(obj.count)

#############################################################################
print(hello_to_dog("Sohan"))
print(hello_to_dog("Mohan"))
print(hello_to_dog("Rohan"))

print(hello_to_dog.count)
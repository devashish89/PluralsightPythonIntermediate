def display():
    print("original function")

def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("wrapper executed before original function {}".format(original_function.__name__))
        return original_function(*args, **kwargs) # execute original function and return is None
    return wrapper

dr = decorator_function(display)
print(dr.__name__) #wrapper
f = dr() #execute wrapper()
print(f)
print("."*75)
#############################################################################################
@decorator_function #doing same as above
def display1():
    print("same as above display()")

display1()
print("."*75)
#############################################################################################
@decorator_function
def display_person(name, age):
    print("My name is {} and I'm {} years old".format(name, age))
    
display_person("John", 22)


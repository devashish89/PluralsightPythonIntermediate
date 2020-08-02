def enclosing():
    def local_func():
        print("local func")

    return local_func

lf = enclosing() # returning local func
lf()

print("."*50)

def outer():
    x=3
    def inner(y):
        return x+y

    return inner

i = outer() # returns inner function
print(i(4)) # print  7
#Closure: is a inner function(local function) that remembers or have access to local variables when it was created even when outer function has finished

def outer(msg):
    message = msg
    def inner():
        print(message)

    return inner

f = outer("Hi")
print(f)
print(f.__name__) #inner()
f()
f()
f1 = outer("Hello")
f1()
f1()

def is_even(num):
    return num%2 == 0

print(callable(is_even))

is_odd = lambda x:x%2!=0
print(callable(is_odd))


print(callable(list))
print(callable(list.append))

# instance objects can be made as callable using def __call__() method in class

class Test:
    def __call__(self):
        print("Called!!")

obj = Test()

print(callable(obj))

print(callable("This is not callable")) # strings are not callable




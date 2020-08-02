from typing import List, Any

points = [(x,y) for x in range(5) for y in range(3)]
print(points)

points1 = []
for x in range(5):
    for y in range(3):
        points1.append((x,y))

print(points1)


num_div_tuple = [(num, div) for num in range(1,20) for div in range(1,num) if num % div == 0]
print(num_div_tuple)

#nested comprehensions
num_divList_tuple = [(num,[div for div in range(1,num) if num % div == 0]) for num in range(1,20)]
print(num_divList_tuple)

primeNos =[tup[0] for tup in [(num,[div for div in range(2,num) if num % div == 0]) for num in range(2,100)] if len(tup[1])==0 ]
print(primeNos)


### map() ########

def trace(func):
    def wrapper(*args, **kwargs):
        print("Calling {} with args:{} and kwargs:{}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return wrapper

iterator = map((trace(ord)), "Hello my name is devashish") # map is lazy : as it only producces values when needed

print(iterator.__next__()) # gets ascii value for each character
print(iterator.__next__())
print(iterator.__next__())

print("."*50)

for val in map(ord, "Hello my name is devashish"):
    print(val)

print("-"*50)

print(map(lambda x:x**2, range(1,10)))
print(list(map(lambda x:x**2, range(1,10))))

print("#"*50)

def sum(x,y):
    return x+y

# map on multiple input sequences
squares=map(lambda x, y, z: x*y*z, range(10), range(10), range(10))
print(list(squares))

#### filter ########
print("-"*50)
def prime(num):
    for div in range(2,num):
        if num % div == 0:
            return None
    return num

print(prime(7))
print(prime(10))

primes = filter(prime, range(10))
print(prime)

for i in primes:
    print(i)

print("-"*50)

trues = filter(None, [True, False, 0, -1, 5, None, [], [1,2,3], {}, '', 'hello']) ## remove all False values
print(list(trues))


### reduce #################################
from functools import reduce
import math

def mult(x,y):
    print("{} {}*{}".format(mult.__name__,x,y))
    return x*y

a=reduce(mult, range(1,5))
print(a)

print("="*50)
## important ###
import operator
b = reduce(operator.add, range(1,5), 0) ## if no list is there it will return default value which is 0
print(b)

c = reduce(operator.mul, [], 1)
print(c) # default value = 1





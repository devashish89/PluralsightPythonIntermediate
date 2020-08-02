import socket

def resolve(host):
    print(socket.gethostbyname(host))
    

resolve("sixty-north.com")

from Resolver import Resolver

resolve = Resolver()

print(resolve("google.com")) # implemented __call__ method
# OR
print(resolve.__call__("sixty-north.com")) ## we will never do it in practice
print(resolve._cache)
print(resolve.__call__("pluralsight.com"))
print(resolve._cache)

print("."*50)

from timeit import timeit

print(timeit(stmt="resolve('python.org')", setup="from __main__ import resolve", number=1))

resolve.clearCache()
print(resolve._cache)
print(resolve.has_host("google.com"))
print(resolve("pluralsight.com"))
print(resolve._cache)



print("*"*50)

def sequence_class(immutable):
    return tuple if immutable else list

seq = sequence_class(True)
print(seq("hello"))
print(type(seq("hello")))

seq1 = sequence_class(False)
print(seq1("Deva"))
print(type(seq1("Deva")))



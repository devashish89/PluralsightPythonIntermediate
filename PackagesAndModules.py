import urllib.request

print(type(urllib)) #urllib is packages represented as directory
print(type(urllib.request))
print(type(urllib.request.urlopen))

print("urllib location", urllib.__path__) #urllib is package so __path__ will give the package location
try:
    print("urllib location", urllib.request.__path__) # Error: because it's module not pacakge
except AttributeError as e:
    print(e)

import sys
print(sys.path)


import MyPackage.sum

print( MyPackage.sum.sum1( 1, 2, 3, 4 ) )

print( type( MyPackage ) )
print( MyPackage.__path__ )
print( MyPackage.__file__ )

print("."*50)

import MyPackage.reader
import os
obj = MyPackage.reader.Reader("sample.txt")
print(obj.read())
obj.close()

print("-"*50)
import MyPackage.reader
file1 = r"C:\Users\dnigam\PycharmProjects\PythonIntermediate\MyPackage\compressed\test.bz2"
obj1 = MyPackage.reader.Reader(file1)
print(obj1.read())
obj1.close()

print("-"*50)
import gzip
file2 = "C:\\Users\\dnigam\\PycharmProjects\\PythonIntermediate\\MyPackage\\compressed\\test.gz"
f = gzip.open(file2, "rt")
print(f.read())
f.close()

print("-"*50)
obj2 = MyPackage.reader.Reader(file2)
print(obj2.read())
obj2.close()




import sys

#basics
def division(x,y):
    return x/y
try:
    division(2,1)
except ZeroDivisionError as e:
    print(e.args)
    raise ValueError("Value of second argument can not be 0") from e
else:
    print("No error occurred")

finally:
    print("Alwyas executed")

print("-"*50)

def lookups():
    x = [1,2,3]

    try:
        print(x[5])

    except IndexError:
        print("Handled IndexError")

    d = dict(a=65, b=20, c=30)
    try:
        print(d["a"])
        print(d["e"])
    except KeyError:
        print("Handled KeyError")

print("Method Resolution Order (MRO) of IndexError", IndexError.mro()) # Both IndexError and KeyError inherits from LookupError
print("Method Resolution Order (MRO) of KeyError", KeyError.mro())

lookups()

print("."*50)

def lookups1():
    x = [1,2,3]

    try:
        print(x[5])

    except LookupError:
        print("Handled IndexError")

    d = dict(a=65, b=20, c=30)
    try:
        print(d["a"])
        print(d["e"])
    except LookupError:
        print("Handled KeyError")

lookups1()

import cv2

print(cv2.__version__)

import os
import path

print(os.path.isfile("ExceptionHandlingInheritanceHierarchy.JPG"))

img = cv2.imread("ExceptionHandlingInheritanceHierarchy.JPG", 1)
cv2.imshow("Exception Handling Inheritance Hierarchy", img)
cv2.waitKey(0)


def cal_median(iterable):
    if len(iterable) == 0 or iterable == None:
        raise ValueError("Please provide iterable to argument of function")
    lst = sorted(iterable)
    if len(lst) % 2 == 0:
        return (lst[(len(lst)-1)//2] + lst[(len(lst)-1)//2+1])/2.0

    else:
        return lst[((len(lst)-1)//2)]


print(cal_median([1,2,3,4,5,6,7,8]))
print(cal_median([1,2,3,4,5,6,7,8,9]))
try:
    print(cal_median([]))
except Exception as e:
    print(e)
    print(e.args)

print("-"*50)
### Custom Exception creation############
class TriangleError(Exception):

    def __init__(self,text,sides):
        super().__init__(text)
        self._sides = tuple(sides)
        print(self.args)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "{} for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "TriangleError({}, {})".format(self.args[0], self._sides)


def area_triangle(a, b, c):
    import math
    sides = sorted([a,b,c])
    print(sides)

    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal Triangle", sides)

    else:
        s = sum(sides)/2.0
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

try:
    print(area_triangle(3,4,5))
    print(area_triangle(1,2,10))
except TriangleError as e:
    print(e)
    print(e.args)
    print(str(e))
    print(repr(e))


print("="*50)
####### Chain Exceptions #####
###### implicit chaining exception
import io
import sys
def main():
    try:
        print( area_triangle( 1, 2, 10 ) )
    except TriangleError as e:
        try:
            print(e, file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(e)
            print(f)
            print(f.__context__ is e)


if __name__ == "__main__":
    main()

print("#"*50)
### Explict chaining of Exception################################
import math

class InclinationError(Exception):

    def __init__(self, text):
        super().__init__(text)

    def __repr__(self):
        "InclinationError({!r})".format(self.args[0])

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy/dx))

    except ZeroDivisionError as e:
        raise InclinationError("Slope can not be vertical") from e #using from e explicit chaining with ZeroDivisionError


try:
    inclination(0,5)

except InclinationError as e:
    print(e)
    print(e.__cause__)
    print(e.__traceback__) # traceback object
    import traceback
    traceback.print_tb(e.__traceback__) # print traceback object


### assertion #################################
print("*"*50)

name = "deva"
try:
    assert (name=="sohan")
except AssertionError as e:
    print("Assertion Error", e.args)
else:
    print(name)

name = "Rohan"
try:
    assert (name=="Deva"), f"name is {name}, it should be Deva"
except AssertionError as e:
    print("Assertion Error", e.args)
else:
    print(name)




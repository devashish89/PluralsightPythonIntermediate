class A:
    def func(self):
        return "A.func",


class B(A):
    def func(self):
        return "B.func"

class C(A):
    def func(self):
        return "C.func"

class D(C,B):
    pass

print(D.__bases__) # seeing parent / base classes of D
print(D.__mro__) #seeing the MRO (Method Resolution Order)
print(D.mro())
d = D()
print(d.func())


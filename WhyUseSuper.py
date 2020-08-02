class A:
    def func(self):
        print("A.func")


class B(A):
    def func(self):
        A.func(self)
        print("B.func")


class C(A):
    def func(self):
        A.func(self)
        print("C.func")

class D(B,C):
    def func(self):
        B.func(self)
        C.func(self)
        print("D.func")


d = D()
d.func()

# A.func comming twice which cane be avaoided using super
# C:\Users\dnigam\AppData\Local\Continuum\anaconda3\python.exe C:/Users/dnigam/PycharmProjects/PluralsightPythonIntermediate/MyPackage/WhyUseSuper.py
# A.func
# B.func
# A.func
# C.func
# D.func


#################################################################
print("-"*50)

class A1:
    def func(self):
        print("A1.func")


class B1(A1):
    def func(self):
        super().func() # -->C1.func() and not A.func() because of MRO
        print("B1.func")


class C1(A1):
    def func(self):
        super().func() #-> A1.func() as it is last in MRO
        print("C1.func")

class D1(B1,C1):
    def func(self):
        super().func() # -->B1.func()
        print("D1.func")


d1= D1()
d1.func()
print(D1.mro())

# each method is only called once this happens because of MRO(Method Resolution Order) which use algo C3 Linearization

# A1.func
# C1.func
# B1.func
# D1.func


################################################################
print("#"*50)

class Base:
    def __init__(self):
        print("base class init method")

class Child1(Base):
    def __init__(self):
        super().__init__()
        print("Child1 class init method")

class Child2(Base):
    def __init__(self):
        super().__init__()
        print("Child2 class init method")

class Child3(Child1, Child2):
    def __init__(self):
        super(Child2, self).__init__()
        print("Child3 class init method")

# MRO: Child3 --> Child1-->Child2-->Base
#super(Child2, self).__init__() so next after child2 is Base
#
c3 = Child3()
print(Child3.__mro__)
print("*"*10)
print(super(Child2, c3).__init__())
print("*"*10)

############# super() doesnot always mean parent class ######## VV. Imp.################################

class Tenth:
    def compute(self, *args):
        super().compute(*args) # super() of Tenth is Hundered as per MRO
        print(sum(args)+10)

class Hundered:
    def compute(self, *args):
        print(sum(args)+100)

class D(Tenth, Hundered):
    pass

d = D()
print(D.mro())
d.compute(1,2,3,4,5) # --> Tenth.compute(1,2,3,4,5) --> Hundered(1,2,3,4,5)

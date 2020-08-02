class Base1:
    def __init__(self):
        print("Base1 class __init__ method")

    def method1(self):
        print("method1 of class: Base1")

    def __repr__(self):
        return "{}()".format("Base1")


class Base2:
    def __init__(self):
        print("called {} class __init__ method".format("Base2"))

    def __repr__(self):
        return "{}()".format("Base2")


    def method1(self):
        print("method1 of class: {}".format("Base2"))


    def method2(self):
        print("method2 of class: {}".format("Base2"))


class Child(Base1, Base2):

    def __repr__(self):
        return "{}()".format(self.__class__.__name__)

    def method3(self):
        print("method of class: {}".format(self.__class__.__name__))


c = Child() #First base class init method (Method Resolution Order) in absence of it's own init method
print(c.__dict__)
print(c.__dir__())
print(Child.__bases__) ## IMP. #####
c.method1() # First base class (Method Resolution Order)
c.method2()
c.method3()
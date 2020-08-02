### IMP! we can only inherit the methods from parent class and not attributes

class Base:
    def __init__(self,name):
        print("Base class __init__")
        self.name = name

    def get_name(self):
        print( "{} class func: {} is called".format("Base", "get_name()" ))
        return self.name


class Child(Base):

    def get_name(self):
        print("{} class func: {} is called".format("Child", "get_name()"))
        return super().get_name()


c = Child("Deva") # Base class __init__() method is called because child class does not have
print(c.get_name())
print("."*50)

class Child1(Base):
    def __init__(self,first, last):
        print("Child1 class init method")
        self.fullname = first+" " + last
        super().__init__(self.fullname)

    def get_name(self):
        return self.fullname


c1 = Child1("Deva", "Nigam") # Child1 init mathod is called because it has one
print(c1.get_name())
print("."*50)


a = [1,2,3]
b=a
d=list(a)

print("a==d", a==d)
print("a==b", a==b)
print("a is d", a is d)
print("a is b",a is b)

print("#"*50)
##################### isinstance() #################

print(isinstance("hello", str))#True
print(isinstance(12, int))#True
print(isinstance(12, str))#False
print(isinstance(str(12), str))#True

x = {}

print("x is instance of any of the types", isinstance(x, (str, list, dict, tuple)))

print(isinstance(c, Base))#True
print(isinstance(c1, Base))#True
print(isinstance(c1, Child))#False
print(isinstance(c1, Child1))#True
print(isinstance(c, Child1))#False
print(isinstance(c, Child))#True

##### issubclass #################################
print("Child is subclass of Base", issubclass(Child, Base))#True
print("Child1 is subclass of Base", issubclass(Child1, Base))#True
print("Child1 is subclass of Child", issubclass(Child1, Child))#True

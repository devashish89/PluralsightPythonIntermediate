class Employee:
    raise_percent = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self.firstname, self.lastname,self.pay)

    def get_fullname(self):
        return self.firstname+" "+self.lastname

    def raise_pay(self):
        print(self.__class__.__name__)
        self.pay = (self.pay)*(self.raise_percent) # instance method can access instance and class attributes
        ## careful when using self.raise_percent or Employee.raise_percent
        ##because if we use Employee.raise_percent then changing raise_percent=1.1 in Developer child class won't impact raise_pay as it will use 1.04 only

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.pay + other.pay

    def __len__(self):
        return len(self.get_fullname())

class Developer(Employee):
    raise_percent = 1.1

    def __init__(self,firstname,lastname,pay,programming_language):
        super().__init__(firstname,lastname,pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self,firstname,lastname,pay,employees=None):
        super().__init__(firstname,lastname,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print(emp.get_fullname())


e1 = Employee("Shyam", "Kumar", 20000)
print(e1.pay)
print("######################")
e1.raise_pay()
print(e1.raise_percent)
print(e1.pay)
print("*"*50)

e2 = Developer("Ram", "Kumar", 30000, "Python")
print(help(Developer))
print(e2.pay)
print("######################")
e2.raise_pay() #raise percent = 1.1
print(e2.raise_percent)
print(e2.pay)
print("*"*50)

e3 = Manager("Dev", "Nigam", 50000, [e1,e2])
print(e3.pay)
print("######################")
## Since raise_percent is not in Manager class it will look for raise_percent in Employee (parent class) = 1.04
print(e2.raise_percent)
e3.raise_pay()
print(e3.pay)
e3.print_employees()
print("-"*50)
e3.add_emp(Developer("Deepak", "Rai", 28000, "C#"))

e4 = Manager("Mona", "Singh", 40000, [Developer("Sohan", "B", 22000, "C#"), Developer("Rohan", "Jai", 25000, "C#")])

e3.add_emp(e4)
print("Employees under Manager:{}".format(e3.get_fullname()))
e3.print_employees()

print("-"*50)
print("Employees under Manager:{}".format(e4.get_fullname()))
e4.print_employees()
print("-"*50)

# demo of __add__ method
print(e1+e2)
print(e1.pay+e2.pay)

print(int.__add__(1,2))
print(str.__add__('a', 'b'))
print("test".__len__())

print(e1.get_fullname(), len(e1))

print("="*25+" VV. IMP "+"="*25)
print(isinstance(e3, Manager)) #True
print(isinstance(e3, Employee)) #True
print(isinstance(e3, Developer))#False
print(issubclass(Developer, Employee))# True
print(issubclass(Manager, Employee))# True
print(issubclass(Manager, Developer))# True







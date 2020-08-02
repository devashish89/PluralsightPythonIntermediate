class Employee:
    nums_of_emps = 0 # class variable
    rasiePercent = 1.04 #class variables

    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName #instance variables
        self.lastName = lastName #instance variables
        self.salary = salary #instance variables
        Employee.nums_of_emps +=1

    def get_fullname(self):
        return self.firstName+" "+self.lastName

    def pay_raise(self):
        return self.salary * Employee.rasiePercent

    def number_of_employees(self):
        return Employee.nums_of_emps


emp1 = Employee("John", "Smith", 1000)
emp2 = Employee("Mohan", "Kumar", 2000)

print("emp1 namespace\n", emp1.__dict__) # does not have class variable/attribute rasiePercent
print("."*50)
print("Employee class namespace\n", Employee.__dict__)
print("."*50)
print(emp1.rasiePercent) # first it will look in emp1 namespace and then it will look in Employee class namespace
print(emp2.rasiePercent)
print(Employee.rasiePercent)
print("-"*50)
emp1.rasiePercent = 1.05
print("emp1 namespace\n", emp1.__dict__) # because of that raisePercent =1.05 it has come in emp1 namespace and class attribute value gets over written
print(emp1.rasiePercent) #1.05
print(Employee.rasiePercent) #1.04
print("emp2 namespace\n", emp2.__dict__)
print(emp2.rasiePercent) #1.04
print("*"*50)
Employee.rasiePercent = 1.06 # this will change raisePercent value for all objects
print("emp1 namespace\n", emp1.__dict__) # because of that raisePercent =1.05 it has come in emp1 namespace
print(emp1.rasiePercent) #1.05
print(emp2.rasiePercent) #1.06
print("emp2 namespace\n", emp2.__dict__)
print(Employee.rasiePercent) #1.06
print("Number of employees", Employee.nums_of_emps)
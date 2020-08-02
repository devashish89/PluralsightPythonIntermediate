class Employee:
    def __init__(self,first, last):
        self.first = first
        self.last = last
        self.email = first+"_"+last+"@gmail.com"

    def get_fullname(self):
        return self.first+" "+self.last


emp1 = Employee("John", "Smith")
print(emp1.email)
emp1.first = "Jane"
print(emp1.email) ##email didnt change but firstname changed
print(emp1.get_fullname())

### because of this getters and setters are important!!

class Employee1:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first+"_"+self.last+"@gmail.com" #getter

    @property
    def fullname(self):
        return self.first+" "+self.last #getter


emp2 = Employee1("Deva", "Nigam")
print(emp2.email)
emp2.first = "Devashish"
print(emp2.email)
print(emp2.fullname)
try:
    emp2.fullname = "Mona Lisa" ## Attribute Error
except AttributeError as e:
    print(e)
print(emp2.first)
print(emp2.fullname)

#####################################################
class Employee2:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first+"_"+self.last+"@gmail.com" #getter

    @property
    def fullname(self):
        return self.first+" "+self.last #getter

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ") #setter

    @email.setter
    def email(self, email):
        email = email.replace("@gmail.com","")
        self.first, self.last = email.split("_") #setter

emp3 = Employee2("Deva", "Nigam")
print(emp3.first)
emp3.fullname ="Devashish Nigam"
print(emp3.first)
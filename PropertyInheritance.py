class Employee:
    annualIncrement = 1.1
    deptt = "NA"
    def __init__(self,firstname,lastname, pay=0):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.increment = self.__class__.annualIncrement

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    @fullname.setter
    def fullname(self,value):
        self.firstname, self.lastname = value.split(" ")

    @property
    def email(self):
        return self.firstname + "." + self.lastname+"_"+self.__class__.deptt + "@gmail.com"

    @email.setter
    def email(self, value):
        value = value.replace("@gmail.com")
        self.firstname, self.lastname = value.split(".")

    @property
    def CTC(self):
        return self.pay

    @CTC.setter
    def CTC(self,value):
        self.CTC = value
        return self.CTC


    def salary_increment(self):
        return self.pay*self.increment



class Developer(Employee):
    annualIncrement = 1.15
    defaultBonus = 1000
    deptt = "R&D"
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.increment = self.__class__.annualIncrement


    @property
    def CTC(self):
        return self.pay+self.__class__.defaultBonus

    @Employee.email.setter ## IMP.
    def email(self, value):
        value = value.replace("@gmail.com","")
        self.first, val = value.split(".")
        self.lastname, _ = val.split("_")


e1 = Employee("Jim", "Smith")
print(e1.fullname)
print(e1.__dict__)
e1.pay=30000
print(e1.__dict__)

d1 = Developer("John", "James", 40000, "Python")
print(d1.CTC)
print(d1.email)
d1.fullname = "John Keynes"
print(d1.email)
d1.email = "John.Keynes1_R&D@gmail.com"
print(d1.fullname)






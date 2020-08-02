class Student:
    TotalMarks = 600
    def __init__(self,name, percentage):
        self.name = name
        self.percentage = percentage

    def __repr__(self):
        return "{self.__class__.__name__}({self.name},{self.percentage})".format(self=self)

    # using static method you can NOT access instance OR class attributes/variables
    #used for implementing internal logic which can be tested without using class or object
    @staticmethod
    def calculate_percent(marks, TotalMarks):
        return float(marks/TotalMarks)*100

    # using class method you can NOT access instance variables/ attributes
    # you can only access Class attributes/variables
    # in this case acting as class constructor
    @classmethod
    def get_percent(cls, name, marks):
        return cls( name, cls.calculate_percent(marks, cls.TotalMarks)) #retuns object and acting as constructor


if (__name__ == "__main__"):
    obj1 = Student("deva", 76)
    print(obj1)
    print(obj1.__dict__)

    obj2 = Student.get_percent("Rohan", 550)
    print(obj2)
    print(obj2.__dict__)


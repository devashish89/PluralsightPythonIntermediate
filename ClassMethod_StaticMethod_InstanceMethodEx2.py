class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,self.ingredients)


    @classmethod #as constructor
    def margherita(cls):
        return cls(["Tomato", "Cheese", "Basil"])

    @classmethod
    def prosciutto(cls):
        return cls(["Tomato", "Cheese", "Ham", "Mushroom"])

    @staticmethod #internal implementation
    def _calculate_area(radius):
        import math
        return math.pi *2*radius

    def get_area(self, radius):
        return self._calculate_area(radius)

if (__name__ == "__main__"):
    p1 = Pizza(["Cheese", "Onions", "Tomato"])
    print(p1)
    print(p1.get_area(2))
    print( p1.__dict__ )

    m1 = Pizza.margherita()
    print(m1)
    print(m1.get_area(4))
    print(m1.__dict__ )


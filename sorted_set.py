###https://docs.python.org/3/library/collections.abc.html
## For implementing index methods
#bcoz index, contains etc. all these methods are mixin methods ande gets auto-implmeneted by inheriting collections abtrsct base class: Sequence as we already implemented depended method __len__ and __getitem__ methods
from collections import Container, Iterable
from collections.abc import Sequence, Set

class SortedSet(Sequence, Set):
    def __init__(self,items=None):
        if items is None:
            self.items=[]
        else:
            self.items = sorted(set(items))


    def __repr__(self):
        return "SortedSet({})".format(self.items)

    def __contains__(self,value):
        return value in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __eq__(self,rhs):
        if isinstance(rhs, type(self)):
            print(isinstance(rhs, type(self)), "############")
            return NotImplemented
        return self.items == rhs


    def __ne__(self, rhs):
        if isinstance(rhs, type(self)):
            print(isinstance(rhs, type(self)), "############")
            return NotImplemented
        return self.items != rhs

    def __reversed__(self):
        return list(reversed(self.items))

    # Since inherited count method O(n) and as we know our list is sorted we can implement our own count() using Binary search Tree implementation

    def count(self, value):
        import bisect

        index = bisect.bisect_left(self.items, value)
        found = (index < len(self.items) and self.items[index] == value)
        return 1 if found else 0


    def __add__(self, other):
        self.other = SortedSet(other)
        return list(sorted(set(self.items).union(self.other)))

    def __mul__(self, multiplier):
        result = self.items if multiplier<= 1 else self.items*multiplier
        return result

    def issubset(self, iterable):
        self <= SortedSet(iterable)

    def issuperset(self, iterable):
        self >= SortedSet(iterable)

    def union(self, iterable):
        print( isinstance( set(self), set ), isinstance( set(SortedSet( iterable )), set ) )
        return set(self) | set(SortedSet(iterable))

    def intersection(self, iterable):
        print( isinstance( set( self ), set ), isinstance( set( SortedSet( iterable ) ), set ) )
        return set( self ) & set( SortedSet( iterable ) )

    def symmetric_difference(self, iterable):
        print( isinstance( set( self ), set ), isinstance( set( SortedSet( iterable ) ), set ) )
        return set( self ) ^ set( SortedSet( iterable ) )

    def difference(self, iterable):
        print( isinstance( set( self ), set ), isinstance( set( SortedSet( iterable ) ), set ) )
        return set( self ) - set( SortedSet( iterable ) )

    def isdisjoint(self, iterable):
        print( isinstance( set( self ), set ), isinstance( set( SortedSet( iterable ) ), set ) )
        return True if len(set( self )  & set( SortedSet( iterable ) )) == 0  else False




if __name__ == "__main__":
    print(issubclass(SortedSet, object))
    print(issubclass(SortedSet, Container))
    print(issubclass(SortedSet, Iterable))

    obj = SortedSet([1,2,3,3])
    print(type(obj.items))
    print(obj*3)
    print(obj.union([1,2,3,4,5,8]))

    print(obj.isdisjoint([10,20,30,50]))





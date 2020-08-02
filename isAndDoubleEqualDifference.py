a = [1,2,3]
b = a
c = a.copy()
d = list(a)

print("a==b", a==b)
print("c==a", c==a)
print("a==d", d==a)
print("."*50)
print("a is b", a is b)
print("a is c", a is c)
print("a is d", a is d)

print("="*75)

a1 = [[1,2], [2,3]]
b1 = a1
a1.append([3,4])
print(a1,"\n" ,b1)
print(id(a1) ,id(b1))
c1 = a1.copy()
a1[0] = [10,20]
print(a1,"\n" ,c1)
print(id(a1), id(c1))


sunday = [10,12,12,14,13,11,16]
monday = [10,13,11,14.5,13.2,13,17]
tuesday = [20,22,22,24,23,19,20]

for item in zip(sunday, monday, tuesday):
    print(item)

print("."*50)

for item in zip(sunday, monday, tuesday):
    print("Min: {}, Max: {}, Average:{:1f}".format(min(item), max(item), sum(item)/len(item)))

print("-"*50)

daily = [sunday, monday, tuesday] #list<list>

from pprint import  pprint as pp
pp(daily)

for item in zip(*daily): # transposed
    print(item)
    

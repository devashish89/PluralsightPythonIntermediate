def print_args(arg1, arg2, *args):
    print("arg1",arg1)
    print("arg2", arg2)
    print("*args", args)

t = (1,2,3,4)
print_args(*t) #*t is tuple unpacking into arg1, arg2, args

t1=[5,6,7,8,9]
print_args(*t1)

print("-"*50)

def color(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)

dic = {"red":10,
       "green":20,
       "blue":30,
       "black":40,
       "brown":50}

color(**dic) ##dic unpacking into red, green, blue, **kwargs

dic1 = dict(red=100, green=200, blue=300, black=400, brown=500)
color(**dic1)



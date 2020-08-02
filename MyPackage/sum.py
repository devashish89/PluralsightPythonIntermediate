import functools
def sum1(*args):
    #print(type(args)) #tuples
    return functools.reduce(lambda a,b: a+b, args)

print(__name__)

if __name__ =="__main__":
    print(sum1(1,2,3))
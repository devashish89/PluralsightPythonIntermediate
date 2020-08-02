def trace(f, *args, **kwargs):
    print("*args", args)
    print("**kwargs", kwargs)
    result = f(*args, **kwargs)
    print(result)
    return result

#print(int("ff",16))

trace(int, "ff", base=16)
print("."*50)
trace(int, "0100", 2)

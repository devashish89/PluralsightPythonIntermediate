def logger(original_function):
    def wrapper(*args, **kwargs):
        print(f"Executing {original_function.__name__}({args}, {kwargs})")
        result = original_function(*args, **kwargs)
        return result
    return wrapper

@logger
def sum(a,b):
    return a + b
@logger
def sub(a,b):
    return a - b
@logger
def multiply(a,b):
    return a * b
@logger
def division(a,b):
    return float(a) / float(b)








import math


def math_power_func(val):
    if str( val ).isdigit():
        def get_pow(x):
            return pow( x, val )

        return get_pow

    elif val == "exp":
        def get_exp(x):
            return math.exp( x )

        return get_exp

    else:
        def get_log(x):
            return math.log( x )

        return get_log


f = math_power_func( "exp" )  ## returns get_exp(x) function
print( f( 2 ) )

f = math_power_func( 2 )  ## returns get_pow(x) function
print( f( 5 ) )

f = math_power_func( 'log' )  ## returns get_log(x) function
print( f( math.exp( 1 ) ) )

print( "**************************************************************" )

###### Scope of Variables: LEGB Rule ############################
import builtins
print(dir(builtins))

message = "global"


def enclosing():
    message = "enclosing"

    def local():
        message = "local"
        print("local message:", message)

    def local1():
        """global keyword: changes the scope of variable from local to global"""
        global message
        message = "local1"
        print("local1 message:", message)

    def local2():
        """nonlocal keyword: changes scope of variable to enclosing if it doesn't find matching bidding it will raise syntax error'"""
        nonlocal message
        message="nonlocal"
        print("nonlocal message:", message)

    print( "enclosing message:", message )
    local()
    local1()
    local2()
    print( "enclosing message:", message )


print("global message:", message) #global
enclosing()
print("global message:", message)#global

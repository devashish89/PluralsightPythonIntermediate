class decorator_class:
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print( "call method executed before original function {}".format(self.original_function.__name__ ))
        return self.original_function( *args, **kwargs )  # execute original function and return is None


def display():
    print( "original function" )

@decorator_class
def display_person(name, age):
    print( "My name is {} and I'm {} years old".format( name, age ) )

obj = decorator_class(display)
obj()
print("."*75)
#############################################################################################
display()
print("."*75)
#############################################################################################


display_person( "John", 22 )


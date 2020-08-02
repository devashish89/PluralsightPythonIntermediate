import sorted_set
import inspect

print(inspect.ismodule(sorted_set))
print("------------------------------------")

#print(inspect.getmembers(sorted_set))
print(inspect.getmembers(sorted_set, inspect.isclass)) ## All classes in module(sorted_set) namespace is returned

print("**********************************")

print(inspect.getmembers(sorted_set.SortedSet, inspect.isfunction)) ## methods in sorted_set.SortedSet class

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

# inspect the specific function in  a class
init_signature = inspect.signature(sorted_set.SortedSet.__init__)
print(init_signature.parameters)
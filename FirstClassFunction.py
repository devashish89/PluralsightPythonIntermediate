def square(x):
    return pow(x,2)

print(square(5))
print(square)
func = square # square() - parentheses means we are executing/calling the func so when func to be passed to variable f=square()
print(func)

print("."*50)

def cube(x):
    return pow(x,3)

def my_map(func, data_list):
    lst = []
    for i in data_list:
        lst.append(func(i))
    return lst

print(my_map(square, [1,2,3,4]))
print(my_map(cube, [1,2,3,4]))

print("&"*50)

def html_tag(tag):
    def html_message(msg):
        print("<{}>{}</{}>".format(tag,msg,tag))
    return html_message #html_tag function returning html_message func

print_header1 = html_tag("H1")
print_header1("First Class Function")

print_para = html_tag("p")
print_para("Learning python!")

print(print_para.__name__) # corresponds to html_message() function

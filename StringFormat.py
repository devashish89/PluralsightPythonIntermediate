def sort_by_last_letter(*strings):
    for item in strings:
        def last_letter(item): #local function
            return str(item)[-1]

    return sorted(strings, key=last_letter)

print(sort_by_last_letter("back", "bat", "ball", "ma"))

### LEGB rule: Local, enclosing, Global & Bulit in

g="global"

def outer(p="param"):
    def inner():
        l = "local"
        print(g, p, l)

    inner()

outer() ## inner can only be called inside outer func
# outer.inner() #Error
#inner()


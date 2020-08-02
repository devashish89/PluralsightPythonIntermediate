lst = ["Deva", 20, "Programmer"]
print("I'm {pos[0]}. I'm {pos[1]} years old and works as {pos[2]}.".format(pos=lst))

dic = dict(name="Deva", age=20, job="Programmer")
print("I'm {name}. I'm {age} years old and works as {job}.".format(**dic))
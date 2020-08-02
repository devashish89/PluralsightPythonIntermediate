scientist = ["Marie Curie", "Albert Einstein", "Charles Darwin", "Dmitri Mendeleev",
             "Neil Bohr", "Antonio Lavoisier", "Alfred Wegener"]


# sort by last Name
sorted_scientist = sorted(scientist, key= lambda x:x.split()[-1])
print(sorted_scientist)

print("-"*50)

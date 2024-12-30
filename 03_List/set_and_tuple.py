"""
Set are unordered and cannot be duplicated (cannot use subscription like list)
"""

my_set = {1,2,3,4,5,2,1,2,2}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

my_set.discard(3) # discard function
print(my_set)
my_set.clear() # clear function
print(my_set)
my_set.add(6) # add function
print(my_set)
my_set.update([7,8]) # update function
print(my_set)
my_set.add("Joe") # Set can also mix types like list
print(my_set)

"""
Tuple is ordered and `cannot be changed`
"""
my_tuple = (4,5,2,1,3,10)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[2])

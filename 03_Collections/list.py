"""
List is collection of data
"""

my_list = [80,96,45,30]
print(my_list)
print(my_list[2])

people_list = ["Eric","Jane","Bill","Samanta","Alex"]
print(people_list)
print(people_list[-2])
print(len(people_list)) # len function
print(people_list[0:2]) # slicing
print(people_list[2:]) # slicing
people_list.sort() # sort function (all members of the list must be compared!!
print(people_list)

mix_list = [12,"John",True]
print(mix_list)
mix_list.append("Arun") # append function
mix_list.append(22)
print(mix_list)
mix_list.insert(2,"AAA") # insert function
print(mix_list)
mix_list.remove(True) # remove function
print(mix_list)
mix_list.pop(1) # pop function
print(mix_list)

# Lists Assignment
zoo = ["Panda","Tiger","Dragon","Bird","Snake"]
print(f"Original in Zoo: {zoo}")
print(f"Delete 3rd index: {zoo.pop(3)}, so left {zoo}")
zoo.append('Cat')
print(f"Append Cat: {zoo}")
zoo.pop(0)
print(f"Delete first: {zoo}")
print(f"Only first 3 in List: {zoo[:3]}")
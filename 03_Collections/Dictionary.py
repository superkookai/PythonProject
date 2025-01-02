"""
Dictionary
"""

user_dictionary = {
    "username": "superkookai",
    "name": "Joey",
    "age": 50
}
print(user_dictionary)
print(user_dictionary.get("username"))

user_dictionary["married"] = False # add new key-value
print(user_dictionary)

print(len(user_dictionary)) # number of key-value pairs in Dictionary

# user_dictionary.pop("age") # pop out the key-value pair
# print(user_dictionary)

# user_dictionary.clear() # delete all key-value pairs
# print(user_dictionary)
#
# del user_dictionary # delete Dictionary

for key in user_dictionary:
    print(key)

for key,value in user_dictionary.items():
    print(f"key: {key}, value: {value}")

user_dictionary2 = user_dictionary ## pass by reference
user_dictionary2.pop("age")
print(user_dictionary)

user_dictionary3 = user_dictionary.copy() ## pass by value
user_dictionary3.pop("name")
print(f"dict1: {user_dictionary}")
print(f"dict3: {user_dictionary3}")


## Dictionaries Assignment
print("Dictionaries Assignment")

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for key,value in my_vehicle.items():
    print(f"key: {key}, value: {value}")

vehicle2 = my_vehicle.copy()
vehicle2['number_of_tires'] = 4
vehicle2.pop("mileage")
print(vehicle2.keys())

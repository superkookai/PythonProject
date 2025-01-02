"""
Functions
"""

def my_func():
    print("Inside my function")

def print_my_name(first_name,last_name):
    print(f"Hello {first_name} {last_name}")

# print_my_name("Steve","Job")

def print_color_red():
    color = "Red" # Local variable
    print(color)

color = "Blue" # Global variable
print(color)
print_color_red()

def print_numbers(highest_num,lowest_num):
    print(f"High: {highest_num}")
    print(f"Low: {lowest_num}")

print_numbers(lowest_num=3,highest_num=10) # key-value parameters

## Function that return value
def multiply_num(a,b):
    return a*b
solution = multiply_num(6,5)
print(f"Solution: {solution}")

## Use Loop inside function
def print_list(your_list):
    for mem in your_list:
        print(mem)
print_list([1,2,3,4,5])
print_list(["Joe","Jane","John"])

## Call functions inside another function
def buy_item(cost):
    return cost + add_tax(cost)
def add_tax(cost):
    tax_rate = 0.07
    return cost * tax_rate
final_cost = buy_item(100)
print(f"Final cost is {final_cost}")


# Functions Assignment
print("Functions Assignment")
def create_dict(first_name,last_name,age):
    dict = {}
    dict["first_name"] = first_name
    dict["last_name"] = last_name
    dict["age"] = age
    return dict
print(f"Created Dict: {create_dict('Joe','Doe',35)}")

"""
User Input
"""
from math import floor

first_name = input("Enter your first name: ")
print(f"Hello {first_name}")

input_num = input("Enter your number: ")
print(type(input_num)) # input is return str

# String Assignment
days = input("How many days until your birthday: ")
weeks = floor(int(days) / 7)
print(f"There are {weeks} weeks to your birthday!!")


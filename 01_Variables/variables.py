"""
Variables
"""

cost  = 20
tax_percent = 0.25
tax = cost * tax_percent
total = cost + tax
print(f"Total cost is {total}")

first_name = "John"
last_name = "Doe"
print(first_name + " " + last_name)

first_num = 10
second_num = 22.5
print(first_num)
print(second_num)

first_num = 30 # reassign first_num
print(first_num)
print(second_num)


# Assignment
own_money = 50
buy_item = 15 + (15*0.03)
money_left = own_money - buy_item
print(f"I have ${own_money}, buy gun ${buy_item}. Money left ${money_left}") # f-string

sentence = "Hi {} {}"
print(sentence.format(first_name,last_name)) # format function








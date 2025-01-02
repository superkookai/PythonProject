"""
For and While loop
"""

my_list = [1,2,3,4,5]

## for-in
for num in my_list:
    print(num)

print("_____")
## range
for i in range(len(my_list)):
    print(my_list[i])

print("_____")
## Sum
sum = 0
for num in my_list:
    sum += num
print(f"Sum is {sum}")

print("_____")
## While
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 5:
        break
else:
    print("This is finished while loop [i greater than 10]") # This run only 'finished while loop', not run if break in loop!!

### Loops Assignment
print("Loops Assignment")

day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    i += 1
    for day in day_list:
        if day == "Monday":
            continue
        print(day, end=" ")
    print()









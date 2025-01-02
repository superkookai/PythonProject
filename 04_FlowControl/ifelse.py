"""
Control Flow: if-else
"""
# Indentation is matter in Python
x = 2
if x == 1:
    print("x is equal to 1")
else:
    print("x is not equal to 1")
    print("This still in else block")

print("Outside if-else statement")


# If Else Assignment
print("### If Else Assignment")
grade = 87
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
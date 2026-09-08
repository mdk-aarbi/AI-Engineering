# Problem_9: Write a program to print a right-angled and an inverted pyramid pattern using nested
# loops.

# Right-angled triangle:-
print("Here is the right angled triangle:-")
for x in range(1, 6):
    for y in range(x):
        print("*", end = " ")
    print()
print()

# Inverted pyramid:
print("Here is the inverted pyramid:-")
print()
for x in range(5, 0, -1):
    for y in range(5 - x):             
        print(" ", end = "" )
    for k in range(x):
        print("*", end = " ")
    print()
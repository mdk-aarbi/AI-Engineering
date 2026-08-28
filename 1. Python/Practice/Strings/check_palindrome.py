# Write a program a program that checks whether the given string is palindrome or not.
given = input("Enter the string: ")

flag = True
for index in range(len(given)//2):
    if given[index] != given[len(given) - index - 1]:
        flag = False
        break

if flag:
    print("Palindrome")
else:
    print("Not a palindrome")

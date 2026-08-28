# Write a program which can remove a particular character from a string.
given = input("Enter the string: ")
character =  input("Enter the character to be removed: ")

result = ""
for ch in given:
    if ch != character:
        result += ch

print(result)
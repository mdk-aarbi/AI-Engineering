# find the length of given string without using len() function.
given = input("Enter the string: ")
count = 0
for st in given:
    count += 1

print(f"""The length of string "{given}" is {count}.""")
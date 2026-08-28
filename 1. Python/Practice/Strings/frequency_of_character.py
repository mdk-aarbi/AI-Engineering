# Count the frequency of a particular character in a provided string.
given = input("Enter the string: ")
character = input("Enter the character: ")

count = 0
for ch in given:
    if ch == character:
        count += 1

print(f"The frequency of {character} is {count}.")
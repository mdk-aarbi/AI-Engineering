# # Write a program to count the number of words in a string without using the split().
# given = input("Enter the string: ")

# count = 1
# for ch in given:
#     if ch == " ":
#         count += 1

# print(f"The number of words in the provided string is {count}.")

# Second Solution :-
given = input("Enter the string: ")

lst = list()
temp = ""
for ch in given:
    if ch != " ":
        temp += ch
    else:
        lst.append(temp)
        temp = ""

lst.append(temp)
print(len(lst))
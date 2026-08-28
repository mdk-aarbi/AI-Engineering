# # Write a program to convert a string to title case without using the title().
# given = input("Enter the string: ")

# titled = ""
# for index in range(len(given)):
#     if given[index-1] == " " or index == 0:
#         titled += given[index].upper()
#     else:
#         titled += given[index].lower()

# print(titled)

# Second Solution :-
given = input("Enter the string: ")

lst = list()
for word in given.split():
    lst.append(word[0].upper() + word[1:].lower())

print(" ".join(lst))
# # Extract username from a given email.
# given = input("Enter the email: ")

# username = ""
# for st in given:
#     if st == "@":
#         break
#     username += st

# print(f"The username for email: {given}, is {username}.")

# Second Solution :-
given =  input("Enter the email: ")

position = given.index("@")
print(given[0:position])
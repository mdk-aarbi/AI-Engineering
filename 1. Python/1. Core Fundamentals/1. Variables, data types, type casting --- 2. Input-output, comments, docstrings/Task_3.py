# Write a script that swaps two variables without using a temporary variable.

num_1 = int(input("Enter the number 1: "))
num_2 = int(input("Enter the number 2: "))
print(f"Before swappinng the values are ({num_1}, {num_2}.)")

num_1 = num_1 + num_2
num_2 = num_1 - num_2
num_1 = num_1 - num_2

print(f"After swappinng the values are ({num_1}, {num_2}.)")
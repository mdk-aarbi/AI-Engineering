# Write a program that can convert an integer to string.
given = int(input("Enter the number: "))

result = ""
digits = "0123456789"
while given != 0:
    result = digits[given % 10] + result
    given //= 10

print(result)
print(type(result))
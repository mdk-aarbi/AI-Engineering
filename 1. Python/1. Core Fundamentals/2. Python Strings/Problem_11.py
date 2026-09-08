# Problem_11: Write a Python Program to Find the Sum of the Series till the nth term:

# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

n = int(input("Enter the nth term: "))
x = int(input("Enter the value of x: "))

total = 1
for j in range(2, n+1):
    total += (x**j)/j

print(f"The sum of the series will be {total}.")
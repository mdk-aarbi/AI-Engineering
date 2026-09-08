# Problem_13: Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series
# will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate.
# And the output style should match which is given in the example.

# Example 1:
# Input:-
# 5
# Output:-
# 2+22+222+2222+22222
# Sum of above series is: 24690

n = int(input("Enter the value of n: "))

sum = 0
prod = 0
for k in range(1, n+1):
    prod += 2
    if k == n:
        print(prod)
    else: 
        print(prod, end = "+")
    sum += prod
    prod *= 10

print(f"Sum of above series is: {sum}")
# Problem_12: The natural logarithm can be approximated by the following series.
# (x-1/x) + 1/2(x-1/x)**2 + 1/2(x-1/x)**3 + 1/2(x-1/x)**4 + ...
# If x is input through the keyboard, write a program to calculate the sum of the first seven
# terms of this series.

x = int(input("Enter the value of x: "))

sum = (x-1)/x
for ex in range(2, 8):
    print(f"For ex = {ex}.")
    sum += (1/2)*((x-1)/x)**ex

print(f"The sum of first seven terms of series is {sum}.")
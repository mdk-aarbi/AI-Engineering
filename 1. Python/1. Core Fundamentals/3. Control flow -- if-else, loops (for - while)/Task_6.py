# Write a program that classifies a number as prime.

num = int(input("Enter the number: "))

prime = True
for x in range(2, 10):
    if x is not num:
        if num % x == 0:
            prime = False

if num == 1:
    prime = True

if prime:
    print(f"{num} is prime.")
else:
    print(f"{num} is not a prime.")
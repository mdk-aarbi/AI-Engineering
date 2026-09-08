# Problem_6: Write a program that classifies a number as prime.

num = int(input("Enter the number: "))

if num < 0:
    num *= -1

if num < 2:
    prime = False
else:
    prime = True
    for x in range(2, num + 1):
        if num % x == 0:
            prime = False
            break

if prime:
    print(f"{num} is prime.")
else:
    print(f"{num} is not a prime.")
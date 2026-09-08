# Problem_10: Implement the Collatz sequence for a given starting number using a while loop,
# counting steps to reach 1.

num = int(input("Enter the starting number: "))
count = 0

while(num > 1):
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1

    count += 1
    print(f"{count}. Number = {num}")

print(f"It used {count} steps to reach 1.")
# Problem_7: Implement FizzBuzz for 1–100 using a for loop, then rewrite it using a while loop.

# FizzBuzz for 1-100 using for loop:-
print("FizzBuzz for 1-100 using for loop:-")
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz", end = ", ")
    elif x % 5 == 0:
        print("Buzz", end = ", ")
    elif x % 3 == 0:
        print("Fizz", end = ", ")
    else:
        print(f"{x}", end = ", ")

# FizzBuzz for 1-100 using while loop:-
print("")
print("FizzBuzz for 1-100 using while loop:-")
x = 1
while(x <= 100):
    if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz", end = ", ")
    elif x % 5 == 0:
            print("Buzz", end = ", ")
    elif x % 3 == 0:
        print("Fizz", end = ", ")
    else:
            print(f"{x}", end = ", ")

    x += 1
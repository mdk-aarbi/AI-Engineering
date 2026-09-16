#  a number-guessing game with a limited number of attempts.

import random as rd

rand_num = rd.randint(1, 10)
print("You have 5 chances to guess the number from 1 to 10.")
guessed = False

for x in range(1, 6):
    guess = int(input(f"Try {x}; Guess a number: "))
    if guess == rand_num:
        guessed = True
        break
    print("Wrong, try again...")

print()
if guessed:
    print("Yayyy! you got it.")
else:
    print("Game Over. Better luck next time...")
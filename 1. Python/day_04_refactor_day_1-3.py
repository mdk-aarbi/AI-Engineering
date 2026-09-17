# refactor Day 1-3 scripts so every piece of logic lives in a function.

# Importing the files:-
import random as rd
# ----End of importing the files---

# Functions:-
def temp_conversion(temps):

    if temps == 1:
        cel = float(input("Enter the value in celsius: "))
        print(f"Given {cel} celsius is equal to {(cel * 1.8) + 32} fahrenheit.")
    elif temps == 2:
        fah = float(input("Enter the value in fahrenheit: "))
        print((f"Given {fah} fahrenheit is equal to {(fah-32) / 1.8} celsius."))
    elif temps == 3:
        cel = float(input("Enter the value in celsius: "))
        print(f"Given {cel} celsius is equal to {cel + 273.15} kelvin.")
    elif temps == 4:
        kel = float(input("Enter the value in kelvin: "))
        print(f"Given {kel} kelvin is equal to {kel - 273.15} celsius.")
    elif temps == 5:
        fah = float(input("Enter the value in fahrenheit: "))
        print(f"Given {fah} fahrenheit is equal to {(fah - 32) / 1.8 + 273.15} kelvin.")
    elif temps  == 6:
        kel = float(input("Enter the value in kelvin: "))
        print(f"Given {kel} kelvin is equal to {(kel - 273.15) * 1.8 + 32} fahrenheit.")
    else:
        print("Wrong input. Try Again...")

    print()

def grading_script(marks):

    if marks >= 85 and marks <= 100:
        print("Grade = A")
    elif marks > 79 and marks < 85:
        print("Grade = A-")
    elif marks > 74 and marks < 80:
        print("Grade = B+")
    elif marks > 70 and marks < 75:
        print("Grade = B")
    elif marks > 67 and marks < 71:
        print("Grade = B-")
    elif marks > 63 and marks < 68:
        print("Grade = C+")
    elif marks > 60 and marks < 64:
        print("Grade = C")
    elif marks > 57 and marks < 61:
        print("Grade = C-")
    elif marks > 53 and marks < 58:
        print("Grade = D+")
    elif marks > 49 and marks < 54:
        print("Grade = D")
    elif marks >= 0 and marks < 50:
        print("Grade = F")
    else:
        print("Invalid input. Try again.")

    print()

def number_guessing_game():
    
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

    print()
# -----End of Functions-----

# Main:-
circulate = True

while(circulate):
    print("Enter 1 for temperature conversion.")
    print("Enter 2 for grading script.")
    print("Enter 3 for playing number guessing game.")
    print("Enter 999 to exit.")
    direction = int(input("Enter your direction: "))

    go_round = True
    if direction == 1:
        while(go_round):
            print("Enter 1 to convert from Celsius to Fahrenheit.")
            print("Enter 2 to convert from Fahrenheit to Celsius.")
            print("Enter 3 to convert from Celsius to Kelvin.")
            print("Enter 4 to convert from Kelvin to Celsius.")
            print("Enter 5 to convert from Fahrenheit to Kelvin.")
            print("Enter 6 to convert from Kelvin to Fahrenheit.")
            print("Enter 0 to go back.")
            print("Enter 999 to exit.")
            temps = int(input("Enter your choice: "))

            if temps == 0:
                go_round = False
            elif temps == 999:
                go_round = False
                circulate = False
            else:
                temp_conversion(temps)
    elif direction == 2:
        while(go_round):
            print("Enter 1 for entering the grading script.")
            print("Enter 0 to go back.")
            print("Enter 999 to exit.")
            choice = int(input("Enter your choice: "))

            if choice == 0:
                go_round = False
            elif choice == 999:
                go_round = False
                circulate = False
            elif choice == 1:
                marks = int(input("Enter the marks: "))
                grading_script(marks)
            else:
                print("Wrong Input. Try Again...")
    elif direction == 3:
        while(go_round):
            print("Enter 1 to play the number guessing game.")
            print("Enter 0 to go back.")
            print("Enter 999 to exit.")
            play = int(input("Enter your choice: "))

            if play == 0:
                go_round = False
            elif play == 999:
                go_round = False
                circulate = False
            elif play == 1:
                number_guessing_game()
            else:
                print("Wrong Input. Try Again...")
    elif direction == 999:
        circulate = False
    else:
        print("Wrong Input. Try Again...")

    print()
# ---- End of Main -----
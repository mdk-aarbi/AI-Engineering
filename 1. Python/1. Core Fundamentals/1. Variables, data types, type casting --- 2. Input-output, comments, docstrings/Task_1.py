# Task_1: Write a program that takes a string input from the user and safely casts it to int/float.

st_1 = int(input("Enter a number: "))
st_2 = float(input("Enter a decimal value: "))
print(f"{st_1} = {type(st_1)} and {st_2} = {type(st_2)}")
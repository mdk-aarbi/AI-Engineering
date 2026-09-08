# Problem_14: Write a program that will take a decimal number as input and prints out the binary
# equivalent of the number.

number = int(input("Enter a decimal number: "))

binary = 0
while(number != 0):
    binary += (number % 2)
    binary *= 10
    number /= 2
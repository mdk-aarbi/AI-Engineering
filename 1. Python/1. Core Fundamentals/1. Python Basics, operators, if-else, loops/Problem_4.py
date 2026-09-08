# Problem_4: Write a program `celsius_to_fahrenheit` and its inverse.

cel = float(input("Enter the value in celsius: "))
print(f"You entered {cel} celsius.")
fah = cel * 9/5 + 32
print(f"After conversion, we got {fah} fahrenheit.")
    
fah = float(input("Enter the value in fahrenheit: "))
print(f"You entered {fah} celsius.")
cel = (fah - 32) * 5/9
print(f"After convnersion, we got {cel} celsius.")
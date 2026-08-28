# Write a function `celsius_to_fahrenheit(c)` and its inverse, each validating that input is numeric.

cel = float(input("Enter the value in celsius: "))
print(f"You entered {cel} celsius.")

fah = cel * 9/5 + 32
print(f"After conversion, we got {fah} fahrenheit.")

cel = (fah - 32) * 5/9
print(f"Again, after convnersion, we got {cel} celsius.")
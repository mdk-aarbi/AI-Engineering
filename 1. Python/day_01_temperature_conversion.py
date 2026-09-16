# a temperature converter (C to F to K, both ways) CLI script.

# Getting the initial inputs..
cel = float(input("Enter the value in celsius: "))
fah = float(input("Enter the value in fahrenheit: "))
kel = float(input("Enter the value in kelvin: "))

# Celsius and Fahrenheit:-

# Celsius to Fahrenheit: F = (C * 1.8) + 32
print(f"Given {cel} celsius is equal to {(cel * 1.8) + 32} fahrenheit.")

# Fahrenheit to Celsius: C = (F - 32) / 1.8
print((f"Given {fah} fahrenheit is equal to {(fah-32) / 1.8} celsius."))

# Celsius and Kelvin:-

# Celsius to Kelvin: K = C + 273.15
print(f"Given {cel} celsius is equal to {cel + 273.15} kelvin.")

# Kelvin to Celsius: C = K - 273.15
print(f"Given {kel} kelvin is equal to {kel - 273.15} celsius.")

# Fahrenheit and Kelvin:-

# Fahrenheit to Kelvin: K = (F - 32) / 1.8 + 273.15
print(f"Given {fah} fahrenheit is equal to {(fah - 32) / 1.8 + 273.15} kelvin.")

# Kelvin to Fahrenheit: F = (K - 273) * 1.8 + 32
print(f"Given {kel} kelvin is equal to {(kel - 273.15) * 1.8 + 32} fahrenheit.")
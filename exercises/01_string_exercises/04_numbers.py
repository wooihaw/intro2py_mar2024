# Write a Python script to ask for an integer number, 
# and print the corresponding binary and hexadecimal numbers.
# E.g.
# Enter an integer: 1234
# Binary: 10011010010, Hexadecimal: 4d2

num = int(input("Enter an integer: "))
print(f"Binary: {num:b}, Hexadecimal: {num:x}")
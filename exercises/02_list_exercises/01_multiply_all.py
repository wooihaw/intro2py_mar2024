# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

# Hint
total = 0
for i in alist:
    total = total + i
print(f"{total = }")

# Solution
product = 1
for i in alist:
    product = product * i
print(f"{product = }")

# Use list comprehension
p = 1
product = [p := p*i for i in alist]
print(f"{product[-1] = }")
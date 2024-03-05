# Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result: 
# d4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
d3 = {'e': 50}

# Method 1 - Using the update() method
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)
print(f"{d4 = }")    

# Method 2 - Using the union operator
d5 = d1 | d2 | d3
print(f"{d5 = }")    
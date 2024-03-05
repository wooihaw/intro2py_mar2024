# Write a Python script that takes a list of numbers and returns a new list containing only the even numbers from the original list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 168, -6]
print(f'{alist=}')

# Method 1 - Use the for loop
even1 = []
for i in alist:
    if i % 2 == 0:
        even1.append(i)
print(f"{even1 = }")

# Method 2 - Use list comprehension
even2 = [i for i in alist if i % 2 == 0]
print(f"{even2 = }")

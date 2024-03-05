# Write a Python script to remove duplicates from a list.
# The order of elements should remain unchanged.
alist = [99, 3, -1.2, 2.5, -1.2, -1.2, 5.75, 'xyz', 'a', 99, 'P', 'a', 2.5, 'xyz', 99, 'xyz', 99, 'xyz', 1, -1.2]
print(f'{alist=}')

# Use set
print(list(set(alist)))

# Use for loop
ulist = []
for i in alist:
    if i not in ulist:
        ulist.append(i)
print(f"{ulist = }")

# Use list comprehension
tmp = []
ulist2 = [(i, tmp.append(i))[0] for i in alist if i not in tmp]
print(f"{ulist2 = }")
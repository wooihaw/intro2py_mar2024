# Write a Python script to check if any of the numbers in the list is greater than 100.
# If so, print True. Otherwise, print False.
# Furthermore, print True if all the numbers in the list are greater than 50. Otherwise, print False.
alist = [74, 88, 90, 73, 74, 61, 74, 90, 56, 56, 100, 59, 85, 54, 99, 101]
print(f'{alist=}')

# Use the for loop to check if any of the items in alist is greater than 100
ans = False
for i in alist:
    if i > 100:
        ans = True
        break
if ans:
    print("Yes, there is at least one number greater than 100")        
else:
    print("No, none of the numbers is greater than 100")


# Use any() to check if any of the items in alist is greater than 100
if any(True if i > 100 else False for i in alist):
    print("Yes, there is at least one number greater than 100")        
else:
    print("No, none of the numbers is greater than 100")
    
# Use all() to check if all numbers in the list are greater than 50
if all(True if i > 50 else False for i in alist):
    print("All numbers are greater than 50")
else:
    print("Not all numbers are greater than 50")
    
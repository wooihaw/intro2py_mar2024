# In-class examples for Day 2

#%% Dictionary methods
adict = dict(a=1, b=2.5, c='abc')

print(f"{adict['c'] = }")

# print(f"{adict['d'] = }")  # KeyError as the key is not found in the dictionary

# Use the get() method to return a default value if the key is not found
print(f"{adict.get('d', 'Not found') = }")
print(f"{adict = }")

# The setdefault() method will insert the key and default value if the key is not found
print(f"{adict.setdefault('d', 'Not found') = }")
print(f"{adict = }")

#%% Joining 2 dictionaries

d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(x=4, y=5, z=6)

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 =}")

# Method 2
d4 = d1 | d2
print(f"{d4 =}")

#%% Set operations
alist = [1, 2, 1, 3, 1, 4, 5, 1, 2, 0, 2.5, 0, 'a', 'abc', 2.5, 'a']
blist = list(set(alist))  # a list of unique items from alist

print(f"{alist = }")
print(f"{blist = }")

#%% Set methods
name1 = ['Ali', 'Baba', 'Chen', 'Dave', 'Edward']
name2 = ['John', 'Donald', 'Edward', 'Ali', 'Peter']

common_names = list(set(name1) & set(name2))
print(f"{common_names = }")

all_names = list(set(name1) | set(name2))
print(f"{all_names = }")

#%% Conditional statements
mark = 54
if mark >= 50:
    print("Passed the test")
    print("Still passed the test")
    print("Passed the test again")
else:
    print("Failed the test")
    print("Still failed the test")
    print("Failed the test again")
print("Outside of if-else block")

#%% Ternary operator
num = int(input("Enter an integer: "))
print(f"This is an {'odd' if num%2 else 'even'} number")

# Use if-else statement to perform the same operation
if num % 2:
    print("This is an odd number")
else:
    print("This is an even number")

#%% False value testing
alist = [0]

# Method 1 - Use len() to check whether a list if empty
if len(alist) > 0:
    print("The list is not empty")
else:
    print("The list is empty")

# Method 2 - Check the list itself (empty list is evaluated as false)
if alist:
    print("The list is not empty")
else:
    print("The list is empty")

#%% Examples for loop
names = ['ali', 'baba', 'cloud', 'data']
ages = [13, 37, 23, 43, 56]
blood_types = ['a', 'o', 'b', 'o', 'ab']

# Using indexing to iterate through multiple lists
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old with blood type {blood_types[i]}")

# Using zip() to combine multiple lists
for i, j, k in zip(names, ages, blood_types):
    print(f"{i.capitalize()} is {j} years old with blood type {k.upper()}")
    
# Using enumerate() to automatically add an index to each iteration
for n, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{n}. {i.capitalize()} is {j} years old with blood type {k.upper()}")

#%% Example of while loop

while True:
    name = input("Enter your name: ")
    print(f"Hello {name}")
    ...
    ans = input("Do you want to repeat? (y/[n]) ") or 'n'
    if ans in ('y', 'Y'):
        continue
    elif ans in ('n', 'N'):
        print("Good bye!")
    else:
        print("Invalid choice!")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'eggs', 'cat', 'donkey', 'whale', 'orange')

# Method 1 - Use the for loop
vowel_words1 = []
for w in words:
    if w[0] in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1 = }")

# Method 2 - Use list comprehension
vowel_words2 = [w for w in words if w[0] in 'aeiou']
print(f"{vowel_words2 = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
numbers = [1, 4, 2, 3, 5, 7, 9, 10, 23, 34, 57]

# Method 1 - Use the for loop
count = 0
for n in numbers:
    if n%2:
        count += 1
print(f"There are {count} odd numbers in the list.")      

# Method 2 - Use list comprehension
print(f"There are {sum([n%2 for n in numbers])} odd numbers in the list.")

#%% Dictionary comprehension
#  Create a new dictionary for discounted price (after 10% discount)
prices = dict(apple=1.5, orange=2.5, durian=20, mango=8)

# Method 1 - Use the for loop
new_prices1 = {}
for k in prices:
    new_prices1[k] = prices[k] * 0.9
print(f"{new_prices1 = }")

# Method 2 - Use dictionary comprehension
new_prices2 = {k: prices[k] * 0.9 for k in prices}
print(f"{new_prices2 = }")

#%% Use any() and all() functions
# Check whether any word in the tuple starts with a vowel
words = ('bees', 'cats', 'eggs')
words2 = ('apple', 'orange', 'ice')

# Method 1 - Use the for loop
ans = False
for w in words:
    if w[0] in 'aeiou':
        ans = True
if ans:
    print("There is at least one word that starts with a vowel.")        
else:
    print("There is no word that starts with a vowel.")
    
# Method 2 - Use any() and list comprehension
if any(True if w[0] in 'aeiou' else False for w in words):
    print("There is at least one word that starts with a vowel.")        
else:
    print("There is no word that starts with a vowel.")
    
# Check whether all words in the tuple starts with a vowel
if all(True if w[0] in 'aeiou' else False for w in words2):
    print("All words starts with a vowel.")        
else:
    print("Not all words start with a vowel.")

#%% Use pickle to store dictionary to a file
import pickle

data = {}
ans = 'y'
while ans.lower() in ('y', 'yes'):
    name = input("Enter name: ") or "Unknown"
    age = input("Enter age: ") or "0"
    data[name] = age
    ans = input("Do you want to enter another data? ([y]/n) ") or "y"

print(f"{data =  }")

with open("nameage.pkl", "wb") as f:
    pickle.dump(data, f)

#%% Use pickle to retrieve the dictionary from file
import pickle

with open("nameage.pkl", "rb") as f:
    mydata = pickle.load(f)

print(f"{mydata = }")



  






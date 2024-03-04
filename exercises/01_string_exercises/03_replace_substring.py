# Write a Python script to ask for a string and two substrings,
# and print the string with all occurrences of the first substring
# replaced by the second substring.
# E.g.
# Enter a string: Hello world!
# Enter substring to replace: world
# Enter replacement substring: Python
# Hello Python!

s = input("Enter a string: ")
t = input("Enter substring to replace: ")
u = input("Enter replacement substring: ")
print(s.replace(t, u))
# In-class examples for Day 1

#%% Numeric data types
a = 7869678671283487621378164083270372814028374098273409809781238947
b = a ** 10
print(a, b)
print(a.__sizeof__())
print(b.__sizeof__())

c = 1_234_567
print(c)
print(c.__sizeof__())

#%% Binary and hexadecimal numbers
a = 0b10110101
b = 0x12cafe
print(a, b)
print(bin(a), hex(b))
print(bin(1234), hex(1234))

#%% Variables

# class = 1  # Using keyword as a variable name will cause a syntax error

a = 'bcd'
print(type(a))

#type = 2  # Built-in function will be shadowed by variable of the same name
#print(type(a))

#%% Convert between data types
a, b, c = 1, 2.3, '456'
print(type(a), type(b), type(c), sep=', ')

d = float(a)
e = str(b)
f = int(c)

print(d, e, f, sep=', ')
print(type(d), type(e), type(f), sep=', ')

g = 'abc'
h = int(g, base=16)
print(h)

#%% Arithmetic operators
a = 3 ** 2
b = -3 ** 2
c = (-3) ** 2

print(a, b, c, sep=', ')

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 50)
print(100 <= b < 200)

#%% String indexing and slicing
s = "Introduction to Python"
print("First character: ", s[0])
print("Last character: ", s[-1])
print("First 12 characters: ", s[:12])
print("Last 6 characters: ", s[-6:])

s1 = s[0]  # indexing
s2 = s[0:1]  # slicing

print(type(s1), type(s2), sep=" ,")

print(s[:12:2])

#%% String concatenation and repetition 
a = '45'
s = '123'
t = a + s  # string concatenation
print(t)

u = 5 * a # string repetition
print(u)

print(10 * "Ha ")

#%% String methods
s = "Introduction to Python"
print(s.upper())
print(s.lower())
print(s.title())
print(s.replace('n', 'm'))
print(s)

s1 = 'Abc'
s2 = '123'
s3 = s1 + s2

print(s1.isalpha())
print(s2.isdigit())
print(s3.isalpha())
print(s3.isalnum())

s4 = s3.lower().replace('c', 'z')  # methods can be chained
print(s4)

#%% f-string formatting
for i in range(10, 101, 10):
    print(f"{i:>5} {i**2:>7} {i**3:>9}")

for i in range(20):
    print(f"{i:>3} {i:>6b} {i:>3x}")
    
a = 12.345
b = 6789

print(f"{a = }, {a = :.1f}, {a = :.2f}")

print(f"Binary: {b:016b}, Hex: {b:04X}")
















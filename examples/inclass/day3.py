# In-class examples for Day 3

#%% Exception Handling

while True:
    try:
        num = int(input("Enter an integer: "))
    except Exception as e:
        print("Invalid input!", e)
    else:
        print(f"You have entered {num}")
        break

#%% Functions and return value
def myfunc1(x, y):
    print(x, y)

def myfunc2(x: int|float, y: int|float) -> int|float:
    '''This is a function to add 2 arguments'''
    return x + y

a = myfunc1(11, 22)

b = myfunc2(33, 44)

print(f"{a = }, {b = }")

#%% Function that returns multiple values
def myfunc3(x: int, y: int, z: int) -> tuple[int]: 
    '''This is a function which returns 3 values'''
    return x*x, y*y, z*z

a = myfunc3(2, 3, 4)
print(f"{a = }, {type(a) = }")

b, c, d = myfunc3(5, 6, 7)
print(f"{b = }, {c = }, {d = }")

*e, f = myfunc3(8, 9, 10)
print(f"{e = }, {f = }")

#%% Functions are objects
def func1(x):
    return x + 1

def func2(y):
    return y - 1

def func3(z):
    return z * 2

functions = (func1, func2, func3)
for f in functions:
    print(f(10))

d_func = {'function1': func1, 'function2': func2, 'function3': func3}
for k in d_func:
    print(f"{k} output: {d_func[k](10)}")
    
#%% Lambda function example 1
alist = [(1, 2, 3), (11, 4, 1), (7, 9, 2)]
blist = sorted(alist)
print(f"{blist = }")

# To sort according to the 3rd element in descending order
clist = sorted(alist, key=lambda x: x[2], reverse=True)
print(f"{clist = }")

#%% Lambda function example 2
# Sort the list based on the ID numbers
IDs = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID82', 'ID1234']

sorted_IDs = sorted(IDs)
print(f"{sorted_IDs = }")

new_sorted_IDs = sorted(IDs, key=lambda x: int(x[2:]))
print(f"{new_sorted_IDs = }")

print(f"ID of oldest member: {min(IDs, key=lambda x: int(x[2:]))}")
print(f"ID of newest member: {max(IDs, key=lambda x: int(x[2:]))}")

#%% Lambda function example 3
GID = ['G2ID25', 'G1ID14', 'G1ID2', 'G2ID10', 'G1ID25']

print(f"{sorted(GID) = }")

# Sort G in descending order and ID in ascending order
sorted_GID = sorted(GID, key=lambda z: (-int(z[1]), int(z[4:])))
print(f"{sorted_GID = }")

#%% Using map() function
# Reverse each string in a list
words = ['apple', 'bell', 'cat', 'door', 'eggs']

# Methods 1 - Use the for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Method 2 - Use list comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map() function
r3 = list(map(lambda w: w[::-1], words))
print(f"{r3 = }")

#%% Using filter() function
# Select only the palindrome  from a list
words = ('ant', 'boy', 'civic', 'dad', 'fish', 'madam')

# Method 1 - Use the for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")

# Method 2 - Use list comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")

# Method 3 - Use filter() function
p3 = list(filter(lambda w: w == w[::-1], words))
print(f"{p3 = }")

#%% Functional approach

# Function to add a book
def add_book(library, book):
    library.append(book)
    
# Function to remove a book
def remove_book(library, book):
    if book in library:
        library.remove(book)

# Function to display the books in the library
def display_book(library):
    for book in library:
        print(book)
        
library1 = []
add_book(library1, 'Harry Porter and the Goblet of Fire')
add_book(library1, 'Harry Porter and the Deathly Hallows')
add_book(library1, 'Fantastic Beasts and Where to Find Them')
display_book(library1)
remove_book(library1, 'Fantastic Beasts and Where to Find Them')
display_book(library1)

library2 = []
add_book(library2, 'Introduction to Python')
add_book(library2, 'Fluent Python')
display_book(library2)

#%% OOP approach
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            
    def display_book(self):
        for book in self.books:
            print(book)

library1 = Library()
library1.add_book('Machine Learning with Python')
library1.add_book('Deep Learning Fundamentals')
library1.display_book()

library2 = Library()
library2.add_book('Physics')
library2.add_book('Chemistry')
library2.add_book('Biology')
library2.add_book('Mathematics')
library2.display_book()

library2.remove_book('Biology')
library2.display_book()

print(type(library1))

#%% OOP Example
class Rectangle:
    desc = 'This is a rectangle'
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.__secret = "Top secret"  # private attribute
    def __str__(self):
        return f"Rectangle with length of {self.length} and width of {self.width}"
    def __repr__(self):
        return f"Rectangle({self.width}, {self.length})"
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self. length + 2*self.width
    def __gt__(self, other):
        return self.area() > other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def reveal_secret(self):
        return f"The secret is {self.__secret}"
    
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 4)
print(r1, r2, sep="\n")

rlist = [r1, r2]
print(rlist)

for r in rlist:
    print(f"{r}, area: {r.area()}, perimeter:{r.perimeter()}")

if r1 > r2:
    print(f"{r1} is greater than {r2}")
else:
    print(f"{r1} is smaller than {r2}")
    
if r1 < r2:
    print(f"{r1} is smaller than {r2}")
else:
    print(f"{r1} is bigger than {r2}")
    
r3 = Rectangle(3, 2)
if r1 == r3:
    print(f"{r1} is the same as {r3}")
    
print(f"Public attribute: {r1.length}")

print(f"Private attribute: {r1.reveal_secret()}")

# Child class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f"Square with side of {self.length}"
    def __reprt__(self):
        return f"Square({self.length})"

s1 = Square(5)
s2 = Square(6)

print(s1, s2, sep="\n")

if s1 > s2:
    print(f"{s1} is greater than {s2}")
else:
    print(f"{s1} is smaller than {s2}")
    
    
    
    
    
    
    
    
    
    
    
    
    



















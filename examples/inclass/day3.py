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

















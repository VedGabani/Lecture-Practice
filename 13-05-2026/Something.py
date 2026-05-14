# All Type of python fn

'''

TNRN
TSRN
TNRS
TSRS

T - Take argument
R - Return value
N - No argument
N - No return value

'''

# TNRN

print("\n")

def greet():
    print("Welcome to the world of python.....")

greet()

# TSRN

print("\n")

def add(a,b):
    print("Addition -_- ", a+b)

add(10,20)

# TNRS

print("\n")

def message():
    return"Hello python....."

print(message())


# TSRS

print("\n")

def multiply(x,y):
    return x*y

print(multiply(5,5))

# Diagram
# Return TNRS , TSRN
# Argument TNRN
# Both TSRS

# Return ends fn executation

print("\n")

def cal(a,b):
    return a+b , a-b

x,y = cal(10,5)

print(x)
print(y)

# 1D Arry
# In Python a list is used to store multiple values in a single variable
# Example

print("\n")

marks = [77 , 99 , 88 , 66 ]
print(marks)

# Accessing Element using index

print("\n")

numbers = [1 , 2 , 3 , 4 , 5]
print(numbers[0])

# Nagative indexing

print("\n")

print(numbers[-1])

# Changing arry element

print("\n")

numbers[1] = 20
print(numbers)

# List traversing using loop

print("\n")

for i in numbers:
    print(i)

# Using rangle fn with indexing

print("\n")

for i in range(len(numbers)):
    print("Index -_- " , i , "Value" , numbers[i])

# Add element at end of list

print("\n")

numbers.append(11)
print(numbers)

# Inser() in list

print("\n")

numbers.insert(3 , 30)
print(numbers)

# Remove element

print("\n")

numbers.remove(1)
print(numbers)

numbers.pop()
print(numbers)

# Searching
print("\n")

if 2 in numbers:
    print("Found")

# List slicing

print("\n")

print(numbers[1:4])

# Sum of List elements

print("\n")

total = 0
for i in numbers:
    total += 1

print(total)
total = sum(numbers)

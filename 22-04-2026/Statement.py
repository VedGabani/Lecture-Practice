# Python Statement

# if....else Statement

print("----- if...else -----\n")

dooropen = True

if dooropen:
    print("Welcome to Home -_- ")

else:
    print("No one is at Home -_- ")

# if.....elif.....else Statement

print("\n----- if.....elif.....else Statement -----\n")

a = int(input("Enter your Number -_- "))

if a>0:
    print(f"{a} Number is Positive -_- ")

elif a<0:
    print(f"{a} Number is Negative -_- ")

else:
    print(f"{a} is Zero -_- ")

# Find Largest of 2 number

print("\n----- Find Largest of 2 Number -----\n")

a = int(input("Enetr First Number -_- "))
b = int(input("Enetr Second Number -_- "))
print("\n")

if a>b:
    print(f"{a} is greater than {b} -_- ")

elif a<b:
    print(f"{b} is greater than {a} -_- ")

else:
    print(f"{a} and {b} both are equal -_- ")

# Check 

print("\n----- Leap Year -----\n")

year = int(input("Enter a year -_- "))

if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0):
    print("Leap Year ✅")

else:
    print("Not a Leap Year ❌")

# Loop in Python

#while loop

print("\n----- While Loop -----\n")

a = int(input("Enter number to Start loop -_- "))
b = int(input("Enter number to End loop -_- "))

print("\n")

i = a
while i < b:
    print(i)
    i += 1

# For Loop

print("\n----- For Loop -----\n")

a = int(input("Enter number to End loop -_- "))
for i in range(a):
    print(i)

# List

print("\n----- List -----\n")

fruits = ["Apple" , "Banana" , "Orange" , "Mango"]

for fruit in fruits:
    print(fruit)

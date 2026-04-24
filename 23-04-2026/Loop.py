# Print number from 1 to 10

print("----- Print number from 1 to 10 -----\n")

for i in range(1 , 11):
    print(i)

# Print Even number

print("\n------ Print Even number -----\n")

for i in range(1 , 21):
    if i % 2 == 0:
        print(i)

# Sum of first N number

print("\n----- Sum of first N number -----\n")

a = int(input("Enter number for Sum -_- "))
total = 0

for i in range(1 , a+1):
    total += 1

print("Sum -_- ", total)

# While loop

print("\n----- While loop -----\n")

a = int(input("Enter number -_- "))
fact = 1

while a>0:
    fact += a
    a -= 1
print("Factorial -_- ", fact)

# Pattern Program

print("\n----- Pattern Program -----\n")

# Right Triangle

print("\n----- Right Triangle -----\n")

a = int(input("Enter number of Rows -_- "))

for i in range(1 , a+1):
    print("*" *i)

# Reverse Triangle

print("\n----- Reverse Triangle -----\n")

a = int(input("Enter number of Rows -_- "))

for i in range(a , 0 , -1):
    print("*" *i)

# Nested loop

print("\n----- Nested loop -----\n")

# Multiplication table

print("\n----- Multiplication table -----\n")

end = ""
for i in range (1 , 6):
    for j in range (1 , 11):
        print(i * j , end=" ")
        print()

# Break and Continue

print("\n----- Break and Continue -----\n")

for i in range (1 , 10):
    if i == 5:
        break
print(i)

for i in range (1 , 10):
    if i == 5:
        continue
print(i)

# Reverse a number

print("\n----- Reverse a number -----\n")

a = int(input("Enter number to Reverse -_- "))
rev = 0
while a>0:
    calc = a%10
    rev = rev * 10 + calc
    a //= 10
    print("Reversed -_- ", rev)

# Loop with string

print("\n----- Loop with string -----\n")

text = "Python"
for ch in text:
    print(ch)

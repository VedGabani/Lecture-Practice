# List

print("\----- List -----\n")

my_list = [10, 20, 30, 40]
print("List -_- ", my_list)

print("\n")

# Mutability

print("\----- Mutability -----\n")

my_list[0] = 100
print("Mutability List -_- ", my_list)

print("\n")

# append()

print("\----- append() -----\n")

my_list.append(50)
print("Append List -_- ", my_list)

print("\n")

# Max() and Min()

print("\----- Max() and Min() -----\n")

print("Max -_- ", max(my_list))
print("Min -_- ", min(my_list))

print("\n")

# Remove duplicats menually

print("\----- Remove duplicats menually -----\n")

unique = []
for i in my_list:
    if i not in unique:
        unique.append(i)
print("Unique List -_- ", unique)

print("\n")

# Tuple (Not Mutable)

print("\----- Tuple (Not Mutable) -----\n")

my_tuple = (1, 2, 3, 4)
print("Orignal Tuple -_- ", my_tuple)
print("\n")

# Count Occurence

print("\----- Count Occurence -----\n")

print("Counr 2 -_- ", my_tuple.count(2))

print("\n")

# Swapping using Tuple

print("\----- Swapping using Tuple -----\n")

a , b = 10 , 20
a , b = b , a
print("Value -_- ", a,b)

print("\n")

# Set

print("\----- Set -----\n")

set = {1, 2, 3, 4, 5}
print("Set -_- ", set)

print("\n")

# Set Operator

print("\----- Set Operator -----\n")

a = {1, 2, 3}
b = {3, 4, 5}
print("Union -_- ", a|b)

print("\n")

# Dictionary

print("\----- Dictionary -----\n")

s = {"Name":"Ved" , "Marks":"85"}
print("Student -_- ", s)

print("\n")

s["Marks"] = 90
print("Student -_- ", s)

print("\n")

# Using loop using dict

print("\----- Using loop using dict -----\n")

for key,value in s.items():
    print(key,":",value)

print("Students Marks -_- ", s["Marks"])

print("\n")

# Find Topper

print("\----- Find Topper -----\n")

s = ["A":80,"B":85,"C":90]

topper.max(student,key = student.get)
print("Topper -_- ", topper)

print("\n")

# List Comprihension

print("\----- List Comprihension -----\n")

n = [i for i in range(5)]
print("Numbers -_- ", n)

even = [i for i in range(10) if i%2 == 0]
print("Even -_- ", even)

print("\n")

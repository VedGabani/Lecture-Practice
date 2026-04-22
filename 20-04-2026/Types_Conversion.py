'''

Type conversion

Explicit type coversion

int() constructor

'''

# String to int

print("----- String to int -----\n")

num_str = "89"
print("Type of num_str -_- ", type(num_str))
num_int = int(num_str)
print(f"string `{num_str}` -> int{num_int}, type:{type(num_int)}")

print("\n")

# Float to int

print("----- Float to int -----\n")

num_float = 3.14
print(f"Float {num_float} -> int:{int(num_float)}")

print("\n")

# Boolean to int

print("----- Boolean to int -----\n")

print(" True -> ", int(True))
print(" False -> ", int(False))

print("\n")

# Float to string

print("----- Float to string -----\n")

str_float_num = 3.14
str_float = str(str_float_num)
print(f"(str_float_num) -> str:{str_float}, type:{type(str_float)}")

print("\n")

# String to List/Type/set

# List

print("----- List -----\n")

list1 = [1, 2, 3]
print(list1)
print(type(list1))

print("\n")

# Tuple

print("----- Tuple -----\n")

tuple1 = (1, 2, 3)
print(tuple1)
print(type(tuple1))

print("\n")

# Set

print("----- Set -----\n")

set1 = {1, 2, 3}
print(set1)
print(type(set1))

print("\n")

# Dict

print("-----   -----\n")

dict1 = {'a':1 , 'b':2}
print(dict1)
print(type(dict1))

print("\n")

# id() fuction memory address

print("----- id() fuction memory address -----\n")

a = int(input("Enter value for A -_- "))
b = int(input("Enter value for B -_- "))
c = int(input("Enter value for C -_- "))

print(f"(a) : {id(a)}")
print(f"(b) : {id(b)}")
print(f"(c) : {id(c)}")

print("\n")

# With mutable obj

print("-----  With mutable obj -----\n")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nid(list1) : {id(list1)}")
print(f"\nid(list2) : {id(list2)}")
print(f"\nid(list3) : {id(list3)}")

print("\n")

# List to Str

print("----- List to Str -----\n")

a = (1, 2, 3)
b = str(a)
print(f"(a) -> str:{b}, type:{type(b)}")

print("\n")

# List to Tulpe

print("----- List to Tulpe -----\n")

a = (1, 2, 3)
b = tuple(a)
print(f"(a) -> tuple:{b}, type:{type(b)}")

print("\n")

# List to Set

print("----- List to Set -----\n")

a = (1, 2, 3)
b = set(a)
print(f"(a) -> set:{b}, type:{type(b)}")

print("\n")

'''
# List to Dict

a = (1, 2, 3)
b = dict(a)
print(f"(a) -> dict:{b}, type:{type(b)}")

print("\n")

'''
# List to Int

print("----- List to Int -----\n")

a = (1, 2, 3)
b = int(a)
print(f"(a) -> int:{b}, type:{type(b)}")


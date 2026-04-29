# List and Tuple in Python(Basic & Mutability)

# List-Mutable

my_list = [1, 2, 3, "Ved"]

print("List -_- ", my_list)

my_list[1] = 99

print("List -_- ", my_list)

my_list[3] = 100

print("List -_- ", my_list)

# Tuple can't be changed like List

# Using list width slicing and Formatting

s = ["Honda","Inova","BMW","Mercedes"]

print("First 2 Cars -_- ", s[:2])

# String Formatting using List

for cars in s:
    print("Best car is ", cars)

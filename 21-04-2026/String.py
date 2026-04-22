# Python String Manipulation

print("----- Python String Manipulation -----\n")

s1 = 'Hello'
s2 = "World"
s3 = ''' Multiline
        String '''
s4 = r"Raw \n String"

print(s1)
print(s2)
print(s3)
print(s4)

print("\n")

# Comman string method

print("----- Comman string method -----\n")

s = input("Enter your Word -_- ")
a = input("Enter word that you want to find which Ends -_- ")
b = input("Enter word that you want to find which Starts -_- ")
c = input("Enter word you want to find -_- ")
d = input("Enter letter that you want to count -_- ")
print("\n")
print(s.upper())
print(s.lower())
print(s.split())
print(s.endswith(a))
print(s.startswith(b))
print(s.find(c))
print(s.count(d))

print("\n")

# String Formatting

print("----- String Formatting -----\n")

name = input("Enter your Name -_- ")
age = int(input("Enter your Age -_- "))

print("\n----- f String -----\n")

print(f"Name -_- {name} Age -_- {age}")

print("\n----- . Formatting -----\n")

print("Name -_- {} Age -_- {} ".format(name , age))

# Slicing

print("\n----- Slicing -----\n")

a = input("Enter your Words -_- ")

print("\n")
print("a[0]")
print("a[9]")
print("a[0:5]")
print("a[:5]")
print("a[::-1]")

# Joining and Splitting in Python

print("\n----- Joining and Splitting in Python -----\n")

words = ["Python","is","Awesome"]

print(" ".join(words))
print("-".join(words))
print("+".join(words))

splits = ("a, b, c")
print(splits.split(","))

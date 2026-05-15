# Q-5

arr = []

size = int(input("Enter a size -_- "))

print("\n")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n")

find = int(input("Enter a number to find -_- "))
found = False
for i in range(len(arr)):
    if arr[i] == find:
        print("\nElement index -_- ", i)
        found = True
        break

if found == False:
    print("\nNot found elements")

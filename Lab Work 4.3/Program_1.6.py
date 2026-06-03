# Q-6

arr = []
size = int(input("Enter a range -_- "))
print("\n")

for i in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n",arr)

print("\n")

find = int(input("Enter a number to find -_- "))
found = False

for i in range(len(arr)):
    if arr[i] == find:
        print("\nElement Index -_- ", i)
        found = True
        break

if found == False:
    print("\nNot Found Element")

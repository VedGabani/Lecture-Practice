# Q-4

arr = []
size = int(input("Enter a range -_- "))
print("\n")

for i in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n",arr)

print("\n")

a = int(input("Enter a number to delete -_- "))

print("\n")

arr.remove(a)

print(arr)

# Q-5

arr = []
size = int(input("Enter a range -_- "))
print("\n")

for i in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n",arr)

print("\n")

a = int(input("Enter a index number -_- "))
b = int(input("Enter a number to change -_- "))

print("\n")

arr[a] = b

print(arr)

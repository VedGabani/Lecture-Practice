# Q-6

arr = []

size = int(input("Enter a size -_- "))

print("\n")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\nArray for even number\n")

for i in arr:
    if i%2 == 0:
        print(i)

print("\nArray for odd number\n")

for i in arr:
    if i%2 != 0:
        print(i)

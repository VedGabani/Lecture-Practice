# Q-7

arr = []

size = int(input("Enter a size -_- "))

print("\n")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\nFirst five elements are\n")

for i in range(5):
    print(arr[i])

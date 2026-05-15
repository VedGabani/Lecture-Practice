# Q-8

arr = []

size = int(input("Enter a size -_- "))

print("\n")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n")

print("First Element are -_- ", arr[0])

print("\n")

print("Last Element are -_- ", arr[-1])

print("\n")

a = len(arr)//2

print("Middle Element are -_- ", arr[a])

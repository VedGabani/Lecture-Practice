# Q-3

arr1 = []
arr2 = []
arr3 = []

size = int(input("Enter a size -_- "))

print("\nEnter value for array 1\n ")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr1.append(value)

print("\nEnter value for array 2\n ")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr2.append(value)

print("\n")

for i in range(size):
    arr3.append(arr1[i] + arr2[i])

print("Arry Result -_- ", arr3)

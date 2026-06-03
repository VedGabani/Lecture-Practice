# Q-6

print("\nEnter element for 1nd arr\n")
arr1 = []
size = int(input("Enter a range -_- "))
print("\n")

for i in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr1.append(value)

print("\n",arr1)

print("\nEnter element for 2nd arr\n")

arr2 = []

for i in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr2.append(value)

print("\n",arr2)


print("\n")

combine = arr1 + arr2

print(combine)

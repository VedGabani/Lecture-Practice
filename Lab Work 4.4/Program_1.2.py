# Q-2

arr = []

size = int(input("Enter a size -_- "))

print("\n")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n")

sum = 0

for i  in arr:
    sum += i

average = sum/size

print("Average of arry -_- ", average)

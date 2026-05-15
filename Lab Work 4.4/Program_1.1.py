# Q-1

arr = []

size = int(input("Enter a size -_- "))

print("\n")

for i  in range(size):
    value = int(input(f"a[{i}] -_- "))
    arr.append(value)

print("\n")

count = 0
for i in arr:
    count+=1

print("\nLength of arry -_- ", count)
print("\nOrignal arry -_- ", arr)
